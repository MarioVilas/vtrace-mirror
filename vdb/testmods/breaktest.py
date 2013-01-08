
import sys
import time
import ctypes
import threading

import vdb.testmods as v_testmods

plat_syms = {
    'Windows':'kernel32.ExitProcess',
    'Linux':'ld.brk',
    'FreeBSD':'libc.exit',
}

pycode = 'trace.setMeta("testbphit", 1)'

class BreakpointTest(v_testmods.VtracePythonTest):

    modname = 'vdb.testmods.breaktest'

    def runTest(self):

        plat = self.trace.getMeta('Platform')
        symname = plat_syms.get( plat )

        bpid = self.trace.addBreakByExpr( symname )
        self.trace.setBreakpointCode(bpid, pycode)

        #import vdb
        #db = vdb.Vdb(trace=self.trace)
        ##import code
        #code.interact(local=locals())
        #db.cmdloop()

        self.trace.setMode('RunForever',True)
        self.trace.run()

        assert( self.trace.getMeta('ExitCode', 0) == 30 )
        assert( self.trace.getMeta('testbphit') )


if __name__ == '__main__':

    import sys
    sys.exit(30)
