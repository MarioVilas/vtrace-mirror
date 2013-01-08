import sys
import vdb.testmods as v_testmods

class RegisterAccessTest(v_testmods.VtracePythonProcTest):
    modname = 'vdb.testmods.regtest'

    def runTest(self):
        self.trace.setMode('RunForever', True)
        pc = self.trace.getProgramCounter()
        sc = self.trace.getStackCounter()
        self.trace.setProgramCounter( pc )
        self.trace.setStackCounter( sc )
        self.runProcess()
        assert( pc )
        assert( sc )
        assert( self.trace.getMeta('ExitCode', 0) == 22 )

if __name__ == '__main__':
    v_testmods.waitForTest()
    sys.exit(22)
