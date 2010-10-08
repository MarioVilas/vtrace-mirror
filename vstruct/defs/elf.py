
import vstruct
from vstruct.primitives import *

@vstruct.structbuilder
def Elf32():
    x = vstruct.VStruct("Elf32")
    x.e_ident     = v_bytes(16)
    x.e_type      = v_uint16()
    x.e_machine   = v_uint16()
    x.e_version   = v_uint32()
    x.e_entry     = v_uint32()
    x.e_phoff     = v_uint32()
    x.e_shoff     = v_uint32()
    x.e_flags     = v_uint32()
    x.e_ehsize    = v_uint16()
    x.e_phentsize = v_uint16()
    x.e_phnum     = v_uint16()
    x.e_shentsize = v_uint16()
    x.e_shnum     = v_uint16()
    x.e_shstrndx  = v_uint16()
    return x

@vstruct.structbuilder
def Elf32Dynamic():
    x = vstruct.VStruct("Elf32Dynamic")
    x.d_tag   = v_uint32()
    x.d_value = v_uint32()
    return x

@vstruct.structbuilder
def Elf32Reloc():
    x = vstruct.VStruct("Elf32Reloc")
    x.r_offset = v_ptr()
    x.r_info   = v_uint32()
    return x

@vstruct.structbuilder
def Elf32Symbol():
    x = vstruct.VStruct("Elf32Symbol")
    x.st_name  = v_uint32()
    x.st_value = v_uint32()
    x.st_size  = v_uint32()
    x.st_info  = v_uint8()
    x.st_other = v_uint8()
    x.st_shndx = v_uint16()
    return x

# def Elf64Symbol

