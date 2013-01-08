import hashlib

import vstruct
import envi.bits as e_bits

def evalSymbolik(reprstr):
    '''
    Take a previously repr'd symboliks object and eval it
    back into objecthood.

    Example:
        x = "o_add(Var('eax'), 3)"
        symobj = evalSymbolik(x)
    '''
    return eval(reprstr, globals(), {})

class ExpressionHelper:

    def __init__(self):
        self.d = {}
        self.d['mem'] = self

    def parseExpression(self, expr):
        return eval(expr, globals(), self)

    def __getitem__(self, name):
        r = self.d.get(name)
        if r != None:
            return r
        return Var(name)

    def __getslice__(self, symaddr, symsize):
        return Mem(symaddr, symsize)

t = ExpressionHelper()
def exprSymbolik(expr):
    return t.parseExpression(expr)

def frobSymbol(thing):
    '''
    Translate native python types to symbolik types
    if we know how...
    '''
    ttype = type(thing)
    if ttype in (long, int):
        return Const(thing)

    if ttype in (str,): # Unicode?
        return exprSymbolik(thing)

    return thing

def getSymbolikImport(vw, impname):
    '''
    Resolve (hopefully) and return a symbolik import emulation
    function for the given import by name.
    '''
    modbase = vw.getMeta('SymbolikImportEmulation')
    if modbase == None:
        return None

    nameparts = impname.split('.')

    # FIXME *.malloc!
    # FIXME cache

    mod = vw.loadModule(modbase)
    return vstruct.resolve(mod, nameparts)

class SymbolikBase:

    def __init__(self):
        pass

    def __add__(self, other):
        return o_add(self, other)

    def __iadd__(self, other):
        return o_add(self, other)

    def __sub__(self, other):
        return o_sub(self, other)

    def __isub__(self, other):
        return o_sub(self, other)

    def __xor__(self, other):
        return o_xor(self, other)

    def __ixor__(self, other):
        return o_xor(self, other)

    def __lshift__(self, count):
        return o_lshift(self, count)

    def __ilshift__(self, count):
        return o_lshift(self, count)

    def __rshift__(self, count):
        return o_rshift(self, count)

    def __irshift__(self, count):
        return o_rshift(self, count)

    def __or__(self, other):
        return o_or(self, other)

    def __ior__(self, other):
        return o_or(self, other)

    def __and__(self, other):
        return o_and(self, other)

    def __iand__(self, other):
        return o_and(self, other)

    def __mod__(self, other):
        return o_mod(self, other)

    def __imod__(self, other):
        return o_mod(self, other)

    def __mul__(self, other):
        return o_mul(self, other)

    def __imul__(self, other):
        return o_mul(self, other)

    def __div__(self, other):
        return o_div(self, other)

    def __idiv__(self, other):
        return o_div(self, other)

    def __pow__(self, other):
        return o_pow(self, other)

    def __eq__(self, other):
        if other == None:
            return False

        if type(other) in (int, long):
            return self.solve() == other

        return self.solve() == other.solve()

    # FIXME more comparitors!

    def solve(self, emu=None):
        '''
        Produce a reproducable answer based on the current state if provided.
        '''
        raise Exception('%s *must* implement solve(emu=emu)!' % self.__class__.__name__)

    def reduce(self, emu=None):
        '''
        Algebraic reduction and operator folding where possible. (INLINE!)
        '''
        raise Exception('%s *must* implement reduce(emu=emu)!' % self.__class__.__name__)

    def update(self, emu):
        '''
        Return an updated representation for this symbolik state based on the given
        emulator.  This is *NOT* inline.
        '''
        raise Exception('%s *must* implement update(emu)!' % self.__class__.__name__)

    def getWidth(self):
        #FIXME width!
        #FIXME perhaps default width from sym solver ctx?
        return 4

    def isDiscrete(self, emu=None):
        '''
        Returns True if the given symbolik (from here down) does *not* depend on
        any variables or runtime values.
        '''
        raise Exception('Symbolik %s *must* implement isDiscrete(emu=emu)!' % self.__class__.__name__)

    def walkTree(self, cb, ctx=None):
        raise Exception('%s *must* implement walkTree()!' % (self.__class__.__name__))

    # FIXME getVars() method!

class cnot(SymbolikBase):
    '''
    Mostly used to wrap the reverse of a contraint which is based on
    a variable.
    '''
    def __init__(self, v1):
        SymbolikBase.__init__(self)
        self._v1 = v1

    def walkTree(self, cb, ctx=None):
        self._v1.walkTree(cb, ctx=ctx)
        self._v1 = cb(self._v1, ctx)

    def __repr__(self):
        return 'cnot( %s )' % (repr(self._v1) )

    def __str__(self):
        return 'not( %s )' % (str(self._v1) )

    def solve(self, emu=None):
        return int( not bool( self._v1.solve(emu=emu)) )

    def isDiscrete(self, emu=None):
        return self._v1.isDiscrete(emu=emu)

    def update(self, emu):
        # FIXME dependancy loop...
        from vivisect.symboliks.constraints import Constraint
        v1 = self._v1.update(emu=emu)
        if isinstance(v1, Constraint):
            return v1.reverse()
        return cnot(v1)

    def reduce(self, emu=None):
        # FIXME dependancy loop...
        from vivisect.symboliks.constraints import Constraint
        self._v1 = self._v1.reduce(emu=emu)
        if isinstance( self._v1, Constraint):
            return self._v1.reverse()
        if isinstance( self._v1, cnot):
            return self._v1._v1
        return self

class Call(SymbolikBase):
    '''
    This represents the return value of an instance of a call to
    a function.
    '''
    def __init__(self, funcsym, argsyms=()):
        SymbolikBase.__init__(self)
        self.funcsym = funcsym
        self.argsyms = argsyms

    def walkTree(self, cb, ctx=None):
        self.funcsym.walkTree(cb, ctx=ctx)
        x = [ arg.walkTree(cb, ctx=ctx) for arg in self.argsyms]

        self.funcsym = cb(self.funcsym, ctx)
        self.argsyms = [ cb(arg, ctx) for arg in self.argsyms ]

    def __str__(self):
        args = ','.join( [ str(sym) for sym in self.argsyms ] )
        return '%s(%s)' % (self.funcsym, args)

    def __repr__(self):
        return 'Call(%s, argsyms=%s)' % (repr(self.funcsym), repr(self.argsyms))

    def reduce(self, emu=None):
        self.funcsym = self.funcsym.reduce(emu=emu)
        self.argsyms = [ x.reduce(emu=emu) for x in self.argsyms ]
        return self

    def solve(self, emu=None):
        sbase = self.funcsym.solve(emu=emu)
        for arg in self.argsyms:
            sbase ^= arg.solve(emu=emu)
        return sbase

    def update(self, emu):
        funcsym = self.funcsym.update(emu)
        argsyms = [ x.update(emu) for x in self.argsyms ]
        return Call(funcsym, argsyms)

    def isDiscrete(self, emu=None):
        # FIXME resolve for the function!  it could be!
        return False

class Mem(SymbolikBase):
    '''
    This is effectivly a cop-out for symbolic states read in from
    memory which has not been initialized yet.
    '''

    def __init__(self, symaddr, symsize):
        SymbolikBase.__init__(self)
        self.symaddr = frobSymbol(symaddr)
        self.symsize = frobSymbol(symsize)

    def walkTree(self, cb, ctx=None):
        self.symaddr.walkTree(cb, ctx=ctx)
        self.symsize.walkTree(cb, ctx=ctx)
        self.symaddr = cb(self.symaddr, ctx)
        self.symsize = cb(self.symsize, ctx)

    def __repr__(self):
        return 'Mem(%s, %s)' % (repr(self.symaddr), repr(self.symsize))

    def __str__(self):
        return 'mem[%s:%s]' % (str(self.symaddr), str(self.symsize))

    def reduce(self, emu=None):
        self.symaddr = self.symaddr.reduce(emu=emu)
        self.symsize = self.symsize.reduce(emu=emu)
        return self

    def update(self, emu):
        symaddr = self.symaddr.update(emu)
        symsize = self.symsize.update(emu)

        # If the emulator (or is viv) knows about us, update to his...
        ret = emu.readSymMemory(symaddr, symsize)
        if ret != None:
            return ret

        return Mem(symaddr, symsize)

    def isDiscrete(self, emu=None):
        # non-updated memory locations are *never* discrete
        return False

    def solve(self, emu=None):
        addrval = self.symaddr.solve(emu=emu)
        sizeval = self.symsize.solve(emu=emu)
        # FIXME higher entropy!
        return hash(str(addrval)) & 0xffffffff

    def getWidth(self):
        # FIXME should we do something about that?
        return self.symsize.solve()

class Var(SymbolikBase):

    def __init__(self, name, width=4):
        SymbolikBase.__init__(self)
        self.name = name
        self.width = width
        self.mask = e_bits.u_maxes[width]

    def walkTree(self, cb, ctx=None):
        pass # We have no kids!

    def __repr__(self):
        return 'Var("%s", width=%d)' % (self.name,self.width)

    def __str__(self):
        return self.name

    def solve(self, emu=None):

        name = self.name
        if emu != None:
            # Is this really the only one that uses the emu?
            name = name + emu.getRandomSeed()

        return hash(hashlib.md5(name).hexdigest()) & 0xffffffff

    def update(self, emu):
        ret = emu.getSymVariable(self.name, create=False)
        if ret != None:
            return ret
        return Var(self.name, width=self.width)

    def reduce(self, emu=None):
        return self

    def getWidth(self):
        return self.width

    def isDiscrete(self, emu=None):
        return False

class Const(SymbolikBase):

    def __init__(self, value):
        SymbolikBase.__init__(self)
        self.value = value

    def walkTree(self, cb, ctx=None):
        pass # We have no kids!

    def solve(self, emu=None):
        return self.value

    def reduce(self, emu=None):
        return self

    def __repr__(self):
        return 'Const(0x%.8x)' % self.value

    def __str__(self):
        if self.value > 4096:
            return '0x%.8x' % self.value
        return str(self.value)

    def getWidth(self):
        return e_bits.intwidth(self.value)

    def update(self, emu):
        # const's are immutable... don't copy...
        return self

    def isDiscrete(self, emu=None):
        return True

class Operator(SymbolikBase):
    '''
    A class representing an algebraic operator being carried out
    on two symboliks...
    '''
    revclass = None
    operstr = None
    def __init__(self, v1, v2):
        SymbolikBase.__init__(self)
        self._v1 = frobSymbol(v1)
        self._v2 = frobSymbol(v2)

    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, repr(self._v1), repr(self._v2))

    def __str__(self):
        if self.operstr == None:
            raise Exception('Operators *must* set operstr')
        return '(%s %s %s)' % (str(self._v1), self.operstr, str(self._v2))

    def walkTree(self, cb, ctx=None):
        self._v1.walkTree(cb, ctx=ctx)
        self._v2.walkTree(cb, ctx=ctx)
        self._v1 = cb(self._v1, ctx)
        self._v2 = cb(self._v2, ctx)

    def reduce(self, emu=None):

        v1 = self._v1.reduce(emu=emu)
        v1val = v1.solve(emu=emu)
        v2 = self._v2.reduce(emu=emu)
        v2val = v2.solve(emu=emu)

        # All operators should check for discrete...
        if v1.isDiscrete() and v2.isDiscrete():
            return Const(self.solve(emu=emu))

        ret = self._op_reduce(v1, v1val, v2, v2val, emu)
        if ret != None:
            return ret

        self._v1 = v1
        self._v2 = v2
        return self

    def update(self, emu):
        v1 = self._v1.update(emu)
        v2 = self._v2.update(emu)
        return self.__class__(v1, v2)

    def _op_reduce(self, v1, v1val, v2, v2val, emu):
        # Override this to do per operator special reduction
        return None

    def isDiscrete(self, emu=None):
        return self._v1.isDiscrete(emu=emu) and self._v2.isDiscrete(emu=emu)

def reduce_addsub(oper):
    '''
    Join up any nested addition / subtraction so we can just
    calculate the total...
    '''

    oper = Operator.reduce(oper)

    toadd = []
    tosub = []

    ctot = 0
    todo = [oper,]
    while len(todo):

        o = todo.pop()

        # Ok, first of all, if a given chunk is totally discrete
        # lets just resolve it and modify ctot...
        if o.isDiscrete():
            ctot += o.solve()
            continue

        if isinstance(o, o_add):
            if isinstance(o._v1, o_add):
                todo.append(o._v1)
            elif isinstance(o._v1, o_sub):
                todo.append(o._v1)
            else:
                toadd.append(o._v1)

            if isinstance(o._v2, o_add):
                todo.append(o._v2)
            elif isinstance(o._v2, o_sub):
                todo.append(o._v2)
            else:
                toadd.append(o._v2)

        if isinstance(o, o_sub):
            if isinstance(o._v1, o_add):
                todo.append(o._v1)
            elif isinstance(o._v1, o_sub):
                todo.append(o._v1)
            else:
                toadd.append(o._v1)

            if isinstance(o._v2, o_add):
                todo.append(o._v2)
            elif isinstance(o._v2, o_sub):
                todo.append(o._v2)
            else:
                tosub.append(o._v2)

    sym = None
    for a in toadd:

        if a.isDiscrete():
            ctot += a.solve()
            continue

        if sym == None:
            sym = a
        else:
            sym = o_add(sym, a)
        #if isinstance(a, Const):
            #ctot += a.value
        #else:
            #if sym == None:
                #sym = a
            #else:
                #sym = o_add(sym, a)

    for s in tosub:
        if s.isDiscrete():
            ctot -= s.solve()
            continue
        if sym == None:
            sym = s
        else:
            sym = o_sub(sym, s)
        #if isinstance(s, Const):
            #ctot -= s.value
        #else:
            #if sym == None:
                #sym = s
            #else:
                #sym = o_sub(sym, s)

    if sym == None:
        # FIXME unsigned!
        return Const(ctot)

    if ctot > 0:
        return o_add(sym, ctot)
    elif ctot < 0:
        return o_sub(sym, abs(ctot))

    return sym

class o_add(Operator):
    operstr = '+'

    def reduce(self, emu=None):
        return reduce_addsub(self)

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 + v2

class o_sub(Operator):
    operstr = '-'

    def reduce(self, emu=None):
        return reduce_addsub(self)

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 - v2

class o_xor(Operator):
    operstr = '^'

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 ^ v2

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        if v1val == v2val:
            return Const(0)

        if v1val == 0:
            return v2

        if v2val == 0:
            return v1

class o_and(Operator):

    operstr = '&'

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        v1width = v1.getWidth()
        v2width = v2.getWidth()

        v1umax = e_bits.u_maxes[v1width]
        v2umax = e_bits.u_maxes[v2width]

        # Mask them down to their real sizes...
        v1val &= v1umax
        v2val &= v2umax

        if v2val & v1umax == v1umax:
            return v1

        if v1val & v2umax == v2umax:
            return v2

        if v1val == 0:
            return Const(0)

        if v2val == 0:
            return Const(0)

        if v1val == v2val:
            return v1

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 & v2

class o_or(Operator):

    operstr = '|'

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        v1width = v1.getWidth()
        v1umax = e_bits.u_maxes[v1width]

        v2width = v2.getWidth()
        v2umax = e_bits.u_maxes[v2width]

        # Mask them down to their real sizes...
        v1val &= v1umax
        v2val &= v2umax

        if v1val == 0xffffffff: # FIXME width!
            return Const(0xffffffff)

        if v2val == 0xffffffff:
            return Const(0xffffffff)

        if v1val == 0:
            return v2

        if v2val == 0:
            return v1

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 | v2

class o_mul(Operator):

    operstr = '*'

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        if v1val == 0:
            return Const(0)

        if v2val == 0:
            return Const(0)

        if v1val == 1:
            return v2

        if v2val == 1:
            return v1

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 * v2

class o_div(Operator):
    operstr = '/'

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        if v1val == 0:
            return Const(0)

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 / v2

class o_mod(Operator):

    operstr = '%'

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        if v1val == 0:
            return Const(0)

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 % v2

class o_lshift(Operator):
    operstr = '<<'

    def reduce(self, emu=None):
        v1 = self._v1.reduce(emu=emu)
        v2 = self._v2.reduce(emu=emu)

        if v2 == 0:
            return v1

        if v1 == 0:
            return Const(0)

        return o_lshift(v1, v2)

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        if v2val == 0:
            return v1

        if v1val == 0:
            return Const(0)

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 << v2

class o_rshift(Operator):

    operstr = '>>'

    def _op_reduce(self, v1, v1val, v2, v2val, emu):

        if v2val == 0:
            return v1

        if v1val == 0:
            return Const(0)

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 << v2

class o_pow(Operator):

    operstr = '**'
    def _op_reduce(self, v1, v1val, v2, v2val, emu):
        # for starters, anything to the 1th is itself...
        if v2val == 1:
            return v1

        # Anything to the 0th is 1...
        if v2val == 0:
            return Const(1)

        if v1val == 1:
            return Const(1)

    def solve(self, emu=None):
        v1 = self._v1.solve(emu=emu)
        v2 = self._v2.solve(emu=emu)
        return v1 ** v2

