import sys
import time
import threading

import vtrace
import vtrace.notifiers as vt_notif

import vdb.testmods as v_testmods

class ThreadTest(v_testmods.VtracePythonProcTest, vt_notif.Notifier):

    modname = 'vdb.testmods.threadtest'

    def __init__(self):
        v_testmods.VtracePythonProcTest.__init__(self)
        vt_notif.Notifier.__init__(self)
        self.got_thread_create = False
        self.got_thread_exit = False

    def notify(self, event, trace):

        if event == vtrace.NOTIFY_CREATE_THREAD:
            self.got_thread_create = True
            return

        if event == vtrace.NOTIFY_EXIT_THREAD:
            self.got_thread_exit = True
            return

    def runTest(self):
        #assert( len( self.trace.getThreads() ) == 2 )
        self.trace.setMode('RunForever', True)
        self.trace.registerNotifier( vtrace.NOTIFY_ALL, self )
        self.runProcess()

        assert( self.got_thread_create )
        assert( self.got_thread_exit )
        assert( self.trace.getMeta('ExitCode', 0) == 35 )

if __name__ == '__main__':
    #thr0 = threading.Thread( target=time.sleep, args=( 9999, ) )
    #thr0.setDaemon(True)
    #thr0.start()

    import time; time.sleep(0.2)

    v_testmods.waitForTest()

    thr = threading.Thread( target=time.sleep, args=(0.1, ) )
    thr.start()

    thr.join()

    sys.exit(35)
