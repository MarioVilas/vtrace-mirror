import envi
import vivisect
import vstruct.defs.ihex as v_ihex
import vivisect.parsers as v_parsers

from vivisect.const import *

def parseFile(vw, filename):

    #baseaddr = vw.getOptionInt("blob","baseaddr")
    #if baseaddr == None:
        #raise Exception('Blob loader *requires* base address (-O blob:baseaddr:<address>)')

    arch = vw.getOption('ihex','arch')
    if arch == None:
        raise Exception("IHex loader *requires* arch option (-O ihex:arch:<archname>)")

    envi.getArchModule(arch)

    vw.setMeta('Architecture', arch)
    vw.setMeta('Platform','Unknown')
    vw.setMeta('Format','ihex')

    fname = vw.addFile(filename, 0, v_parsers.md5File(filename))

    ihex = v_ihex.IHexFile()
    ihex.vsParse( file(filename, 'rb').read() )

    for addr, perms, notused, bytes in ihex.getMemoryMaps():
        vw.addMemoryMap( addr, perms, fname, bytes )
        vw.addSegment( addr, len(bytes), '%.8x' % addr, fname )

def parseMemory(vw, memobj, baseaddr):
    raise Exception('ihex loader cannot parse memory!')
