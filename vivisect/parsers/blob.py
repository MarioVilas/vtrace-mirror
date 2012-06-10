import envi
import vivisect
import vivisect.parsers as v_parsers
from vivisect.const import *

def parseFile(vw, filename):

    baseaddr = vw.getOptionInt("blob","baseaddr")
    if baseaddr == None:
        raise Exception('Blob loader *requires* base address (-O blob:baseaddr:<address>)')

    arch = vw.getOption('blob','arch')
    if arch == None:
        raise Exception("Blob loader *requires* arch option (-O blob:arch:<archname>)")

    envi.getArchModule(arch)

    vw.setMeta('Architecture', arch)
    vw.setMeta('Platform','Unknown')
    vw.setMeta('Format','blob')

    fname = vw.addFile(filename, baseaddr, v_parsers.md5File(filename))
    vw.addMemoryMap(baseaddr, 7, filename, file(filename, "rb").read())

def parseMemory(vw, memobj, baseaddr):
    va,size,perms,fname = memobj.getMemoryMap(baseaddr)
    if not fname:
        fname = 'map_%.8x' % baseaddr
    bytes = memobj.readMemory(va, size)
    fname = vw.addFile(fname, baseaddr, v_parsers.md5Bytes(bytes))
    vw.addMemoryMap(va, perms, fname, bytes)

