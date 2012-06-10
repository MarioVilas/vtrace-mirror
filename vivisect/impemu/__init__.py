
"""
This is a subsystem in vivisect devoted to pretending
to be known APIs to get more out of emulation.
"""
import copy
import struct
import traceback



import envi
import emufunc
import visgraph.pathcore as vg_path
import envi.bits as e_bits
import envi.memory as e_mem
import envi.archs.i386 as e_i386

from impmagic import *
from vivisect.const import *

# A global calling convention default
cc_default = None

# Used by the import call emulation hooks
imp_hooks = {}

# Pre-initialize a stack memory bytes
init_stack_map = ''
for i in xrange(8192/4):
    init_stack_map += struct.pack("<I", 0xfefe0000+(i*4))

class EmulationMonitor:
    """
    Emulation monitors may be passed into functions like
    runFunction() to track and hook the emulator.
    """
    def __init__(self):
        # FIXME make this a dict and re-plumb for VaSet
        self.emuanom = [] # A list of emulation anomalies (in va,msg tuples)
        self.retvals = [] # A list of the return values seen

    def logAnomaly(self, va, msg):
        self.emuanom.append((va,msg))

    def getAnomalies(self):
        return list(self.emuanom)

    def prehook(self, emu, op, starteip):
        """
        This monitor hook gets called back prior to the execution of
        each instruction in the emulator.
        """
        pass

    def posthook(self, emu, op, endeip):
        """
        This monitor hook gets called back following the execution of
        each instruction in the emulator. During this callback, the
        emulator's curpath variable remains on the previous instruction.
        """
        pass

    def impcall(self, emu, impfunc):
        """
        This monitor hook gets called when the workspace emulator has
        resolved an import emulation function that is called by the
        current instruction. It will be called back *prior* to the
        emufunc getting run.
        """
        pass

class WorkspaceEmulator:

    def __init__(self, vw, logwrite=False, logread=False):

        self.vw = vw
        # Save off the next parent class so we can call it from overrides
        self.funcva = None # Set if using runFunction
        self.mbase = 0x41560000 #FIXME hack
        self.magic = {}
        self.uninit_use = {}
        self.logwrite = logwrite
        self.logread = logread
        self.path = self.newCodePathNode()
        self.curpath = self.path
        self.opcache = {}
        self.emumon = None
        self.stackargs = {}     # Store off StackArg magics by offset
        self.psize = self.getPointerSize()
        self.stack_map_mask = e_bits.sign_extend(0xffffe000, 4, vw.psize)
        self.stack_map_base = e_bits.sign_extend(0xbfbf0000, 4, vw.psize)
        self.stack_pointer = self.stack_map_base + 4096

        # Possibly need an "options" API?
        self._safe_mem = True   # Should we be forgiving about memory accesses?
        self._func_only = True  # is this emulator meant to stay in one function scope?

        # Map in a memory map for the stack
        self.addMemoryMap(self.stack_map_base, 6, "[stack]", init_stack_map)

        # Map in all the memory associated with the workspace
        for va, size, perms, fname in vw.getMemoryMaps():
            offset, bytes = vw.getByteDef(va)
            self.addMemoryMap(va, perms, fname, bytes)

        self.setStackCounter(self.stack_pointer)

    def getPathProp(self, key):
        '''
        Retrieve a named value from the current code path context.
        '''
        return vg_path.getNodeProp(self.curpath, key)

    def setPathProp(self, key, value):
        """
        Set a named value which is only relevant for the current code path.
        """
        return vg_path.setNodeProp(self.curpath, key, value)

    def setEmulationMonitor(self, emumon):
        """
        Snap in an emulation monitor. (see EmulationMonitor doc from vivisect.impemu)
        """
        self.emumon = emumon

    def parseOpcode(self, pc):
        # We can make an opcode *faster* with the workspace because of
        # getByteDef etc... use it.
        op = self.opcache.get(pc)
        if op == None:
            op = envi.Emulator.parseOpcode(self, pc)
            self.opcache[pc] = op
        return op

    def checkCall(self, starteip, endeip, op):
        """
        Check if this was a call, and if so, do the required
        import emulation and such...
        """
        iscall = bool(op.iflags & envi.IF_CALL)
        if iscall:

            impfunc = self.getEmuFunc(endeip)

            # If we found an emulation function, and we speak it's calling
            # convention, let it modify the emulator state.
            if impfunc and self.hasCallingConvention(impfunc.callconv):
                if self.emumon != None:
                    try:
                        self.emumon.impcall(self, impfunc)
                    except Exception, e:
                        self.emumon.logAnomaly(endeip, "%s.impcall failed: %s" % (self.emumon.__class__.__name__, e))

                impfunc(self)

            # Either way, if it's a call PC goes to next instruction
            if self._func_only:
                self.setProgramCounter(starteip+len(op))

        return iscall

    def newCodePathNode(self, parent=None, bva=None):
        '''
        NOTE: Right now, this is only called from the actual branch state which
        needs it.  it must stay that way for now (register context is being copied
        for symbolic emulator...)
        '''
        props = {
            'bva':bva,    # the entry virtual address for this branch
            'valist':[],  # the virtual addresses in this node in order
            'calllog':[], # FIXME is this even used?
            'readlog':[], # a log of all memory reads from this block
            'writelog':[],# a log of all memory writes from this block
        }
        ret = vg_path.newPathNode(parent=parent, **props)
        return ret

    def getBranchNode(self, node, bva):
        '''
        If a node exists already for the specified branch, return it. Otherwise,
        create a new one and return that...
        '''
        for knode in vg_path.getNodeKids(node):
            if vg_path.getNodeProp(knode, 'bva') == bva:
                return knode
        return self.newCodePathNode(node, bva)

    def checkBranches(self, starteip, endeip, op):
        """
        This routine gets the current branch list for this opcode, adds branch
        entries to the current path, and updates current path as needed
        (returns a list of (va, CodePath) tuples.
        """

        ret = []
        # Add all the known branches to the list
        blist = op.getBranches(emu=self)

        # FIXME this should actually check for conditional...
        # If there is more than one branch target, we need a new code block
        if len(blist) > 1:
            for bva,bflags in blist:
                if bva == None:
                    print "Unresolved branch even WITH an emulator?"
                    continue

                bpath = self.getBranchNode(self.curpath, bva)
                ret.append((bva, bpath))

        return ret

    def stepi(self):
        # NOTE: when we step, we *always* want to be stepping over calls
        # (and possibly import emulate them)
        starteip = self.getProgramCounter()

        # parse out an opcode
        op = self.parseOpcode(starteip)
        if self.emumon:
            self.emumon.prehook(self, op, starteip)

        # Execute the opcode
        self.executeOpcode(op)
        vg_path.getNodeProp(self.curpath, 'valist').append(starteip)

        endeip = self.getProgramCounter()

        if self.emumon:
            self.emumon.posthook(self, op, endeip)

        if not self.checkCall(starteip, endeip, op):
            self.checkBranches(starteip, endeip, op)

    def runFunction(self, funcva, stopva=None, maxhit=None, maxloop=None):
        """
        This is a utility function specific to WorkspaceEmulation (and impemu) that
        will emulate, but only inside the given function.  You may specify a stopva
        to return once that location is hit.
        """

        self.funcva = funcva

        # Let the current (should be base also) path know where we are starting
        vg_path.setNodeProp(self.curpath, 'bva', funcva)

        hits = {}
        todo = [(funcva,self.getEmuSnap(),self.path),]
        vw = self.vw # Save a dereference many many times

        while len(todo):

            va,esnap,self.curpath = todo.pop()

            self.setEmuSnap(esnap)

            self.setProgramCounter(va)

            # Check if we are beyond our loop max...
            if maxloop != None:
                lcount = vg_path.getPathLoopCount(self.curpath, 'bva', va)
                if lcount > maxloop:
                    continue

            while True:

                starteip = self.getProgramCounter()

                if not vw.isValidPointer(starteip):
                    break

                if starteip == stopva:
                    return

                # Check straight hit count...
                if maxhit != None:
                    h = hits.get(starteip, 0)
                    h += 1
                    if h > maxhit:
                        break
                    hits[starteip] = h

                # If we ran out of path (branches that went
                # somewhere that we couldn't follow?
                if self.curpath == None:
                    break

                try:

                    # FIXME unify with stepi code...
                    op = self.parseOpcode(starteip)
                    if self.emumon:
                        self.emumon.prehook(self, op, starteip)

                    # Execute the opcode
                    self.executeOpcode(op)
                    vg_path.getNodeProp(self.curpath, 'valist').append(starteip)

                    endeip = self.getProgramCounter()

                    if self.emumon:
                        self.emumon.posthook(self, op, endeip)

                    iscall = self.checkCall(starteip, endeip, op)

                    # If it wasn't a call, check for branches, if so, add them to
                    # the todo list and go around again...
                    if not iscall:
                        blist = self.checkBranches(starteip, endeip, op)
                        if len(blist):
                            # pc in the snap will be wrong, but over-ridden at restore
                            esnap = self.getEmuSnap()
                            for bva,bpath in blist:
                                todo.append((bva, esnap, bpath))
                            break

                    # If we enounter a procedure exit, it doesn't
                    # matter what EIP is, we're done here.
                    if op.iflags & envi.IF_RET:
                        vg_path.setNodeProp(self.curpath, 'cleanret', True)
                        break

                except Exception, e:
                    #traceback.print_exc()
                    if self.emumon != None:
                        self.emumon.logAnomaly(starteip, str(e))

                    break # If we exc during execution, this branch is dead.

    def getEmuFunc(self, va):
        """
        Get and return an emulation funcion if one is present and should be called
        at the specified va.
        """
        vw = self.vw

        # Check the workspace...
        if self._func_only and vw.isFunction(va):
            return vw.getEmuFunc(va)

        # Perhaps it is known by magic?
        eipmagic = self.getMagic(va)
        impfunc = None
        if eipmagic: # OMG magic eip!!!

            defcall = vw.getMeta("DefaultCall")

            if isinstance(eipmagic, ImportEntry):

                impfunc = vw.getImpEmuFunc(eipmagic.name)

            elif isinstance(eipmagic, FUNCPTR):

                impfunc = vw.getImpEmuFunc("%s.%s" % (eipmagic.libname,eipmagic.funcname))

                #if impfunc == None:
                    #if vw.getComment(starteip) == None:
                        #vw.setComment(starteip, repr(eipmagic))
                    #retmagic = ReturnValue(0, "%s.%s" % (eipmagic.libname, eipmagic.funcname))

            elif defcall != None:
                # If we at least have a default calling convention...
                impfunc = emufunc.DefaultCallFunc(defcall, bestname=repr(eipmagic))

            #FIXME deal with values that we do know how to execute, but failed to resolve
            #FIXME deal with magic vals in eip that we don't know how to execute...
            return impfunc

        defcall = vw.getMeta("DefaultCall")
        if self._func_only and defcall != None:
            return emufunc.DefaultCallFunc(defcall, bestname="%.8x_DefaultCall" % va)

        return None

    def setMagic(self, magic):
        """
        Set a "magic" object and give it an "address" that can be
        used to look it back up from the emulator later.
        """
        ret = self.mbase
        self.magic[ret] = magic
        self.mbase += 8192 #FIXME hard coded
        ret += 4096 # Make the magic va an offset in the page...
        magic.setMagicVa(ret)
        return ret

    def getMagic(self, tag):
        '''
        Return the magic object for the given tag address.
        '''
        # FIXME 64 bit masking...
        return self.magic.get(tag&0xffffe000, None)

    def writeMemory(self, va, bytes):
        """
        Try to write the bytes to the memory object, otherwise, dont'
        complain...
        """
        if self.logwrite:
            wlog = vg_path.getNodeProp(self.curpath, 'writelog')
            wlog.append((self.getProgramCounter(),va,bytes))

        m1 = None
        m = self.getMagic(va)
        if len(bytes) == 4: #FIXME platform word
            val = struct.unpack("<I", bytes)[0]
            m1 = self.getMagic(val)

        # At this point, m1 is set to the magic being *stored* at va.

        if m1 != None and self.vw.isValidPointer(va):
            #FIXME maybe do something more with this?
            self.vw.setComment(va, repr(m1))

        # If we're writing to an un-initialized register, note it.
        if isinstance(m, UninitReg):
            self.logUninitRegUse(m.regindex)

        # It's totally ok to write to invalid memory during the
        # emulation pass (as long as safe_mem is true...)
        probeok = self.probeMemory(va, len(bytes), e_mem.MM_WRITE)
        if self._safe_mem and not probeok:
            return

        return e_mem.MemoryObject.writeMemory(self, va, bytes)

    def logUninitRegUse(self, regid):
        self.uninit_use[regid] = True

    def readMemory(self, va, size):

        if self.logread:
            rlog = vg_path.getNodeProp(self.curpath, 'readlog')
            rlog.append((self.getProgramCounter(),va,size))

        # If they read an import entry, start a tracker...
        l = self.vw.getLocation(va)
        if l != None:
            lva, lsize, ltype, ltinfo = l
            if ltype == LOC_IMPORT and lsize == size: # They just read an import.
                ie = ImportEntry(va, ltinfo)
                # This is a special emulator hook for import call detection
                ret = self.setMagic(ie)
                return e_bits.buildbytes(ret, lsize)

        # Lets check if they are reading from a magic
        # FIXME track this for auto struct definition!
        m = self.getMagic(va)
        if m != None:
            if isinstance(m, UninitReg):
                self.logUninitRegUse(m.regindex)

            # If we read a pointer size chunk from inside a magic,
            # lets track that too...
            if size == self.getPointerSize():
                deref = MagicDeref(m, va - m.va)
                ret = self.setMagic(deref)
                return e_bits.buildbytes(ret, self.vw.psize)

        # Read from the emulator's pages if we havent resolved it yet
        probeok = self.probeMemory(va, size, e_mem.MM_READ)
        if self._safe_mem and not probeok:
            return 'A' * size

        return e_mem.MemoryObject.readMemory(self, va, size)

    # Some APIs for telling if pointers are in runtime memory regions

    def isUninitStack(self, val):
        """
        If val is a numerical value in the same memory page
        as the un-initialized stack values return True
        """
        #NOTE: If uninit_stack_byte changes, so must this!
        if (val & 0xfffff000) == 0xfefef000:
            return True
        return False

    def isStackPointer(self, va):
        return (va & self.stack_map_mask) == self.stack_map_base

    def isStackLocal(self, va):
        """
        Return true if the given VA is within the frame memory maps and is
        below the initial stack pointer (meaning it's a local)
        """
        if (va & self.stack_map_mask) == self.stack_map_base and va < self.stack_pointer:
            return True
        return False

    def getLocalOffset(self, va):
        """
        If the specified virtual address represents a stack local, return the
        offset (absolute) from the frame.

        NOTE: For ease of use (cause exceptions are shlow) returns None if the VA
        is NOT a valid frame local.
        """
        if not self.isStackLocal(va):
            return None
        return self.stack_pointer - va

    def isStackArg(self, va):
        """
        Return true if the given VA is within the frame memory maps and is
        above the initial stack pointer (meaning it's an argument)
        """
        if (va & self.stack_map_mask) == self.stack_map_base and va > self.stack_pointer:
            return True
        return False

    def getStackIndex(self, va):
        return (va - (self.stack_pointer + self.psize))/self.psize


import envi.archs.i386 as e_i386
import envi.archs.amd64 as e_amd64

########################################################################
#
# NOTE: For each architecture we intend to do workspace emulation on,
#       extend an emulator to allow any of the needed tweaks (rep prefix
#       etc).
# NOTE: ARCH UPDATE

class i386WorkspaceEmulator(WorkspaceEmulator, e_i386.IntelEmulator):
    def __init__(self, vw, logwrite=False, logread=False):
        e_i386.IntelEmulator.__init__(self)
        WorkspaceEmulator.__init__(self, vw, logwrite=logwrite, logread=logread)

        # Setup some general purpose registers
        for i in range(8):
            if i == e_i386.REG_ESP:
                continue
            rname = self.getRegisterName(i)
            val = self.setMagic(UninitReg(rname, i))
            self.setRegister(i, val)

        # Setup some stack args we can use to track...
        seip = self.setMagic(SavedProgramCounter())
        args = [seip,]
        for i in range(16):
            val = self.setMagic(StackArg(i))
            args.append(val)

        self.writeMemory(self.stack_pointer, struct.pack("<17I", *args))

    def doRepPrefix(self, meth, op):
        # Fake out the rep prefix (cause ecx == 0x41414141 ;) )
        return meth(op)

class Amd64WorkspaceEmulator(WorkspaceEmulator, e_amd64.Amd64Emulator):
    def __init__(self, vw, logwrite=False, logread=False):
        e_amd64.Amd64Emulator.__init__(self)
        WorkspaceEmulator.__init__(self, vw, logwrite=logwrite, logread=logread)

        # Setup default register values
        for i in range(16):
            if i == e_amd64.REG_RSP:
                continue
            rname = self.getRegisterName(i)
            magic = self.setMagic(UninitReg(rname, i))
            self.setRegister(i, magic)

        # Setup default argument layout for amd64call
        self.setRegister(e_amd64.REG_RCX, self.setMagic(StackArg(0)))
        self.setRegister(e_amd64.REG_RDX, self.setMagic(StackArg(1)))
        self.setRegister(e_amd64.REG_R8,  self.setMagic(StackArg(2)))
        self.setRegister(e_amd64.REG_R9,  self.setMagic(StackArg(3)))

        # Also setup the stack args out to 16...
        seip = self.setMagic(SavedProgramCounter())
        base = [ seip, ]
        for i in xrange(16):
            if i < 4:
                base.append(0) # The fist 4 are place holders
            else:
                base.append(self.setMagic(StackArg(i)))

        self.writeMemory(self.stack_pointer, struct.pack("<17Q", *base))

    def doRepPrefix(self, meth, op):
        # Fake out the rep prefix (cause ecx == 0x41414141 ;) )
        return meth(op)

workspace_emus  = {
    "i386"  :i386WorkspaceEmulator,
    "amd64" :Amd64WorkspaceEmulator,
}
