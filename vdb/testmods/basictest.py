import sys
import time
import ctypes
import threading

import vdb.testmods as v_testmods

class BasicTest(v_testmods.VtracePythonTest):
    modname = 'vdb.testmods.basictest'

    def runTest(self):
        self.trace.setMode('RunForever',True)
        self.trace.run()
        assert( self.trace.getMeta('ExitCode', 0) == 30 )

if __name__ == '__main__':

    import sys
    #time.sleep(1)
    sys.exit(30)

