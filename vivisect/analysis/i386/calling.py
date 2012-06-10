
"""
An i386 specific function analysis module that is designed to
attempt to detect the calling convention.
"""

import vivisect
import vivisect.impemu as viv_imp
import vivisect.impemu.emufunc as viv_imp_emufunc

from vivisect.impemu.impmagic import *

import visgraph.pathcore as vg_path

import envi
import envi.archs.i386 as e_i386
import envi.archs.i386.opcode86 as opcode86

thiscall_regs =  [e_i386.REG_ECX,]
msfastcall_regs = [e_i386.REG_ECX, e_i386.REG_EDX]
bfastcall1_regs = [e_i386.REG_EAX ]
bfastcall2_regs = [e_i386.REG_EAX, e_i386.REG_EDX ]
bfastcall3_regs = [e_i386.REG_EAX, e_i386.REG_ECX, e_i386.REG_EDX ] # NOTE: Not in call order (sort order..)

class AnalysisMonitor(viv_imp.EmulationMonitor):

    def __init__(self, vw, funcva):
        viv_imp.EmulationMonitor.__init__(self)
        self.vw = vw
        self.funcva = funcva
        self.iscall = False
        self.framebased = False
        self.retbytes = None
        self.recursive = False
        self.maxindex = -1
        self.retvals = []
        self.starteip = 0
        self.mndist = {}
        self.sharedthis = {}

        # A dictionary to make sure we count up the ops/bytes
        self.onceop = {}  # Use this to count each once
        self.inscount = 0 # How many instructions
        self.inssize = 0  # How many instruction bytes

        self.operrefs = []

        # for stack debugging
        #self.startesp = 0

    def logAnomaly(self, eip, msg):
        self.vw.vprint("EmuAnom: 0x%.8x (f:0x%.8x) %s" % (eip, self.funcva, msg))
        viv_imp.EmulationMonitor.logAnomaly(self, eip, msg)

    def prehook(self, emu, op, starteip):

        # The other hooks use these
        self.starteip = starteip
        self.iscall = (op.opcode == opcode86.INS_CALL)
        self.mndist[op.mnem] = True

        if not self.onceop.get(starteip):
            self.onceop[starteip] = True
            self.inscount += 1
            self.inssize += len(op)

            for i,o in enumerate(op.opers):
                if o.isDeref():
                    self.operrefs.append((starteip,i,o.getOperAddr(op,emu)))

        # Do return related stuff before we execute the opcode
        if op.iflags & envi.IF_RET:
            if len(op.opers):
                self.retbytes = op.opers[0].imm

            eax = emu.getRegister(e_i386.REG_EAX)
            self.retvals.append(eax)

            # See if we managed to come out stack aligned
            #esp = emu.getStackCounter()
            #if esp != viv_imp.stack_pointer: # We got mis-aligned...
                #msg = "Return Misaligned: orig: 0x%.8x now: 0x%.8x (%d)" % (viv_imp.stack_pointer, esp, (esp-viv_imp.stack_pointer))
                #self.logAnomaly(self.starteip, msg)

    def posthook(self, emu, op, endeip):

        # Under the intel specific assumption that only one operand may
        # be a memory access, check if the last thing in the readlog
        # is from our startva, and if it accesses an arg.

        # Check the readlog for stack accesses

        readlog = vg_path.getNodeProp(emu.curpath, 'readlog')
        if len(readlog):
            readeip,readva,rsize = readlog[-1]
            if readeip == self.starteip:
                if emu.isStackArg(readva):
                    i = emu.getStackIndex(readva)
                    if i > self.maxindex:
                        self.maxindex = i

                    # Check the operands for ebp based access
                    if not self.framebased:
                        for o in op.opers:
                            if isinstance(o, e_i386.i386RegMemOper):
                                if o.reg == e_i386.REG_EBP:
                                    self.framebased = True

        eipmagic = emu.getMagic(endeip)

        # Holy crap, we have a magic EIP...
        if eipmagic != None:

            # Either way, if EIP == import entry, make sure there's a REF_CODE
            if isinstance(eipmagic, ImportEntry):

                # If it's an import entry, lets make sure we have a DCODE reference.

                # Check if we found a dynamically called import...
                oper0 = op.opers[0]
                if not isinstance(oper0, e_i386.i386ImmMemOper):
                    flags = envi.BR_DEREF
                    if self.iscall:
                        flags |= envi.BR_PROC
                    self.vw.addXref(self.starteip, eipmagic.iva, vivisect.REF_CODE, flags)

            elif isinstance(eipmagic, StackArg):
                if self.iscall:
                    self.vw.setFunctionArg(self.funcva, eipmagic.index, FUNCPTR)

        if self.iscall:

            # Detect recursive functions
            if endeip == self.funcva:
                self.recursive = True

            # If the call target is *not* a function, *is* executable,
            # and is not call 0... make a function.
            if (not self.vw.isFunction(endeip) and
                self.vw.isExecutable(endeip) and
                endeip != (op.va + len(op))):

                try:

                    self.vw.vprint('0x%.8x: Emulation Found 0x%.8x (from func: 0x%.8x) via %s' % (self.starteip, endeip, self.funcva, repr(op)))
                    self.vw.makeFunction(endeip)
                    flags = envi.BR_PROC
                    if op.opers[0].isDeref():
                        flags |= envi.BR_DEREF
                    self.vw.addXref(self.starteip, endeip, vivisect.REF_CODE, flags)

                except Exception, e:
                    if self.vw.verbose: self.vw.vprint("%s: %s" % (e.__class__.__name__, e))

        # FIXME make this use the proper path stuff!
        #vahit = vg_path.getNodeProp(emu.curpath, 'vahit')
        #if vahit.get(endeip):
            #if self.vw.getName(endeip) == None:
                #self.vw.makeName(endeip, "loop_%.8x" % endeip)

    def impcall(self, emu, impfunc):

        try:
            # If we managed to find an import func or wrapper, use it's
            # information to populate our own.
            # Set a comment showing the arguments
            if self.vw.getComment(self.starteip) == None:
                rargs = ",".join(impfunc.getReprArgs(emu))
                self.vw.setComment(self.starteip, "%s(%s)" % (impfunc.getName(), rargs))

            # Call or thunk, either way we ended up executing the function code.
            # See if the impfunc knows anything new about our workspace...

            # FIXME this should maybe go in the core workspace emulator and be done by default
            impfunc.processCaller(emu, self.vw, self.funcva)

            # We only wanna bother tracking this if it's a wrapper
            # function because all else is irrelevant
            if isinstance(impfunc, viv_imp_emufunc.WrapperFunc):
                a = impfunc.getArgs(emu)
                if len(a):
                    argva = a[0]
                    m = emu.getMagic(argva)
                    if isinstance(m, ObjectRef):
                        d = argva - m.va
                        self.sharedthis[impfunc.funcva] = d

                    if isinstance(m, UninitReg):
                        emu.logUninitRegUse(m.regindex)

        except Exception, e:
            import traceback
            traceback.print_exc()

def analyzeFunction(vw, funcva):

    # This is still very hackish...
    emu = vw.getEmulator(logread=True)

    callconv = 'unknown'

    emumon = AnalysisMonitor(vw, funcva)

    emu.setEmulationMonitor(emumon)
    emu.runFunction(funcva, maxhit=1)

    # FIXME make sure eax gets set even on unresolved calls.
    # FIXME do code-block update
    # FIXME do loop analysis via code paths (and set color maps)

    vw.setFunctionMeta(funcva, "EmuReturns", emumon.retvals)
    retrepr = []
    for r in emumon.retvals:
        m = emu.getMagic(r)
        if m != None:
            retrepr.append(repr(m))
        else:
            retrepr.append("0x%.8x" % r)

    vw.setFunctionMeta(funcva, "ReturnRepr", repr(retrepr))

    # More than 40 args?  no way...
    if emumon.maxindex > 40:
        emumon.logAnomaly(funcva, 'Crazy Arg Index Touched: %d' % emumon.maxindex)
    argc = min(emumon.maxindex+1, 40)
    callconv = "cdecl" # Default to cdecl

    # see if we have stdcall return bytes
    if emumon.retbytes != None:
        vw.setFunctionMeta(funcva, "RetBytes", emumon.retbytes)
        callconv = "stdcall"
        argc = emumon.retbytes / 4 # FIXME 64bit

    # Get the currently setup function args.
    fargs = vw.getFunctionArgs(funcva)
    idelta = 0 # arg index of first *stack* arg

    # Log registers we used by didn't init
    undefkeys = emu.uninit_use.keys()
    undefkeys.sort()

    undeflen = len(undefkeys)
    if undeflen:

        if undefkeys == thiscall_regs:
            callconv = 'thiscall'
            argc += 1
            idelta += 1
            fargs = [ (ObjectRef, 'obj'), ] + fargs

            vw.setFunctionMeta(funcva, "SharedThis", emumon.sharedthis)

        elif undefkeys == msfastcall_regs:
            callconv = 'msfastcall'
            argc += 2
            idelta += 2
            fargs = [ (Unknown, 'ecx'), (Unknown,'edx') ] + fargs

        elif undefkeys == bfastcall1_regs:
            callconv = 'bfastcall'
            argc += 1
            idelta += 1
            fargs = [ (Unknown, 'eax'), ] + fargs

        elif undefkeys == bfastcall2_regs:
            callconv = 'bfastcall'
            argc += 2
            idelta += 2
            fargs = [ (Unknown, 'eax'), (Unknown,'edx') ] + fargs

        elif undefkeys == bfastcall3_regs:
            callconv = 'bfastcall'
            argc += 3
            idelta += 3
            fargs = [ (Unknown, 'eax'), (Unknown,'edx'), (Unknown, 'ecx') ] + fargs

        else:
            pass
            #print 'DUNNO! 0x%.8x ' % funcva,undefkeys

        vw.setFunctionMeta(funcva, "UndefRegUse", undefkeys)

    # If we are short, grow...
    u = Unknown()
    while len(fargs) < argc:
        fargs.append((Unknown, u.getDefName()))

    if len(fargs) > argc:
        fargs = fargs[:argc]

    vw.setFunctionArgs(funcva, fargs)

    # Go through the evaluated dereference operands and add operand refs
    delta_done = {}
    begin = emu.stack_pointer + 4
    for va,idx,val in emumon.operrefs:
        if emu.isStackPointer(val):
            if val >= emu.stack_pointer:
                argidx = (val - begin) / 4
                # FIXME this logic should be part of the calling
                # convention somehow
                vw.addFref(funcva, va, idx, argidx+idelta)
            else:
                delta = val - emu.stack_pointer
                if not delta_done.get(delta):
                    vw.setFunctionLocal(funcva, delta, None, 'local')
                    delta_done[delta] = True

                vw.addFref(funcva, va, idx, delta)

    # Now that we're as sure as we can be...
    vw.setFunctionMeta(funcva, "argc", argc)
    vw.setFunctionMeta(funcva, "CallingConvention", callconv)
    # FIXME these should become part of generic codeblock analysis
    vw.setFunctionMeta(funcva, "InstCount", emumon.inscount)
    vw.setFunctionMeta(funcva, "Size", emumon.inssize)
    vw.setFunctionMeta(funcva, "MnemDist", len(emumon.mndist))

    if emumon.recursive: vw.setFunctionMeta(funcva, "Recursive", True)
    if emumon.framebased: vw.setFunctionMeta(funcva, "FrameBased", True)

    # Log our anomalies
    for row in emumon.getAnomalies():
        vw.setVaSetRow("Emulation Anomalies", row)

