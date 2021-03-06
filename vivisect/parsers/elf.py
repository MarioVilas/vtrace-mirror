
import struct

import Elf
import vivisect
import vivisect.parsers as v_parsers

from vivisect.const import *

from cStringIO import StringIO

config = """

[elf]

"""

def parseFile(vw, filename):
    fd = file(filename, 'rb')
    elf = Elf.Elf(fd)
    return loadElfIntoWorkspace(vw, elf, filename=filename)

def parseBytes(vw, bytes):
    fd = StringIO(bytes)
    elf = Elf.Elf(fd)
    return loadElfIntoWorkspace(vw, elf)

def parseMemory(vw, memobj, baseaddr):
    raise Exception('FIXME implement parseMemory for elf!')

def makeStringTable(vw, va, maxva):

    while va < maxva:
        if vw.readMemory(va, 1) == "\x00":
            va += 1
            continue
        else:
            try:
                l = vw.makeString(va)
                va += l[vivisect.L_SIZE]
            except Exception, e:
                print "makeStringTable",e
                return

def makeSymbolTable(vw, va, maxva):
    ret = []
    while va < maxva:
        s = vw.makeStructure(va, "elf.Elf32Symbol")
        ret.append(s)
        va += len(s)
    return ret

def makeDynamicTable(vw, va, maxva):
    ret = []
    while va < maxva:
        s = vw.makeStructure(va, "elf.Elf32Dynamic")
        ret.append(s)
        dtag = s.d_tag
        dtype = Elf.dt_types.get(dtag, "Unknown Dynamic Type")
        vw.setComment(va, dtype)
        va += len(s)
        if dtag == Elf.DT_NULL:
            break
    return ret

def makeRelocTable(vw, va, maxva, addbase, baseaddr):
    while va < maxva:
        s = vw.makeStructure(va, "elf.Elf32Reloc")
        tname = Elf.r_types_386.get(Elf.getRelocType(s.r_info), "Unknown Type")
        vw.setComment(va, tname)
        va += len(s)

arch_names = {
    Elf.EM_ARM:'arm',
    Elf.EM_386:'i386',
    Elf.EM_X86_64:'amd64',
}

def loadElfIntoWorkspace(vw, elf, filename=None):

    arch = arch_names.get(elf.e_machine)
    if arch == None:
       raise Exception("Unsupported Architecture: %d\n", elf.e_machine)

    # setup needed platform/format
    vw.setMeta('Architecture', arch)
    vw.setMeta('Platform', 'unknown')
    vw.setMeta('Format', 'elf')

    # FIXME try to determine *which* Elf system...
    #vw.setMeta("ImportEmulation", "vivisect.impemu.posix")
    vw.setMeta("DefaultCall", "cdecl")
    vw.addNoReturnApi("*.exit")

    # Base addr is earliest section address rounded to pagesize
    # NOTE: This is only for prelink'd so's and exe's.  Make something for old style so.
    addbase = False
    if not elf.isPreLinked() and elf.isSharedObject():
        addbase = True
    baseaddr = elf.getBaseAddress()

    #FIXME make filename come from dynamic's if present for shared object
    if filename == None:
        filename = "elf_%.8x" % baseaddr

    fname = vw.addFile(filename, baseaddr, v_parsers.md5File(filename))

    strtabs = {}
    secnames = []
    for sec in elf.getSections():
        secnames.append(sec.getName())

    for pgm in elf.getPheaders():
        if pgm.p_type == Elf.PT_LOAD:
            if vw.verbose: vw.vprint('Loading: %s' % (repr(pgm)))
            bytes = elf.readAtOffset(pgm.p_offset, pgm.p_filesz)
            bytes += "\x00" * (pgm.p_memsz - pgm.p_filesz)
            pva = pgm.p_vaddr
            if addbase: pva += baseaddr
            vw.addMemoryMap(pva, pgm.p_flags & 0x7, fname, bytes) #FIXME perms
        else:
            if vw.verbose: vw.vprint('Skipping: %s' % repr(pgm))

    # First add all section definitions so we have them
    for sec in elf.getSections():
        sname = sec.getName()
        size = sec.sh_size
        if sec.sh_addr == 0:
            continue # Skip non-memory mapped sections

        sva = sec.sh_addr
        if addbase: sva += baseaddr

        vw.addSegment(sva, size, sname, fname)

    # Now trigger section specific analysis
    for sec in elf.getSections():
        #FIXME dup code here...
        sname = sec.getName()
        size = sec.sh_size
        if sec.sh_addr == 0:
            continue # Skip non-memory mapped sections

        sva = sec.sh_addr
        if addbase: sva += baseaddr

        if sname == ".interp":
            vw.makeString(sva)

        elif sname == ".init":
            vw.makeName(sva, "init_function", filelocal=True)
            vw.addEntryPoint(sva)

        elif sname == ".fini":
            vw.makeName(sva, "fini_function", filelocal=True)
            vw.addEntryPoint(sva)

        elif sname == ".dynamic": # Imports
            makeDynamicTable(vw, sva, sva+size)

        # FIXME section names are optional, use dynamic info from .dynamic
        elif sname == ".dynstr": # String table for dynamics
            makeStringTable(vw, sva, sva+size)

        elif sname == ".dynsym":
            #print "LINK",sec.sh_link
            for s in makeSymbolTable(vw, sva, sva+size):
                pass
                #print "########################.dynsym",s

        # If the section is really a string table, do it
        if sec.sh_type == Elf.SHT_STRTAB:
            makeStringTable(vw, sva, sva+size)

        elif sec.sh_type == Elf.SHT_SYMTAB:
            # FIXME 32 bit specific!
            #print "FOUND A SYMBOL TABLE!"
            makeSymbolTable(vw, sva, sva+size)

        elif sec.sh_type == Elf.SHT_REL:
            makeRelocTable(vw, sva, sva+size, addbase, baseaddr)

        if sec.sh_flags & Elf.SHF_STRINGS:
            print "FIXME HANDLE SHF STRINGS"

    # Let pyelf do all the stupid string parsing...
    for r in elf.getRelocs():
        rtype = Elf.getRelocType(r.r_info)
        rlva = r.r_offset
        if addbase: rlva += baseaddr
        try:
            # If it has a name, it's an externally
            # resolved "import" entry, otherwise, just a regular reloc
            name = r.getName()
            if name:
                if rtype == Elf.R_386_JMP_SLOT:
                    vw.makeImport(rlva, "*", name)

                # FIXME elf has conflicting names for 2 relocs?
                #elif rtype == Elf.R_386_GLOB_DAT:
                    #vw.makeImport(rlva, "*", name)

                elif rtype == Elf.R_386_32:
                    pass

                else:
                    print "OMG, UNKNOWN RELOC",hex(rlva),rtype,name

        except vivisect.InvalidLocation, e:
            print "NOTE",e

    for s in elf.getDynSyms():
        stype = s.getInfoType()
        sva = s.st_value
        if sva == 0:
            continue
        if addbase: sva += baseaddr
        if sva == 0:
            continue

        if stype == Elf.STT_FUNC:
            try:
                vw.addExport(sva, EXP_FUNCTION, s.name, fname)
                vw.addEntryPoint(sva)
            except Exception, e:
                vw.vprint('addExport Failure: %s' % e)

        elif stype == Elf.STT_OBJECT:
            if vw.isValidPointer(sva):
                try:
                    vw.addExport(sva, EXP_DATA, s.name, fname)
                except Exception, e:
                    vw.vprint('WARNING: %s' % e)

        elif stype == Elf.STT_HIOS:
            # So aparently Elf64 binaries on amd64 use HIOS and then
            # s.st_other cause that's what all the kewl kids are doing...
            sva = s.st_other
            if addbase: sva += baseaddr
            if vw.isValidPointer(sva):
                try:
                    vw.addExport(sva, EXP_FUNCTION, s.name, fname)
                    vw.addEntryPoint(sva)
                except Exception, e:
                    vw.vprint('WARNING: %s' % e)

        elif stype == 14:# OMG WTF FUCK ALL THIS NONSENSE! FIXME
            # So aparently Elf64 binaries on amd64 use HIOS and then
            # s.st_other cause that's what all the kewl kids are doing...
            sva = s.st_other
            if addbase: sva += baseaddr
            if vw.isValidPointer(sva):
                try:
                    vw.addExport(sva, EXP_DATA, s.name, fname)
                except Exception, e:
                    vw.vprint('WARNING: %s' % e)

        else:
            pass
            #print "DYNSYM DYNSYM",repr(s),s.getInfoType(),'other',hex(s.st_other)

    for d in elf.getDynamics():
        if d.d_tag == Elf.DT_NEEDED:
            name = d.getName()
            name = name.split('.')[0].lower()
            vw.addLibraryDependancy(name)
        else:
            pass
            #print "DYNAMIC DYNAMIC DYNAMIC",d


    for s in elf.getSymbols():
        sva = s.st_value
        if addbase: sva += baseaddr
        if vw.isValidPointer(sva) and len(s.name):
            try:
                vw.makeName(sva, s.name, filelocal=True)
            except Exception, e:
                print "WARNING:",e

    if vw.isValidPointer(elf.e_entry):
        vw.makeName(elf.e_entry, "main_entry", filelocal=True)
        vw.addEntryPoint(elf.e_entry)
        
    if vw.isValidPointer(baseaddr):
        vw.makeStructure(baseaddr, "elf.Elf32")

    return fname
