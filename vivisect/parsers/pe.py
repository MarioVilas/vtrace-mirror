
import os
import PE
import vivisect
import vivisect.parsers as v_parsers
from vivisect.const import *

# Steal symbol parsing from vtrace
import vtrace
import vtrace.platforms.win32 as vt_win32

import envi
import envi.memory as e_mem

config = """

[pe]

"""

# PE Machine field values
#0x14d   Intel i860
#0x14c   Intel I386 (same ID used for 486 and 586)
#0x162   MIPS R3000
#0x166   MIPS R4000
#0x183   DEC Alpha AXP

def parseFile(vw, filename):
    pe = PE.PE(file(filename,"rb"))
    return loadPeIntoWorkspace(vw, pe, filename)

def parseBytes(vw, bytes):
    raise Exception("FIXME IMPLEMENT")

def parseMemory(vw, memobj, base):
    pe = PE.peFromMemoryObject(memobj, base)
    mapbase, mapsize, perms, fname = memobj.getMemoryMap(base)
    #FIXME does the PE's load address get fixedup on rebase?
    return loadPeIntoWorkspace(vw, pe, fname)

arch_names = {
    PE.IMAGE_FILE_MACHINE_I386:'i386',
    PE.IMAGE_FILE_MACHINE_AMD64:'amd64',
}


def loadPeIntoWorkspace(vw, pe, filename=None):

    mach = pe.IMAGE_NT_HEADERS.FileHeader.Machine

    arch = arch_names.get(mach)
    if arch == None:
        raise Exception("Machine %.4x is not supported for PE!" % mach )

    vw.setMeta('Architecture', arch)
    vw.setMeta('Format', 'pe')
    vw.setMeta('Platform', 'Windows')

    if arch == 'i386':
        vw.setMeta("DefaultCall", "cdecl")

    elif arch == 'amd64':
        vw.setMeta("DefaultCall", "amd64call")

    # FIXME this should die eventually!
    #vw.setMeta("ImportEmulation", "vivisect.impemu.windows")

    #if arch == 'i386':
        #vw.setMeta('SymbolikImportEmulation', 'vivisect.impemu.%s.windows' % arch)

    #vw.setMeta("DefaultCall", "cdecl")

    # Set ourselvs up for extended windows binary analysis

    baseaddr = pe.IMAGE_NT_HEADERS.OptionalHeader.ImageBase
    entry = pe.IMAGE_NT_HEADERS.OptionalHeader.AddressOfEntryPoint + baseaddr
    entryrva = entry - baseaddr

    codebase = pe.IMAGE_NT_HEADERS.OptionalHeader.BaseOfCode
    codesize = pe.IMAGE_NT_HEADERS.OptionalHeader.SizeOfCode
    codervamax = codebase+codesize

    fvivname = filename

    # This will help linkers with files that are re-named
    dllname = pe.getDllName()
    if dllname != None:
        fvivname = dllname

    if fvivname == None:
        fvivname = "pe_%.8x" % baseaddr

    fhash = "unknown hash"
    if os.path.exists(filename):
        fhash = v_parsers.md5File(filename)

    fname = vw.addFile(fvivname.lower(), baseaddr, fhash)

    # Add file version info if VS_VERSIONINFO has it
    vs = pe.getVS_VERSIONINFO()
    if vs != None:
        vsver = vs.getVersionValue('FileVersion')
        if vsver != None:
            vsver = vsver.split()[0]
            vw.setFileMeta(fname, 'Version', vsver)

    # Setup some va sets used by windows analysis modules
    vw.addVaSet("Library Loads", (("Address", int),("Library", str)))

    # Tell vivisect about ntdll functions that don't exit...
    vw.addNonExiter("ntdll.RtlExitUserThread")
    vw.addNonExiter("kernel32.ExitProcess")
    vw.addNonExiter("kernel32.ExitThread")
    vw.addNonExiter("kernel32.FatalExit")

    # Add the first page mapped in from the PE header.
    header = pe.readAtOffset(0, pe.IMAGE_NT_HEADERS.OptionalHeader.SizeOfHeaders)
    secalign = pe.IMAGE_NT_HEADERS.OptionalHeader.SectionAlignment

    subsys_majver = pe.IMAGE_NT_HEADERS.OptionalHeader.MajorSubsystemVersion
    subsys_minver = pe.IMAGE_NT_HEADERS.OptionalHeader.MinorSubsystemVersion

    secrem = len(header) % secalign
    if secrem != 0:
        header += "\x00" * (secalign - secrem)

    vw.addMemoryMap(baseaddr, e_mem.MM_READ, fname, header)
    vw.addSegment(baseaddr, len(header), "PE_Header", fname)

    hstruct = vw.makeStructure(baseaddr, "pe.IMAGE_DOS_HEADER")
    magicaddr = hstruct.e_lfanew
    if vw.readMemory(baseaddr + magicaddr, 2) != "PE":
        raise Exception("We only support PE exe's")

    padloc = vw.makePad(baseaddr + magicaddr, 4)

    ifhdr_va = padloc[L_VA] + padloc[L_SIZE]

    ifstruct = vw.makeStructure(ifhdr_va, "pe.IMAGE_FILE_HEADER")

    vw.makeStructure(ifhdr_va + len(ifstruct), "pe.IMAGE_OPTIONAL_HEADER")

    for sec in pe.sections:
        mapflags = 0

        chars = sec.Characteristics
        if chars & PE.IMAGE_SCN_MEM_READ:
            mapflags |= e_mem.MM_READ
        if chars & PE.IMAGE_SCN_MEM_WRITE:
            mapflags |= e_mem.MM_WRITE
        if chars & PE.IMAGE_SCN_MEM_EXECUTE:
            mapflags |= e_mem.MM_EXEC
        if chars & PE.IMAGE_SCN_CNT_CODE:
            mapflags |= e_mem.MM_EXEC

        secrva = sec.VirtualAddress
        secvsize = sec.VirtualSize
        secfsize = sec.SizeOfRawData
        secbase = secrva + baseaddr
        secname = sec.Name.strip("\x00")
        secrvamax = secrva + secvsize

        # If the section is part of BaseOfCode->SizeOfCode
        # force execute perms...
        if secrva >= codebase and secrva < codervamax:
            mapflags |= e_mem.MM_EXEC

        # If the entry point is in this section, force execute
        # permissions.
        if secrva <= entryrva and entryrva < secrvamax:
            mapflags |= e_mem.MM_EXEC

        if subsys_majver < 6 and mapflags & e_mem.MM_READ:
            mapflags |= e_mem.MM_EXEC

        try:
            secoff = pe.rvaToOffset(secrva)
            secbytes = pe.readAtOffset(secoff, secfsize)
            secbytes += "\x00" * (secvsize - secfsize)
            vw.addMemoryMap(secbase, mapflags, fname, secbytes)
            vw.addSegment(secbase, len(secbytes), secname, fname)
        except Exception, e:
            print "Error Loading Section (%s size:%d rva:%.8x offset: %d): %s" % (secname,secfsize,secrva,secoff,e)

    vw.addExport(entry, EXP_FUNCTION, "main_entry", fname)
    vw.addEntryPoint(entry)

    for rva,rtype in pe.getRelocations():
        vw.addRelocation(rva+baseaddr, vivisect.RTYPE_BASERELOC)

    for rva, lname, iname in pe.getImports():
        vw.makeImport(rva+baseaddr, lname, iname)

    exports = pe.getExports()
    for rva, ord, name in exports:
        eva = rva + baseaddr
        try:
            vw.addExport(eva, EXP_UNTYPED, name, fname)
        except Exception, e:
            vw.vprint('addExport Failed: %s.%s (0x%.8x): %s' % (fname,name,eva,e))
        if vw.probeMemory(eva, 1, e_mem.MM_EXEC):
            vw.addEntryPoint(eva)

    # Save off the ordinals...
    vw.setFileMeta(fname, 'ordinals', exports)

    fwds = pe.getForwarders()
    for rva, name, forwardname in fwds:
        vw.makeName(rva+baseaddr, "forwarder_%s.%s" % (fname, name))
        vw.makeString(rva+baseaddr)

    vw.setFileMeta(fname, 'forwarders', fwds)

    # Check For SafeSEH list...
    if pe.IMAGE_LOAD_CONFIG != None:

        vw.setFileMeta(fname, "SafeSEH", True)

        va = pe.IMAGE_LOAD_CONFIG.SEHandlerTable
        if va != 0:
            vw.makeName(va, "%s.SEHandlerTable" % fname)
            count = pe.IMAGE_LOAD_CONFIG.SEHandlerCount
            # Just cheat and use the workspace with memory maps in it already
            for h in vw.readMemoryFormat(va, "<%dP" % count):
                sehva = baseaddr + h
                vw.addEntryPoint(sehva)
                #vw.hintFunction(sehva, meta={'SafeSEH':True})

    # Last but not least, see if we have symbol support and use it if we do
    if vt_win32.dbghelp:

        s = vt_win32.Win32SymbolParser(-1, filename, baseaddr)

        # We don't want exports or whatever because we already have them
        s.symopts |= vt_win32.SYMOPT_EXACT_SYMBOLS
        s.parse()

        # Add names for any symbols which are missing them
        for symname, symva, size, flags in s.symbols:

            if not vw.isValidPointer(symva):
                continue

            try:

                if vw.getName(symva) == None:
                    vw.makeName(symva, symname, filelocal=True)

            except Exception, e:
                vw.vprint("Symbol Load Error: %s" % e)

        # Also, lets set the locals/args name hints if we found any
        vw.setFileMeta(fname, 'PELocalHints', s._sym_locals)

    # Parse up the new amd64 .pdata section used by new
    # fangled exception unwinding.
    sec = pe.getSectionByName('.pdata')
    if sec != None:
        va = sec.VirtualAddress + baseaddr
        vamax = va + sec.VirtualSize
        while va < vamax:
            f = vw.makeStructure(va, 'pe.IMAGE_RUNTIME_FUNCTION_ENTRY')
            fva = f.BeginAddress + baseaddr
            b = vw.readMemoryFormat(baseaddr + f.UnwindInfoAddress, '<B')[0]
            ver = b & 0x7
            flags = b >> 3
            # Check if it's a function *block* rather than a function *entry*
            if not (flags & PE.UNW_FLAG_CHAININFO):
                vw.addEntryPoint(fva)
            va += len(f)

    return fname
