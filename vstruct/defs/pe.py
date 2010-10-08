
import vstruct
from vstruct.primitives import *

@vstruct.structbuilder
def IMAGE_BASE_RELOCATION():
    x = vstruct.VStruct("IMAGE_BASE_RELOCATION")
    x.VirtualAddress = v_uint32()
    x.SizeOfBlock    = v_uint32()
    return x

@vstruct.structbuilder
def IMAGE_DATA_DIRECTORY():
    x = vstruct.VStruct("IMAGE_DATA_DIRECTORY")
    x.VirtualAddress = v_uint32()
    x.Size           = v_uint32()
    return x

@vstruct.structbuilder
def IMAGE_DOS_HEADER():
    x = vstruct.VStruct("IMAGE_DOS_HEADER")
    x.e_magic    = v_uint16()
    x.e_cblp     = v_uint16()
    x.e_cp       = v_uint16()
    x.e_crlc     = v_uint16()
    x.e_cparhdr  = v_uint16()
    x.e_minalloc = v_uint16()
    x.e_maxalloc = v_uint16()
    x.e_ss       = v_uint16()
    x.e_sp       = v_uint16()
    x.e_csum     = v_uint16()
    x.e_ip       = v_uint16()
    x.e_cs       = v_uint16()
    x.e_lfarlc   = v_uint16()
    x.e_ovno     = v_uint16()
    x.e_res      = vstruct.VArray([v_uint16() for i in range(4)])
    x.e_oemid    = v_uint16()
    x.e_oeminfo  = v_uint16()
    x.e_res2     = vstruct.VArray([v_uint16() for i in range(10)])
    x.e_lfanew   = v_uint32()
    return x

@vstruct.structbuilder
def IMAGE_EXPORT_DIRECTORY():
    x = vstruct.VStruct("IMAGE_EXPORT_DIRECTORY")
    x.Characteristics    = v_uint32()
    x.TimeDateStamp      = v_uint32()
    x.MajorVersion       = v_uint16()
    x.MinorVersion       = v_uint16()
    x.Name               = v_uint32()
    x.Base               = v_uint32()
    x.NumberOfFunctions  = v_uint32()
    x.NumberOfNames      = v_uint32()
    x.AddressOfFunctions = v_uint32()
    x.AddressOfNames     = v_uint32()
    x.AddressOfOrdinals  = v_uint32()
    return x

@vstruct.structbuilder
def IMAGE_FILE_HEADER():
    x = vstruct.VStruct("IMAGE_FILE_HEADER")
    x.Machine              = v_uint16()
    x.NumberOfSections     = v_uint16()
    x.TimeDateStamp        = v_uint32()
    x.PointerToSymbolTable = v_uint32()
    x.NumberOfSymbols      = v_uint32()
    x.SizeOfOptionalHeader = v_uint16()
    x.Ccharacteristics     = v_uint16()
    return x

@vstruct.structbuilder
def IMAGE_IMPORT_DIRECTORY():
    x = vstruct.VStruct("IMAGE_IMPORT_DIRECTORY")
    x.OriginalFirstThunk = v_uint32()
    x.TimeDateStamp      = v_uint32()
    x.ForwarderChain     = v_uint32()
    x.Name               = v_uint32()
    x.FirstThunk         = v_uint32()
    return x

@vstruct.structbuilder
def IMAGE_LOAD_CONFIG_DIRECTORY():
    x = vstruct.VStruct("IMAGE_LOAD_CONFIG_DIRECTORY")
    x.Size                          = v_uint32()
    x.TimeDateStamp                 = v_uint32()
    x.MajorVersion                  = v_uint16()
    x.MinorVersion                  = v_uint16()
    x.GlobalFlagsClear              = v_uint32()
    x.GlobalFlagsSet                = v_uint32()
    x.CriticalSectionDefaultTimeout = v_uint32()
    x.DeCommitFreeBlockThreshold    = v_uint32()
    x.DeCommitTotalFreeThreshold    = v_uint32()
    x.LockPrefixTable               = v_uint32()
    x.MaximumAllocationSize         = v_uint32()
    x.VirtualMemoryThreshold        = v_uint32()
    x.ProcessHeapFlags              = v_uint32()
    x.ProcessAffinityMask           = v_uint32()
    x.CSDVersion                    = v_uint16()
    x.Reserved1                     = v_uint16()
    x.EditList                      = v_uint32()
    x.SecurityCookie                = v_uint32()
    x.SEHandlerTable                = v_uint32()
    x.SEHandlerCount                = v_uint32()
    return x

@vstruct.structbuilder
def IMAGE_NT_HEADERS():
    x = vstruct.VStruct("IMAGE_NT_HEADERS")
    x.Signature      = v_bytes(4)
    x.FileHeader     = IMAGE_FILE_HEADER()
    x.OptionalHeader = IMAGE_OPTIONAL_HEADER()
    return x

@vstruct.structbuilder
def IMAGE_OPTIONAL_HEADER():
    x = vstruct.VStruct("IMAGE_OPTIONAL_HEADER")
    x.Magic                       = v_bytes(2)
    x.MajorLinkerVersion          = v_uint8()
    x.MinorLinkerVersion          = v_uint8()
    x.SizeOfCode                  = v_uint32()
    x.SizeOfInitializedData       = v_uint32()
    x.SizeOfUninitializedData     = v_uint32()
    x.AddressOfEntryPoint         = v_uint32()
    x.BaseOfCode                  = v_uint32()
    x.BaseOfData                  = v_uint32()
    x.ImageBase                   = v_uint32()
    x.SectionAlignment            = v_uint32()
    x.FileAlignment               = v_uint32()
    x.MajorOperatingSystemVersion = v_uint16()
    x.MinorOperatingSystemVersion = v_uint16()
    x.MajorImageVersion           = v_uint16()
    x.MinorImageVersion           = v_uint16()
    x.MajorSubsystemVersion       = v_uint16()
    x.MinorSubsystemVersion       = v_uint16()
    x.Win32VersionValue           = v_uint32()
    x.SizeOfImage                 = v_uint32()
    x.SizeOfHeaders               = v_uint32()
    x.CheckSum                    = v_uint32()
    x.Subsystem                   = v_uint16()
    x.DllCharacteristics          = v_uint16()
    x.SizeOfStackReserve          = v_uint32()
    x.SizeOfStackCommit           = v_uint32()
    x.SizeOfHeapReserve           = v_uint32()
    x.SizeOfHeapCommit            = v_uint32()
    x.LoaderFlags                 = v_uint32()
    x.NumberOfRvaAndSizes         = v_uint32()
    x.DataDirectory               = vstruct.VArray([IMAGE_DATA_DIRECTORY() for i in range(16)])
    return x

@vstruct.structbuilder
def IMAGE_RESOURCE_DIRECTORY():
    x = vstruct.VStruct("IMAGE_RESOURCE_DIRECTORY")
    x.Characteristics      = v_uint32()
    x.TimeDateStamp        = v_uint32()
    x.MajorVersion         = v_uint16()
    x.MinorVersion         = v_uint16()
    x.NumberOfNamedEntries = v_uint16()
    x.NumberOfIdEntries    = v_uint16()
    return x

@vstruct.structbuilder
def IMAGE_SECTION_HEADER():
    x = vstruct.VStruct("IMAGE_SECTION_HEADER")
    x.Name                 = v_bytes(8)
    x.VirtualSize          = v_uint32()
    x.VirtualAddress       = v_uint32()
    x.SizeOfRawData        = v_uint32()
    x.PointerToRawData     = v_uint32()
    x.PointerToRelocations = v_uint32()
    x.PointerToLineNumbers = v_uint32()
    x.NumberOfRelocations  = v_uint16()
    x.NumberOfLineNumbers  = v_uint16()
    x.Characteristics      = v_uint32()
    return x

#    x = vstruct.VStruct(IMAGE_THUNK_DATA">
#return x

