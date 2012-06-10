'''
All information about the number of arguments (and names) for the given APIs
for different platforms is here.

All modules which are expected to be "Import API" modules must implement:

def getImportAPI( impname ) which returns ( 'final_imp_name', 'calling convention', [ arg0, ... ] )

For example:

    on i386 winodws...

    getImportAPI('kernel32.GetComputerNameA') -> ('kernel32.GetComputerNameA', 'stdcall', ('lpBuffer','lpnSize'))
    getImportAPI('kernel32.HeapAlloc') -> ('ntdll.RtlAllocateHeap', 'stdcall', ('HeapHandle', 'Flags', 'Size') )

    or on amd64 linux

    getImportAPI('libc.malloc') -> ('libc.malloc', 'amd64call', ('memSize',))

'''
