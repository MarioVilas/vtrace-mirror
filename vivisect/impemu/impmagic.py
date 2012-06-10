
import struct

import vstruct

#FIXME hard-coded half-pages
# Some values to use if you'd like to give the API's some hints
uninit_map_byte = "\xfc"
uninit_heap_byte = "\xfd"
uninit_stack_byte = "\xfe"

PREC_MAX = 10

class EmuMagic:

    # All emu-magic has precedence. Higher will be more likely to over-ride others
    __precedence__ = 1

    # All magic classes have a default name.  This name (plus an index) is
    # used whenever a function is identified to take a magic object.
    __defname__ = "unkn"

    def __init__(self):
        self.va = 0

    def addToWorkspace(self, vw, va):
        """
        This method should be implemented by EmuMagic types who know
        how to modify a viv workspace when their particular magic type
        is identified existing in the workspace memory.
        """
        #print "FIXME 0x%.8x: Should be  %s" % (va, repr(self))
        pass

    def setMagicVa(self, va):
        self.va = va

    @classmethod
    def getDefName(cls):
        """
        Return the default name for a new variable of this type
        (mostly used for naming function arguments, etc...)
        """
        return cls.__defname__

    def __repr__(self):
        return self.__class__.__name__

    def __long__(self):
        return self.va

    def __int__(self):
        return self.va

class Unknown(EmuMagic):
    """
    Default for unknown argument types.
    """
    __precedence__ = 0

    def __repr__(self):
        return "Unknown(0x%.8x)" % self.va

class VStructMagic(EmuMagic):

    # Extend this to make vstruct aware impmagic types

    __vsname__ = "unknown"

    def addToWorkspace(self, vw, va):
        vw.makeStructure(va, self.__class__.__vsname__)

class Pointer(EmuMagic):

    __defname__ = "ptr"

    def __repr__(self):
        return "Pointer(0x%.8x)" % self.va

class ReturnValue(EmuMagic):
    __precedence__ = -1 # We never want to say this is what a func takes

    def __init__(self, funcva, fname):
        EmuMagic.__init__(self)
        self.funcva = funcva
        self.fname = fname

    def __repr__(self):
        return "RetVal(%.8x:%s)" % (self.funcva, self.fname)

class ImportEntry(EmuMagic):

    __defname__ = "funcptr"

    def __init__(self, iva, name):
        EmuMagic.__init__(self)
        self.iva = iva
        self.name = name

    def __repr__(self):
        return "Import(%s)" % (self.name)

class MagicDeref(EmuMagic):
    """
    A special magic object created by the read of an offset
    into another magic value...
    """
    def __init__(self, parent, offset):
        EmuMagic.__init__(self)
        self.parent = parent
        self.offset = offset

    # FIXME could implement getDefName...

    def __repr__(self):
        return "[ %s + %s ]" % (repr(self.parent), self.offset)

##### Some basic types
class BOOL(EmuMagic):
    __precedence__ = 3
    __defname__ = "isTrue"

    def __init__(self, state=False):
        EmuMagic.__init__(self)
        self.state = state

    def __repr__(self):
        return "BOOL(%s)" % self.state

class BYTE(EmuMagic):
    __defname__ = 'byt'
    def __init__(self, val=0):
        EmuMagic.__init__(self)
        self.val = val

class INT16(EmuMagic):
    pass

class UINT16(EmuMagic):
    pass

class INT32(EmuMagic):
    pass

class UINT32(EmuMagic):
    pass

class StringA(EmuMagic):
    """
    Ascii style NULL terminated string
    """
    __precedence__ = 3
    __defname__ = 'stra'

    def addToWorkspace(self, vw, va):
        vw.makeString(va)

class StringW(EmuMagic):
    """
    utf_16_le MS style unicode string.
    """
    __precedence__ = 3
    __defname__ = 'strw'

    def addToWorkspace(self, vw, va):
        vw.makeUnicode(va)

#FIXME eventually pascall strings etc...

################################################
#
# Some more context specific primative types
#

class PID(INT16):
    __precedence__ = 10
    pass

class FileNameA(StringA):
    __precedence__ = 5
    __defname__ = 'fnamea'

class FileNameW(StringW):
    __precedence__ = 5
    __defname__ = 'fnamew'

class FUNCPTR(EmuMagic):
    __precedence__ = 5
    __defname__ = 'funcptr'

    def __init__(self, libname='unknown', funcname='unknown'):
        EmuMagic.__init__(self)
        self.libname = libname
        self.funcname = funcname

    def addToWorkspace(self, vw, va):
        vw.makeFunction(va)

    def __repr__(self):
        return "FUNCPTR(%s.%s)" % (self.libname, self.funcname)

################################################
#
# Some generic comp-sci types.  These are here so
# library implementations may extend them and allow the
# emulation subsystem to handle them in a universal way.
#
class HEAP(EmuMagic):
    __precedence__ = 10
    def __init__(self, flags=0):
        EmuMagic.__init__(self)
        self.flags = flags

class HeapChunk(EmuMagic):
    __precedence__ = -1 # We never want to say this is what a func takes
    def __init__(self, size, flags=0):
        EmuMagic.__init__(self)
        self.size = size
        self.flags = flags
        self.free = False

    def __repr__(self):
        return "HeapChunk(size %d:flags %.8x:free %s)" % (self.size,self.flags,self.free)

class MUTEX(EmuMagic):
    __precedence__ = 10
    def __init__(self, flags):
        EmuMagic.__init__(self)
        self.flags = flags

class HANDLE(EmuMagic):

    __precedence__ = 5

    def __init__(self, typename="unknown", name="unknown", data="unknown"):
        EmuMagic.__init__(self)
        self.typename = typename
        self.name = name
        self.data = data

    def __repr__(self):
        return "HANDLE(%s:%s)" % (self.typename,self.name)

class LIBRARY(EmuMagic):
    """
    A reference to a loaded library.
    """
    __precedence__ = 10
    def __init__(self, libname="unknownlib"):
        EmuMagic.__init__(self)
        self.libname = libname

class PROCESS(EmuMagic):
    """
    A windows/mach style process handle.
    """
    __precedence__ = 10

class THREAD(EmuMagic):
    """
    A windows/mach style thread handle.
    """
    __precedence__ = 10

################################################
#
# Emulation Helper Types
#
class StackArg(EmuMagic):
    __precedence__ = -1 # We never want to say this is what a func takes

    def __init__(self, index=0):
        EmuMagic.__init__(self)
        self.index = index

    def __repr__(self):
        return "arg%d" % self.index

class StackLocal(EmuMagic):
    __precedence__ = -1 # We never want to say this is what a func takes
    def __init__(self, offset=0):
        EmuMagic.__init__(self)
        self.offset = offset
    def __repr__(self):
        return 'local_%d' % self.offset

class SavedProgramCounter(EmuMagic):
    __precedence__ = -1 # We never want to say this is what a func takes

    def __repr__(self):
        return "SavedPc(%.8x)" % self.va

class UninitReg(EmuMagic):
    __precedence__ = -1 # We never want to say this is what a func takes

    def __init__(self, rname, regindex):
        EmuMagic.__init__(self)
        self.rname = rname
        self.regindex = regindex

    def __repr__(self):
        return "Uninit(%s)" % self.rname

class ObjectRef(EmuMagic):
    __precedence__ = 3

    def __init__(self, thisname="Unknown"):
        EmuMagic.__init__(self)
        self.thisname = thisname

    def __repr__(self):
        return "This(%s)" % self.thisname

