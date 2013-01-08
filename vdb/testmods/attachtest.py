import sys
import vdb.testmods as v_testmods

class AttachTest(v_testmods.VtracePythonProcTest):
    modname = 'vdb.testmods.attachtest'

    def runTest(self):
        self.trace.setMode('RunForever', True)
        self.runProcess()
        assert( self.trace.getMeta('ExitCode', 0) == 99 )

if __name__ == '__main__':
    v_testmods.waitForTest()
    sys.exit(99)
