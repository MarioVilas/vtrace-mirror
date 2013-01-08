import os
import sys
import time
import ctypes

import vtrace
import vdb.testmods as v_testmods

class WriteMemTest(v_testmods.VtracePythonProcTest):
    modname = 'vdb.testmods.writemem'

    def runTest(self):
        self.trace.setMode('RunForever', True)
        self.trace.setMode('NonBlocking', True)
        self.runProcess()
        addrstr = self.proc.stdout.readline()
        addr = int( addrstr, 16 )

        testbuf = os.urandom( 10 ).encode('hex')

        # Stop him so we can write to the buffer he created
        self.trace.sendBreak()
        self.trace.writeMemory( addr, testbuf )
        self.trace.run()

        # Now write to his stdin to let him keep going
        self.proc.stdin.write('woot\r\n')

        # He should now print what we wrote...
        assert( self.proc.stdout.readline().strip() == testbuf )
        while not self.trace.exited: time.sleep(0.1)
        assert( self.trace.getMeta('ExitCode') == 99 )

if __name__ == '__main__':
    v_testmods.waitForTest()
    buf = ctypes.create_string_buffer( 32 )
    sys.stdout.write('0x%.8x\r\n' % ctypes.addressof( buf ))
    sys.stdout.flush()

    sys.stdin.readline()

    sys.stdout.write('%s\n' % buf.value )
    sys.stdout.flush()

    sys.exit(99)
