
from vivisect.symboliks.common import *

class Constraint:
    '''
    A class to represent algibreic constraints which
    will be tracked by a given polynomial.
    '''

    revclass = None
    operstr = None

    def __init__(self, v1, v2):

        self._v1 = frobSymbol(v1)
        self._v2 = frobSymbol(v2)

        # FIXME consider making constraints into operators...
        # Their APIs and internals are basically the same!

    def walkTree(self, cb, ctx=None):
        self._v1.walkTree(cb, ctx=ctx)
        self._v2.walkTree(cb, ctx=ctx)
        self._v1 = cb(self._v1, ctx)
        self._v2 = cb(self._v2, ctx)

    def getWidth(self):
        return 4 # FIXME HACK

    def setSymSolverContext(self, slvctx):
        self._v1.setSymSolverContext(slvctx)
        self._v2.setSymSolverContext(slvctx)

    def __repr__(self):
        return '%s(%s,%s)' % (self.__class__.__name__, repr(self._v1), repr(self._v2))

    def __str__(self):
        return '%s %s %s' % (str(self._v1), self.operstr, str(self._v2))

    def __eq__(self, con):
        '''
        Is this constraint the same as some other?
        '''
        if not isinstance(con, Constraint):
            return False

        c1v1 = self._v1.solve()
        c1v2 = self._v2.solve()
        c2v1 = con._v1.solve()
        c2v2 = con._v2.solve()

        if c1v1 == c2v1 and c1v2 == c2v2 and self.__class__ == con.__class__:
            return True

        if c1v1 == c2v2 and c1v2 == c2v1 and self.__class__ == con.revclass:
            return True

        return False

    def reverse(self):
        if self.revclass == None:
            raise Exception('Constraints Must Define revclass!')
        return self.revclass(self._v1, self._v2)

    def reduce(self, emu=None):
        self._v1 = self._v1.reduce(emu=emu)
        self._v2 = self._v2.reduce(emu=emu)
        return self

    def update(self, emu):
        v1 = self._v1.update(emu)
        v2 = self._v2.update(emu)
        return self.__class__(v1, v2)

    def prove(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return self.testTruth(v1, v2)

    def solve(self, emu=None):
        # A "solution" for a condition is it's boolean state as int...
        return int(self.prove(emu=emu))

    def testTruth(self, v1, v2):
        raise Exception('Constraint %s must implement testTruth!' % self.__class__.__name__)

    def isDiscrete(self, emu=None):
        return self._v1.isDiscrete(emu=emu) and self._v2.isDiscrete(emu=emu)

def opose(c1, c2):
    c1.revclass = c2
    c2.revclass = c1

class eq(Constraint):
    operstr = '=='
    def testTruth(self, v1, v2):
        return v1 == v2

class ne(Constraint):
    operstr = '!='
    def testTruth(self, v1, v2):
        return v1 != v2

class le(Constraint):
    operstr = '<='
    def testTruth(self, v1, v2):
        return v1 <= v2

class gt(Constraint):
    operstr = '>'
    def testTruth(self, v1, v2):
        return v1 > v2

class lt(Constraint):
    operstr = '<'
    def testTruth(self, v1, v2):
        return v1 < v2

class ge(Constraint):
    operstr = '>='
    def testTruth(self, v1, v2):
        return v1 >= v2

class UNK(Constraint): operstr = 'UNK'
class NOTUNK(Constraint): operstr = '!UNK'

# Create our oposing constraints
opose(ne, eq)
opose(le, gt)
opose(lt, ge)
opose(UNK,NOTUNK)

