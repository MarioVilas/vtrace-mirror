
import sys
import time
import ctypes
import threading

import vdb.stalker as v_stalker
import vdb.testmods as v_testmods

plat_syms = {
    'Windows':'ntdll.RtlAllocateHeap',
    'Linux':'ld.brk',
    'FreeBSD':'libc.exit',
}

class StalkerTest(v_testmods.VtracePythonTest):

    modname = 'vdb.testmods.stalkertest'

    def runTest(self):

        plat = self.trace.getMeta('Platform')
        symname = plat_syms.get( plat )

        entry = self.trace.parseExpression(symname)
        v_stalker.addStalkerEntry(self.trace, entry)

        self.trace.setMode('RunForever',True)
        self.trace.run()
        assert( self.trace.getMeta('ExitCode', 0) == 30 )
        assert( len( v_stalker.getStalkerHits( self.trace ) ) )


if __name__ == '__main__':

    import sys
    sys.exit(30)
