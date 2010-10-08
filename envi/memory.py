import struct
import envi

# Memory Map Permission Flags
MM_READ = 0x4
MM_WRITE = 0x2
MM_EXEC = 0x1
MM_SHARED = 0x08

MM_RWX = (MM_READ | MM_WRITE | MM_EXEC)

def reprPerms(mask):
    plist = ['-','-','-','-']
    if mask & MM_SHARED:
        plist[0] = 's'
    if mask & MM_READ:
        plist[1] = 'r'
    if mask & MM_WRITE:
        plist[2] = 'w'
    if mask & MM_EXEC:
        plist[3] = 'x'

    return "".join(plist)

def parsePerms(pstr):
    ret = 0
    if pstr.find('s') != -1: ret |= MM_SHARED
    if pstr.find('r') != -1: ret |= MM_READ
    if pstr.find('w') != -1: ret |= MM_WRITE
    if pstr.find('x') != -1: ret |= MM_EXEC
    return ret

class IMemory:
    """
    This is the interface spec (and a few helper utils)
    for the unified memory object interface.

    NOTE: If your actual underlying memory format is such
    that over-riding anything (like isValidPointer!) can
    be faster than the default implementation, DO IT!
    """

    def __init__(self):
        self.imem_psize = struct.calcsize("P")

    def readMemory(self, va, size):
        """
        Read memory from the specified virtual address for size bytes
        and return it as a python string.

        Example: mem.readMemory(0x41414141, 20) -> "A..."
        """
        raise Exception("must implement readMemory!")

    def writeMemory(self, va, bytes):
        """
        Write the given bytes to the specified virtual address.

        Example: mem.writeMemory(0x41414141, "VISI")
        """
        raise Exception("must implement writeMemory!")

    def protectMemory(self, va, size, perms):
        """
        Change the protections for the given memory map. On most platforms
        the va/size *must* exactly match an existing memory map.
        """
        raise Exception("must implement protectMemory!")

    def allocateMemory(self, size, perms=MM_RWX, suggestaddr=0):
        raise Exception("must implement allocateMemory!")

    def addMemoryMap(self, mapva, perms, fname, bytes):
        raise Exception("must implement addMemoryMap!")

    def getMemoryMaps(self):
        raise Exception("must implement getMemoryMaps!")

    # Mostly helpers from here down...
    def readMemoryFormat(self, va, fmt):
        # Somehow, pointers are "signed" when they
        # get chopped up by python's struct package
        if self.imem_psize == 4:
            fmt = fmt.replace("P","L")
        elif self.imm_psize == 8:
            fmt = fmt.replace("P","Q")

        size = struct.calcsize(fmt)
        bytes = self.readMemory(va, size)
        return struct.unpack(fmt, bytes)

    def writeMemoryFormat(self, va, fmt, *args):
        bytes = struct.pack(fmt, *args)
        self.writeMemory(va, bytes)

    def getMemoryMap(self, va):
        """
        Return a tuple of mapva,size,perms,filename for the memory
        map which contains the specified address (or None).
        """
        for mapva,size,perms,mname in self.getMemoryMaps():
            if va >= mapva and va < (mapva+size):
                return (mapva,size,perms,mname)
        return None

    def isValidPointer(self, va):
        if self.getMemoryMap(va) == None:
            return False
        return True

    def searchMemory(self, needle):
        """
        A quick cheater way to searchMemoryRange() for each
        of the current memory maps.
        """
        results = []
        for va,size,perm,fname in self.getMemoryMaps():
            if not perm & MM_READ:
                continue
            try:
                results.extend(self.searchMemoryRange(needle, va, size))
            except:
                pass # Some platforms dont let debuggers read non-readable mem

        return results

    def searchMemoryRange(self, needle, address, size):
        """
        Search the specified memory range (address -> size)
        for the string needle.   Return a list of addresses
        where the match occurs.
        """
        results = []
        memory = self.readMemory(address, size)
        offset = 0
        while offset < size:
            loc = memory.find(needle, offset)
            if loc == -1: # No more to be found ;)
                break
            results.append(address+loc)
            offset = loc+len(needle) # Skip one past our matcher

        return results

class MemoryObject(IMemory):
    def __init__(self, maps=None, pagesize=4096):
        """
        Take a set of memory maps (va, perms, bytes) and put them in
        a sparse space finder. You may specify your own page-size to optimize
        the search for an architecture.
        """
        IMemory.__init__(self)
        self.pagesize = pagesize
        self.mask = (0-pagesize) & 0xffffffff
        self.maps = []
        self.maplookup = {}
        self.bytelookup = {}
        if maps != None:
            for va,perms,fname,bytes in maps:
                self.addMemoryMap(va, perms, fname, bytes)

    def addMemoryMap(self, va, perms, fname, bytes):
        x = [va, perms, fname, bytes] # Asign to a list cause we need to write to it
        maptup = (va, len(bytes), perms, fname)
        bytelist = [va, perms, bytes]
        base = va & self.mask
        maxva = va + len(bytes)
        while base < maxva:
            self.maplookup[base] = maptup
            self.bytelookup[base] = bytelist
            base += self.pagesize
        self.maps.append((va, len(bytes), perms, fname))

    def getMemoryMap(self, va):
        """
        Get the va,perms,bytes list for this map
        """
        return self.maplookup.get(va & self.mask)

    def getMemoryMaps(self):
        return list(self.maps)

    #FIXME rename this... it's aweful
    #FIXME make extendable maps for things like the stack
    def checkMemory(self, va, perms=0):
        map = self.maplookup.get(va & self.mask)
        if map == None:
            return False
        if (perms & map[1]) != perms:
            return False
        return True

    def readMemory(self, va, size):
        map = self.bytelookup.get(va & self.mask)
        if map == None:
            raise envi.SegmentationViolation(va)
        mapva, mperm, mapbytes = map
        if not mperm & 4: #FIXME make permission bits
            raise envi.SegmentationViolation(va)
        offset = va - mapva
        return mapbytes[offset:offset+size]

    def writeMemory(self, va, bytes):
        map = self.bytelookup.get(va & self.mask)
        if map == None:
            raise envi.SegmentationViolation(va)
        mva, mperm, mbytes = map
        if not mperm & 2: #FIXME make permission bits
            raise envi.SegmentationViolation(va)
        offset = va - mva
        map[2] = mbytes[:offset] + bytes + mbytes[offset+len(bytes):]

class MemoryTracker:
    """
    A utility that will track memory access and let everything be valid
    memory for reading and writing.
    """
    def __init__(self):
        self.bytes = {}
        self.reads = []
        self.writes = []

    def readMemory(self, va, size):
        #FIXME make this unique so it can be tracked
        #FIXME make this return anything he's written already
        self.reads.append((va, size))
        return "A"*size

    def writeMemory(self, va, bytes):
        self.writes.append((va, bytes))
        self.bytes[va] = bytes
        
class FakeMemory:
    def checkMemory(self, va, perms=0):
        return True
    def readMemory(self, va, size):
        return "A"*size
    def writeMemory(self, va, bytes):
        pass

