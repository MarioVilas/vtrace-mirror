
from vivisect.symboliks.common import *

class SymbolikCallingConvention:

    def getSymbolikArgs(emu, argv, argt, update=False):
        '''
        Used when symbolik emulation discovers a call while doing emulation.  This allows
        per-arch-calling-convention argument parsing for updates to fofx effects...
        '''
        raise Exception('%s must implement getSymbolikArgs()' % self.__class__.__name__)

    def setSymbolikArgs(self, emu, argv):
        '''
        Setup the emulator for emulation of a call to a function with this calling convention
        and the specified arguments in argv.

        Example:
            cconv.setSymbolikArgs(emu, ['arg0', 'arg1'])
        '''
        raise Exception('%s must implement setSymbolikArgs!' % self.__class__.__name__)

    def setSymbolikReturn(self, emu, retsym, argv):
        '''
        Set the fofx() return state in the calling emulator to reflect that state introduced by
        our callee.

        Example:
            cconv.setSymbolikReturn(emu, Var('foo'), 
        '''
        raise Exception('%s must implement setSymbolikReturn()' % self.__class__.__name__)

