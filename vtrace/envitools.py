
"""
Some tools that require the envi framework to be installed
"""

import sys
import traceback

import envi
import envi.intel as e_intel # FIXME This should NOT have to be here

class RegisterException(Exception):
    pass

def cmpRegs(emu, trace):
    for idx,name in reg_map:
        er = emu.getRegister(idx)
        tr = trace.getRegisterByName(name)
        if er != tr:
            raise RegisterException("REGISTER MISMATCH: %s 0x%.8x 0x%.8x" % (name, tr, er))
    return True

reg_map = [
    (e_intel.REG_EAX, "eax"),
    (e_intel.REG_ECX, "ecx"),
    (e_intel.REG_EDX, "edx"),
    (e_intel.REG_EBX, "ebx"),
    (e_intel.REG_ESP, "esp"),
    (e_intel.REG_EBP, "ebp"),
    (e_intel.REG_ESI, "esi"),
    (e_intel.REG_EDI, "edi"),
    (e_intel.REG_EIP, "eip"),
    (e_intel.REG_FLAGS, "eflags")
    ]

#FIXME intel specific
def setRegs(emu, trace):
    for idx,name in reg_map:
        tr = trace.getRegisterByName(name)
        emu.setRegister(idx, tr)

def emulatorFromTrace(trace):
    """
    Produce an envi emulator for this tracer object.  Use the trace's arch
    info to get the emulator so this can be done on the client side of a remote
    vtrace session.
    """
    arch = trace.getMeta("Architecture")
    amod = envi.getArchModule(arch)
    emu = amod.getEmulator()

    if trace.getMeta("Platform") == "Windows":
        emu.setSegmentInfo(e_intel.SEG_FS, trace.getThreads()[trace.getMeta("ThreadId")], 0xffffffff)

    emu.setMemoryObject(trace)
    setRegs(emu, trace)
    return emu

def lockStepEmulator(emu, trace):
    while True:
        print "Lockstep: 0x%.8x" % emu.getProgramCounter()
        try:
            pc = emu.getProgramCounter()
            op = emu.makeOpcode(pc)
            trace.stepi()
            emu.stepi()
            cmpRegs(emu, trace)
        except RegisterException, msg:
            print "Lockstep Error: %s: %s" % (repr(op),msg)
            setRegs(emu, trace)
            sys.stdin.readline()
        except Exception, msg:
            traceback.print_exc()
            print "Lockstep Error: %s" % msg
            return

import vtrace
import vtrace.platforms.base as v_base

class TraceEmulator(vtrace.Trace, v_base.BasePlatformMixin, v_base.UtilMixin):
    """
    Wrap an arbitrary emulator in a Tracer compatible API.
    """
    def __init__(self, emu):
        vtrace.Trace.__init__(self)
        self.emu = emu

        # Fake out being attached
        self.attached = True
        self.pid = 0x56

    def platformStepi(self):
        self.emu.stepi()

    def platformWait(self):
        # We only support single step events now
        return True

    def getRegisterFormat(self):
        # Fake this out for the Trace constructor
        return ""

    def getRegisterNames(self):
        # Fake this out for the Trace constructor
        return ""

    def platformProcessEvent(self, event):
        self.fireNotifiers(vtrace.NOTIFY_STEP)

    def platformReadMemory(self, va, size):
        return self.emu.readMemory(va, size)

    def platformWriteMemory(self, va, bytes):
        return self.emu.writeMemory(va, bytes)

    def platformGetMaps(self):
        return self.emu.getMemoryMaps()

    def platformGetThreads(self):
        return ((1, 0xffff0000), )

    def platformDetach(self):
        pass

    def getPcName(self):
        arch = self.emu.arch
        return arch.getRegisterName(arch.getProgramCounterIndex())

    def getSpName(self):
        arch = self.emu.arch
        return arch.getRegisterName(arch.getStackCounterIndex())

    # Over-ride register *caching* subsystem to store/retrieve
    # register information in pure dictionaries
    def cacheRegs(self, threadid):
        if self.regcache == None:
            self.regcache = {}
            for i in range(self.emu.arch.getRegisterCount()):
                name = self.emu.arch.getRegisterName(i)
                val = self.emu.getRegister(i)
                self.regcache[name] = val
        return self.regcache

    def syncRegs(self):
        if self.regcachedirty:
            for i in range(self.emu.arch.getRegisterCount()):
                name = self.emu.arch.getRegisterName(i)
                val = self.emu.setRegister(i, self.regcache.get(name))
            self.regcachedirty = False
        self.regcache = None

def main():
    import vtrace
    sym = sys.argv[1]
    pid = int(sys.argv[2])
    t = vtrace.getTrace()
    t.attach(pid)
    symaddr = t.parseExpression(sym)
    t.addBreakpoint(vtrace.Breakpoint(symaddr))
    while t.getProgramCounter() != symaddr:
        t.run()
    snap = t.takeSnapshot()
    #snap.saveToFile("woot.snap") # You may open in vdb to follow along
    emu = emulatorFromTrace(snap)
    lockStepEmulator(emu, t)

if __name__ == "__main__":
    # Copy this file out to the vtrace dir for testing and run as main
    main()

