
import vstruct
from vstruct.primitives import *

class Elf32(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.e_ident     = v_bytes(16)
        self.e_type      = v_uint16()
        self.e_machine   = v_uint16()
        self.e_version   = v_uint32()
        self.e_entry     = v_uint32()
        self.e_phoff     = v_uint32()
        self.e_shoff     = v_uint32()
        self.e_flags     = v_uint32()
        self.e_ehsize    = v_uint16()
        self.e_phentsize = v_uint16()
        self.e_phnum     = v_uint16()
        self.e_shentsize = v_uint16()
        self.e_shnum     = v_uint16()
        self.e_shstrndx  = v_uint16()

class Elf32Dynamic(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.d_tag   = v_uint32()
        self.d_value = v_uint32()

class Elf32Reloc(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.r_offset = v_ptr()
        self.r_info   = v_uint32()

class Elf32Symbol(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.st_name  = v_uint32()
        self.st_value = v_uint32()
        self.st_size  = v_uint32()
        self.st_info  = v_uint8()
        self.st_other = v_uint8()
        self.st_shndx = v_uint16()

# def Elf64Symbol

