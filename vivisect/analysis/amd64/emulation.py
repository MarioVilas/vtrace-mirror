
import vivisect
import vivisect.impemu as viv_imp
import vivisect.impemu.emufunc as viv_imp_emufunc

from vivisect.impemu.impmagic import *

import envi
import envi.archs.amd64 as e_amd64

class Amd64EmuMon(viv_imp.EmulationMonitor):
    pass

def analyzeFunction(vw, funcva):
    emumon = Amd64EmuMon()
    emu = vw.getEmulator(logread=True)
    #emu.setEmulationMonitor(emumon)
    emu.runFunction(funcva, maxhit=1)

