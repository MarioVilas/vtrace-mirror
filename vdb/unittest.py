import sys
import traceback

import vdb.testmods
import vdb.testmods.regtest as v_t_regtest
import vdb.testmods.writemem as v_t_writemem
import vdb.testmods.basictest as v_t_basictest
import vdb.testmods.attachtest as v_t_attachtest
import vdb.testmods.threadtest as v_t_threadtest
import vdb.testmods.execthreadtest as v_t_execthreadtest

tests = [
    vdb.testmods.TestModule(),
    v_t_basictest.BasicTest(),
    v_t_attachtest.AttachTest(),
    v_t_regtest.RegisterAccessTest(),
    v_t_writemem.WriteMemTest(),
    v_t_threadtest.ThreadTest(),
    v_t_execthreadtest.ExecThreadTest(),
]

def main():

    for test in tests:
        testname = test.__class__.__name__
        try:
            stage = 'prep'
            test.prepTest()
            stage='run'
            test.runTest()
            stage='clean'
            test.cleanTest()
            print('Test Success: %s' % test.__class__.__name__)
        except Exception, e:
            traceback.print_exc()
            print('Test Failure: %s (in %s) %s' % (testname, stage, e))

if __name__ == '__main__':
    sys.exit(main())
