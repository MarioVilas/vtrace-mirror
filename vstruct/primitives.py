
import struct

class v_base(object):
    def __init__(self):
        self._vs_meta = {}

    def vsGetMeta(self, name, defval=None):
        return self._vs_meta.get(name, defval)

    def vsSetMeta(self, name, value):
        self._vs_meta[name] = value

    # Sub-classes (primitive base, or VStruct must have these
    def vsParse(self, bytes): return NotImplemented
    def vsGetFormat(self): return NotImplemented
    def vsIsPrim(self): return NotImplemented
    def vsGetTypeName(self): return NotImplemented

class v_prim(v_base):

    def __init__(self):
        v_base.__init__(self)
        # Used by base len(),vsGetFormat, etc...
        self._vs_value = None
        self._vs_length = None
        self._vs_fmt = None

    def vsIsPrim(self):
        return True

    def vsGetTypeName(self):
        return self.__class__.__name__

    def vsParse(self, bytes):
        """
        Parser for primitives which assumes we are
        calling parse directly.
        """
        fmt = "<%s" % self.vsGetFormat()
        val = struct.unpack(fmt, bytes)[0]
        self.vsSetParsedValue(val)

    def vsSetParsedValue(self, value):
        """
        Primitives will be assigned their values by a parser
        which chops data up with struct format strings.  This
        method will be called by parsers to assign the value
        of a primitive from a struct.unpack call.
        """
        self.vsSetValue(value)

    def vsGetValue(self):
        return self._vs_value

    def vsSetValue(self, value):
        """
        Set the type specific value for this field.
        """
        self._vs_value = value

    def vsGetFormat(self):
        return self._vs_fmt

    def __repr__(self):
        return repr(self.vsGetValue())

    def __len__(self):
        return self._vs_length

    def __str__(self):
        return str(self.vsGetValue())

class v_number(v_prim):

    def __init__(self, value=0, bigend=False):
        v_prim.__init__(self)
        self._vs_bigend = bigend
        self._vs_length = struct.calcsize(self.vsGetFormat())
        self.vsSetValue(value)

    def vsSetValue(self, value):
        """
        Assure that the value is long() able for all numeric types.
        """
        self._vs_value = long(value)

    def vsSetParsedValue(self, value):
        # We were parsed little endian.  Switch if needed.
        if self._vs_bigend:
            oval = value
            value = 0
            for i in range(self._vs_length):
                value = value << 8
                value += (oval >> (8*i)) & 0xff
        self.vsSetValue(value)

    def vsGetFormat(self):
        return self.__class__._vs_fmt

    def __int__(self):
        return int(self._vs_value)

    def __long__(self):
        return long(self._vs_value)

    ##################################################################
    # Implement the number API

    def __add__(self, other): return long(self) + long(other)
    def __sub__(self, other): return long(self) - long(other)
    def __mul__(self, other): return long(self) * long(other)
    def __div__(self, other): return long(self) / long(other)
    def __floordiv__(self, other): return long(self) // long(other)
    def __mod__(self, other): return long(self) % long(other)
    def __divmod__(self, other): return divmod(long(self), long(other))
    def __pow__(self, other, modulo=None): return pow(long(self), long(other), modulo)
    def __lshift__(self, other): return long(self) << long(other)
    def __rshift__(self, other): return long(self) >> long(other)
    def __and__(self, other): return long(self) & long(other)
    def __xor__(self, other): return long(self) ^ long(other)
    def __or__(self, other): return long(self) | long(other)

    # Operator swapped variants
    def __radd__(self, other): return long(other) + long(self)
    def __rsub__(self, other): return long(other) - long(self)
    def __rmul__(self, other): return long(other) * long(self)
    def __rdiv__(self, other): return long(other) / long(self)
    def __rfloordiv__(self, other): return long(other) // long(self)
    def __rmod__(self, other): return long(other) % long(self)
    def __rdivmod__(self, other): return divmod(long(other), long(self))
    def __rpow__(self, other, modulo=None): return pow(long(other), long(self), modulo)
    def __rlshift__(self, other): return long(other) << long(self)
    def __rrshift__(self, other): return long(other) >> long(self)
    def __rand__(self, other): return long(other) & long(self)
    def __rxor__(self, other): return long(other) ^ long(self)
    def __ror__(self, other): return long(other) | long(self)

    # Inplace variants
    def __iadd__(self, other): self.vsSetValue(self+other); return self
    def __isub__(self, other): self.vsSetValue(self - other); return self
    def __imul__(self, other): self.vsSetValue(self*other); return self
    def __idiv__(self, other): self.vsSetValue(self/other); return self
    def __ifloordiv__(self, other): self.vsSetValue(self // other); return self
    def __imod__(self, other): self.vsSetValue(self % other); return self
    def __ipow__(self, other, modulo=None): self.vsSetValue(pow(self, other, modulo)); return self
    def __ilshift__(self, other): self.vsSetValue(self << other); return self
    def __irshift__(self, other): self.vsSetValue(self >> other); return self
    def __iand__(self, other): self.vsSetValue(self & other); return self
    def __ixor__(self, other): self.vsSetValue(self ^ other); return self
    def __ior__(self, other): self.vsSetValue(self | other); return self

    # operator helpers
    def __neg__(self): return -(long(self))
    def __pos__(self): return +(long(self))
    def __abs__(self): return abs(long(self))
    def __invert__(self): return ~(long(self))

    # index use helper
    def __index__(self): return long(self)

    def __coerce__(self, other):
        try:
            return long(self),long(other)
        except Exception, e:
            return NotImplemented

    # Print helpers
    def __hex__(self): return hex(long(self))
    def __oct__(self): return oct(long(self))

class v_uint8(v_number):
    _vs_builder = True
    _vs_fmt = "B"

class v_uint16(v_number):
    _vs_builder = True
    _vs_fmt = "H"

class v_uint32(v_number):
    _vs_builder = True
    _vs_fmt = "L"

class v_uint64(v_number):
    _vs_builder = True
    _vs_fmt = "Q"

class v_int8(v_number):
    _vs_builder = True
    _vs_fmt = "b"

class v_int16(v_number):
    _vs_builder = True
    _vs_fmt = "h"

class v_int32(v_number):
    _vs_builder = True
    _vs_fmt = "l"

class v_int64(v_number):
    _vs_builder = True
    _vs_fmt = "q"

class v_ptr(v_number):
    _vs_builder = True
    _vs_fmt = "L"
    def __repr__(self):
        return "0x%.8x" % self._vs_value

class v_bytes(v_prim):

    _vs_builder = True

    def __init__(self, size=4):
        v_prim.__init__(self)
        self._vs_length = size
        self._vs_value = "\x00" * size

    def vsGetFormat(self):
        return "%ds" % len(self)

    def __repr__(self):
        return self._vs_value.encode('hex')

class v_str(v_prim):

    _vs_builder = True

    def __init__(self, size=4):
        v_prim.__init__(self)
        self._vs_length = size
        self._vs_value = "A"*size

    def vsGetFormat(self):
        return "%ds" % len(self)

    def __len__(self):
        return len(self._vs_value)

class GUID(v_prim):

    _vs_builder = True

    def __init__(self):
        v_prim.__init__(self)
        self._vs_length = 16
        self._vs_value = "\x00" * 16
        self._vs_fmt = "16s"
        self._guid_fields = (0,0,0,0)
        self._guid_text_vals = (0,0,0,0,0)

    def vsSetValue(self, bytes):
        self._guid_fields = struct.unpack("<LHH8B", bytes)

    def __repr__(self):
        base = "{%.8x-%.4x-%.4x-%.2x%.2x-%.2x%.2x%.2x%.2x%.2x%.2x}"
        return base  % self._guid_fields

