"""
Find all undefined reference targets and attempt to determine
if they are code by emulation behaviorial analysis.

(This module works best very late in the analysis passes)
"""

# FIXME these heuristics end up being arch (and possibly plat) specific
#       and should probably be moved to analysis/i386

import vivisect
import vivisect.reports as viv_rep
import vivisect.impemu as viv_imp

import envi

vasetdef = (("va",int),)
report = "vivisect.reports.undeftargets"
verbose = False

class watcher(viv_imp.EmulationMonitor):

    def __init__(self, vw, tryva):
        self.vw = vw
        self.badop = vw.arch.makeOpcode("\x00\x00\x00\x00\x00")
        self.tryva = tryva
        self.hasret = False

    def looksgood(self):
        if not self.hasret:
            return False
        return True

    def prehook(self, emu, op, eip):

        if op.mnem == "out": #FIXME arch specific. see above idea.
            raise Exception("Out instruction...")

        if op == self.badop:
            raise Exception("Hit known BADOP at 0x%.8x %s" % (eip,repr(op)))

        if op.iflags & envi.IF_RET:
            self.hasret = True

        # Make sure we didn't run into any other
        # defined locations...
        if self.vw.isFunction(eip):
            raise Exception("Fell Through Into Function: %.8x" % eip)

        if eip != self.tryva:
            if len(self.vw.getXrefsTo(eip)):
                raise Exception("Encountered an outside xref")

        loc = self.vw.getLocation(eip)
        if loc != None:
            va, size, ltype, linfo = loc
            if ltype != vivisect.LOC_OP:
                raise Exception("HIT %d AT %.8x" % (ltype, va))

        # FIXME do we need a way to terminate emulation here?

def analyze(vw):

    flist = vw.getFunctions()

    tried = {}
    vasetrows = []
    while True:
        docode = []
        for va, name in viv_rep.runReportModule(vw, report).items():
            # Make sure it's executable
            if not vw.isExecutable(va):
                continue

            # Skip it if we've tried it already.
            if tried.get(va):
                continue

            tried[va] = True

            emu = vw.getEmulator()
            wat = watcher(vw, va)
            emu.setEmulationMonitor(wat)
            try:
                emu.runFunction(va, maxhit=1)
            except Exception, e:
                if verbose: print "NEWP %.8x" % va,repr(e)
                continue

            if wat.looksgood():
                docode.append(va)

        if len(docode) == 0:
            break

        for va in docode:
            vw.makeFunction(va)
            vasetrows.append((va,))

    vw.addVaSet("Made By Emucode", vasetdef, vasetrows)
    dlist = vw.getFunctions()

    vw.vprint("emucode: %d new functions defined (now total: %d)" % (len(dlist)-len(flist), len(dlist)))

