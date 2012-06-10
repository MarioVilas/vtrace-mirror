
import sys
import traceback

import vstruct
import impmagic

class EmuFunc:

    __callconv__ = "unknown"
    __argc__ = None
    __argt__ = []
    __argn__ = []
    __noreturn__ = False
    __argmeta__ = {} # If any per-arg meta data is needed (vstruct..)

#FIXME rtype!

    def __init__(self):
        self.callconv = self.__class__.__callconv__

        self.impname = None

        self.argt = self.__class__.__argt__
        self.argn = self.__class__.__argn__
        self.argc = len(self.argn)
        self.argmeta = self.__class__.__argmeta__

    def isNoReturn(self):
        """
        Will return true if this is a function which does not return.
        (libc.exit(0) etc..  compilers *may* not continue to make code.
        """
        return self.__class__.__noreturn__

    def setReturn(self, emu, retval):
        emu.setReturnValue(retval, self.callconv, self.argc)

    def getArgs(self, emu):
        """
        Return the parsed numerical values for the arguments to this
        function based on the specified emulator state.
        """
        return emu.getCallArgs(self.argc, self.callconv)

    def getArgObjects(self):
        """
        Return instances of the argument types (accounting for
        arg meta as needed).
        """
        ret =  []
        for i,t in enumerate(self.argt):
            args = self.argmeta.get(i, ())
            ret.append(t(*args))
        return ret

    def getReprArgs(self, emu):
        ret = []
        for a in self.getArgs(emu):
            m = emu.getMagic(a)
            if m != None:
                offstr = ""
                off = a - m.va
                if off > 0:
                    offstr = "+ %d" % off
                elif off < 0:
                    offstr = "- %d" % abs(off)
                ret.append(repr(m)+offstr)
                continue

            l = emu.getLocalOffset(a)
            if l != None:
                ret.append('local_%d' % l)
                continue

            ret.append("0x%.8x" % a)

        return ret

    def processCaller(self, emu, vw, funcva):
        """
        Update the workspace and function information to account
        for being called by the given function with the specified
        emulator state.
        """
        argobjs = self.getArgObjects()
        args = self.getArgs(emu)
        for i,a in enumerate(self.getArgs(emu)):
            try:
                # Check for an arg being an impmagic object
                m = emu.getMagic(a)
                if m != None:

                    # We have a magic arg! check if it's neato...
                    if isinstance(m, impmagic.StackArg):
                        # He handed us one of *his* args...  update his type with ours.
                        vw.setFunctionArg(funcva, m.index, self.argt[i], self.argn[i])

                    elif isinstance(m, impmagic.UninitReg):
                        # If we got an uninitialized register, note it.
                        emu.logUninitRegUse(m.regindex)

                elif vw.isValidPointer(a):
                    # If we got a valid workspace pointer, try to update the
                    # workspace based our type information.
                    try:
                        argobjs[i].addToWorkspace(vw, a)
                    except Exception, e:
                        print "ERROR: addToWorkspace() for %s: %s" % (argobjs[i].__class__.__name__, e)

                elif emu.isStackLocal(a):
                    # They handed us a pointer to their stack.  If we're a wrapper
                    # update the guy we wrap to take a pointer, and
                    # FIXME update locals references in our caller.
                    if isinstance(self, WrapperFunc):
                        vw.setFunctionArg(self.funcva, i, impmagic.Pointer)

            except Exception, e:
                traceback.print_exc()
                vw.vprint("ERROR: %s.processCaller():0x%.8x:%s" % (self.getName(), funcva, e))

    def __call__(self, emu):
        """
        NOTE: Over-ride this method to implement an emulator for an API call!
        """
        retval = impmagic.ReturnValue(0,self.getName())
        ret = emu.setMagic(retval)
        self.setReturn(emu, ret)

    def getName(self):
        if self.impname == None:
            # NOTE: For now, all impemu modules may only be 1 deep...
            modname = self.__class__.__module__.split(".")[-1]
            self.impname = "%s.%s" % (modname, self.__class__.__name__)
        return self.impname

class WrapperFunc(EmuFunc):

    def __init__(self, vw, funcva):
        EmuFunc.__init__(self)
        self.funcva = funcva
        self.impname = vw.getName(funcva)
        self.callconv = vw.getFunctionMeta(funcva, "CallingConvention")
        fargs = vw.getFunctionArgs(funcva)
        self.argt = [x for x,y in fargs]
        self.argn = [y for x,y in fargs]
        self.argc = len(fargs)

    def __call__(self, emu):
        retval = impmagic.ReturnValue(self.funcva, self.getName())
        val = emu.setMagic(retval)
        self.setReturn(emu, val)

    def __repr__(self):
        return '%s(%s)' % (self.impname, ','.join(self.argn))

class DefaultCallFunc(EmuFunc):

    """
    Calls to totally un-resolved locations will resolve down
    to one of these *if* the DefaultCall meta key is set
    in the workspace.
    """
    def __init__(self, callconv, bestname=None):
        self.argt = []
        self.argn = []
        self.argc = 0
        self.callconv = callconv
        self.impname = bestname

    def __call__(self, emu):
        retval = impmagic.ReturnValue(0, self.getName())
        val = emu.setMagic(retval)
        self.setReturn(emu, val)

