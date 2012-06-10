import sys

import envi
import envi.bits as e_bits
import envi.registers as e_registers
import envi.archs.i386 as e_i386

import vivisect.symboliks.analysis as vsym_analysis
import vivisect.symboliks.callconv as vsym_callconv
import vivisect.symboliks.emulator as vsym_emulator
import vivisect.symboliks.translator as vsym_trans

from vivisect.const import *
from vivisect.symboliks.common import *
from vivisect.symboliks.constraints import *

# Initial stack pointer for all i386SymbolikFunctionEmulators.
initial_esp = 0xbfbff000

def getSegmentSymbol(op):
    if op.prefixes & e_i386.PREFIX_CS:
        return Var('cs')
    if op.prefixes & e_i386.PREFIX_SS:
        return Var('ss')
    if op.prefixes & e_i386.PREFIX_DS:
        return Var('ds')
    if op.prefixes & e_i386.PREFIX_ES:
        return Var('es')
    if op.prefixes & e_i386.PREFIX_FS:
        return Var('fs')
    if op.prefixes & e_i386.PREFIX_GS:
        return Var('gs')

# Our symbolik calling conventions...
class StdCall(vsym_callconv.SymbolikCallingConvention):

    def setSymbolikArgs(self, emu, argv):
        for i in xrange(len(argv)):
            soffset = 4 + (4*i)
            arg = frobSymbol(argv[i])
            emu.writeSymMemory(Const(initial_esp+soffset), arg)

    def getSymbolikArgs(self, emu, argv, update=False):
        argc = len(argv)
        offsets = [ x*4 for x in range(argc) ]
        esp = Var('esp')
        args = [ Mem(esp+off, 4) for off in offsets ]
        if update:
            args = [ x.update(emu) for x in args ]
        return args

    def setSymbolikReturn(self, emu, sym, argv):
        emu.setSymVariable('eax', sym)
        esp = emu.getSymVariable('esp')
        sdelta = 4 * len(argv)
        emu.setSymVariable('esp', esp + sdelta)

    def getSymbolikReturn(self, emu):
        return emu.getSymVariable('eax')

class Cdecl(StdCall):

    def setSymbolikReturn(self, emu, sym, argv):
        emu.setSymVariable('eax', sym)

cdecl = Cdecl()

class ThisCall(StdCall):

    def getSymbolikArgs(self, emu, argv, update=False):
        args = [ Var('ecx'), ]
        esp = Var('esp')
        for i,aname in enumerate(argv[1:]):
            args.append( Mem( esp + (4*i), 4 ) )
        if update:
            args = [ x.update(emu) for x in args ]
        return args

    def setSymbolikReturn(self, emu, sym, argv):
        emu.setSymVariable('eax', sym)
        esp = emu.getSymVariable('esp')
        sdelta = 4 * (len(argv)-1)
        emu.setSymVariable('esp', esp + sdelta)

class i386SymbolikFunctionEmulator(vsym_analysis.SymbolikFunctionEmulator):
    '''
    A symbolik function emulator for i386 based code.
    '''
    def __init__(self, vw):
        vsym_analysis.SymbolikFunctionEmulator.__init__(self, vw)
        self.setSymVariable('esp', initial_esp)
        self.addCallingConvention('cdecl', Cdecl())
        self.addCallingConvention('stdcall', StdCall())
        self.addCallingConvention('thiscall', ThisCall())
        # FIXME possibly decide this by platform/format?
        self.addCallingConvention(None, Cdecl())

        self.addFunctionCallback('ntdll.seh3_prolog', self._seh3_prolog)
        self.addFunctionCallback('ntdll.seh3_epilog', self._seh3_epilog)

        #self.writeSymMemory( Mem(Var('fs') + 292, 4)

#mem[(mem[(fs + 292):4] + 320):1]

    def _seh3_prolog(self, emu, scopetable, localsize):

        esp = emu.getSymVariable('esp')

        emu.writeSymMemory( esp+4,  emu.getSymVariable('ebp'))
        emu.writeSymMemory( esp,    scopetable)
        emu.writeSymMemory( esp-4,  Var('ntdll.seh3_handler', 4))     # push
        emu.writeSymMemory( esp-8,  Var('saved_seh3_scopetable', 4))  # push
        emu.writeSymMemory( esp-12, emu.getSymVariable('ebx'))
        emu.writeSymMemory( esp-16, emu.getSymVariable('esi'))
        emu.writeSymMemory( esp-20, emu.getSymVariable('edi'))
        emu.setSymVariable( 'esp',  (esp - 20) - localsize)
        emu.setSymVariable( 'ebp',  (esp+4))

        return scopetable

    def _seh3_epilog(self, emu, edi, esi, ebx):
        esp = emu.getSymVariable('esp')
        # FIXME do seh restore...
        emu.setSymVariable('edi', edi)
        emu.setSymVariable('esi', esi)
        emu.setSymVariable('ebx', ebx)
        ebp = emu.getSymVariable('ebp')
        savedbp = emu.readSymMemory(ebp, Const(4))
        emu.setSymVariable('ebp', savedbp)
        emu.setSymVariable('esp', ebp+4)

    def getApiModule(self):

        if self._sym_vw.getMeta('Platform') == 'Windows':

            return self._sym_vw.loadModule('vivisect.impemu.api.windows.i386')

    def isLocalMemory(self, symaddr, solvedval=None):
        '''
        Determine if the given virtual address should be considered a "local"
        memory access...
        '''
        if solvedval == None:
            solvedval = symaddr.solve(emu=self)
        return (solvedval & 0xffffc000) == (initial_esp & 0xffffc000)

class i386SymbolikAnalysisContext(vsym_analysis.SymbolikAnalysisContext):

    def getFunctionEmulator(self, fva, args=None):
        emu = i386SymbolikFunctionEmulator(self.vw)
        emu.setupFunctionCall(fva, args=args)
        return emu

    def getTranslator(self):
        return i386SymbolikTranslator(self.vw)

# These must be declared in the symboliks arch module for
# function calling glue to work...
#cdecl = Cdecl()
#default = Cdecl()
#stdcall = StdCall()
#thiscall = ThisCall()

# And the actual translator...
class i386SymbolikTranslator(vsym_trans.SymbolikTranslator):

    def __init__(self, vw):
        vsym_trans.SymbolikTranslator.__init__(self, vw)
        self._reg_ctx = e_i386.i386RegisterContext()

    def getOperAddrObj(self, op, idx):
        oper = op.opers[idx]
        seg = getSegmentSymbol(op)

        if isinstance(oper, e_i386.i386RegMemOper):
            reg = Var(self._reg_ctx.getRegisterName(oper.reg))
            if oper.disp == 0:
                return reg
            if oper.disp > 0:
                return o_add(reg, Const(oper.disp))
            if oper.disp < 0:
                return o_sub(reg, Const(abs(oper.disp)))

        elif isinstance(oper, e_i386.i386SibOper):

            base = None
            if oper.imm != None:
                base = Const(oper.imm)

            if oper.reg != None:
                robj = Var(self._reg_ctx.getRegisterName(oper.reg))
                if base == None:
                    base = robj
                else:
                    base = o_add(base, robj)

            # Base is set by here for sure!
            if oper.index != None:
                robj = Var(self._reg_ctx.getRegisterName(oper.index))
                base = o_add(base, o_mul(robj, Const(oper.scale)))

            if oper.disp != None:
                if oper.disp > 0:
                    base = o_add(base, Const(oper.disp))
                else:
                    base = o_sub(base, Const(abs(oper.disp)))

            return base

        elif isinstance(oper, e_i386.i386ImmMemOper):
            # FIXME plumb more segment awareness!
            if seg:
                return o_add(seg, Const(oper.imm))
            return Const(oper.imm)

    def getOperObj(self, op, idx):
        '''
        Translate the specified operand to a symbol compatable with
        the symbolic translation system.
        '''
        oper = op.opers[idx]
        if oper.isReg():
            return self.getRegObj(oper.reg)

        elif oper.isDeref():
            addrsym = self.getOperAddrObj(op, idx)
            return self.effReadMemory(addrsym, Const(oper.tsize))

        elif oper.isImmed():
            ret = oper.getOperValue(op, self)
            return Const(ret)

        raise Exception('Unknown operand class: %s' % oper.__class__.__name__)

    def setOperObj(self, op, idx, obj):
        '''
        Set the operand to the new symolic object.
        '''
        oper = op.opers[idx]
        if oper.isReg():
            self.setRegObj(oper.reg, obj)
            return

        if oper.isDeref():
            addrsym = self.getOperAddrObj(op, idx)
            return self.effWriteMemory(addrsym, Const(oper.tsize), obj)

        raise 'Umm..... really?'

    def writeMemObj(self, addrsym, sizesym, obj):
        if type(addrsym) in (int,long): addrsym = Const(addrsym)
        if type(sizesym) in (int,long): sizesym = Const(sizesym)
        self.effWriteMemory(addrsym, sizesym, obj)

    def getRegObj(self, regidx):
        ridx = regidx & 0xffff
        rname = self._reg_ctx.getRegisterName(ridx)
        val = Var(rname)
        
        # Translate to meta if needed...
        if ridx != regidx:
            val = self._reg_ctx._xlateToMetaReg(regidx, val)

        return val

    def setRegObj(self, regidx, obj):
        ridx = regidx & 0xffff
        rname = self._reg_ctx.getRegisterName(ridx)

        # Translate to native if needed...
        if ridx != regidx:
            obj = self._reg_ctx._xlateToNativeReg(regidx, obj)
        self.effSetVariable(rname, obj)

    def i_add(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)

        dsize = op.opers[0].tsize
        dmax  = e_bits.s_maxes[dsize]
        ssize = op.opers[1].tsize

        smax, umax = self.__get_dest_maxes(op)

        add = o_add(v1, v2)
        self.setOperObj(op, 0, add)

        #self.effSetVariable('eflags_gt', gt(v1, v2))
        #self.effSetVariable('eflags_lt', lt(v1, v2))
        #self.effSetVariable('eflags_sf', lt(v1, v2))
        #self.effSetVariable('eflags_eq', eq(v1+v2, 0))


    def __get_dest_maxes(self, op):
        tsize = op.opers[0].tsize
        smax = e_bits.s_maxes[tsize]
        umax = e_bits.u_maxes[tsize]
        return smax, umax

    def i_adc(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)

        # FIXME this is wrong!
        if self.getFlag(EFLAGS_CF):
            v2 = v2 + 1

        self.effSetVariable('eflags_zf', eq(add, Const(0)))
        self.setOperObj(op, 0, v1 + v2)

    def i_call(self, op):

        # For now, calling means finding which of our symbols go in
        # and logging what comes out.
        targ = self.getOperObj(op, 0)
        print repr(targ)
        self.effFofX(targ)
        return

    def i_cld(self, op):
        self.effSetVariable('eflags_df', Const(0))

    def i_cmpxchg(self, op):

        # FIXME CATASTROPHIC THIS CONTAINS BRANCHING LOGIC STATE!
        # FOR NOW WE JUST DO IT WITHOUT ANY CONDITIONAL
        x = self.getOperObj(op, 0)
        y = self.getOperObj(op, 1)
        self.effSetVariable('i386_xchg_tmp', x)
        self.setOperObj(op, 0, y)
        self.setOperObj(op, 1, Var('i386_xchg_tmp'))

    def i_cmp(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        res = o_sub(v1, v2)
        self.effSetVariable('eflags_cf', gt(v2, v1)) # 
        self.effSetVariable('eflags_gt', gt(v1, v2)) # v1 - v2 > 0 :: v1 > v2
        self.effSetVariable('eflags_lt', lt(v1, v2)) # v1 - v2 < 0 :: v1 < v2
        self.effSetVariable('eflags_sf', lt(v1, v2)) # v1 - v2 < 0 :: v1 < v2
        self.effSetVariable('eflags_eq', eq(v1, v2)) # v1 - v2 == 0 :: v1 == v2

    def i_dec(self, op):
        v1 = self.getOperObj(op, 0)
        one = Const(1)

        sub = o_sub(v1, one)

        self.effSetVariable('eflags_gt', gt(v1, one)) # v1 - 1 > 0 :: v1 > 1
        self.effSetVariable('eflags_lt', lt(v1, one)) # v1 - 1 < 0 :: v1 < 1
        self.effSetVariable('eflags_sf', lt(v1, one)) # v1 - 1 < 0 :: v1 < 1
        self.effSetVariable('eflags_eq', eq(v1, one)) # v1 - 1 == 0 :: v1 == 1

        self.setOperObj(op, 0, sub)

    def i_div(self, op):
        oper = op.opers[0]
        divbase = self.getOperObj(op, 0)
        if oper.tsize == 1:
            ax = self._reg_ctx._xlateToNativeReg(e_i386.REG_AX, Var('eax'))
            quot = ax / divbase
            rem  = ax % divbase
            self.effSetVariable('eax', (quot << 8) + rem)

        elif oper.tsize == 2:
            raise Exception("16 bit divide needs help!")

        elif oper.tsize == 4:
            eax = Var('eax')
            edx = Var('edx')

            #FIXME 16 bit over-ride
            tot = (edx << 32) + eax
            quot = tot / divbase
            rem = tot % divbase
            self.effSetVariable('eax', quot)
            self.effSetVariable('edx', rem)

            #FIXME maybe we need a "check exception" effect?

        else:
            raise envi.UnsupportedInstruction(self, op)


    def i_and(self, op):

        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)

        obj = o_and(v1, v2)

        u = UNK(v1, v2)
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', lt(obj, Const(0))) # v1 & v2 < 0
        self.effSetVariable('eflags_eq', eq(obj, Const(0))) # v1 & v2 == 0

        self.setOperObj(op, 0, obj)

    def i_or(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        obj = o_or(v1, v2)
        u = UNK(v1, v2)
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', lt(obj, Const(0))) # v1 | v2 < 0
        self.effSetVariable('eflags_eq', eq(obj, Const(0))) # v1 & v2 == 0
        self.setOperObj(op, 0, obj)

    def i_hlt(self, op):
        # Nothing to do symbolically....
        pass

    def i_inc(self, op):
        v1 = self.getOperObj(op, 0)
        obj = o_add(v1, 1)
        u = UNK(obj, Const(1))
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', u)
        self.effSetVariable('eflags_eq', u)
        self.setOperObj(op, 0, obj)

    def i_int3(self, op):
        # FIXME another "test for exception" effect vote!
        pass

    def i_imul(self, op):
        ocount = len(op.opers)
        if ocount == 2:
            dst = self.getOperObj(op, 0)
            src = self.getOperObj(op, 1)
            self.setOperObj(op, 0, dst * src)
            print 'FIXME IMUL FLAGS'

        elif ocount == 3:
            dst = self.getOperObj(op, 0)
            src1 = self.getOperObj(op, 1)
            src2 = self.getOperObj(op, 2)
            self.setOperObj(op, 0, src1 * src2)
            print 'FIXME IMUL FLAGS'
            #res = src1 * src2
            #sof = e_bits.is_unsigned_carry(res, dsize)
            #self.setFlag(EFLAGS_CF, sof)
            #self.setFlag(EFLAGS_OF, sof)

    def i_jmp(self, op):
        pass # Nothing to do symbolically, codeflow must 
        #return ((self.getOperObj(op, 0), None), )

    # We include all the possible Jcc names just in case somebody
    # gets hinkey with the disassembler.
    def i_ja(self, op):
        return self.__cond_jmp(op, Var('eflags_gt'))

    def i_jae(self, op):
        return self.__cond_jmp(op, cnot(Var('eflags_lt')))

    def i_jb(self, op):
        return self.__cond_jmp(op, Var('eflags_lt'))

    def i_jbe(self, op):
        return self.__cond_jmp(op, cnot(Var('eflags_lt')))

    def i_jc(self, op):
        print 'FIXME who set cf?'
        return self.__cond_jmp(op, Var('eflags_cf'))
        #if self.cond_c():    return self.getOperValue(op, 0)

    def i_jecxz(self, op):
        return self.__cond_jmp(op, eq(Var('ecx'), Const(0)))

    def i_je(self, op):
        return self.__cond_jmp(op, Var('eflags_eq'))

    def __cond_jmp(self, op, cond):
        # Construct the tuple for the conditional jump
        return (
                ( self.getOperObj(op, 0), cond ),
                ( Const(op.va + len(op)), cnot(cond)), 
               )

    def i_jg(self, op):
        return self.__cond_jmp(op, Var('eflags_gt'))

    def i_jge(self, op):
        return self.__cond_jmp(op, cnot(Var('eflags_lt')))

    def i_jl(self, op):
        return self.__cond_jmp(op, Var('eflags_lt'))

    def i_jle(self, op):
        return self.__cond_jmp(op, cnot(Var('eflags_gt')))

    i_jna = i_jbe
    i_jnae = i_jb
    i_jnb = i_jae
    i_jnbe = i_ja
    i_jnc = i_jae

    def i_jne(self, op):
        return self.__cond_jmp(op, cnot(Var('eflags_eq')))

    i_jng = i_jle
    i_jnge = i_jl
    i_jnl = i_jge
    i_jnle = i_jg

    #def i_jno(self, op):
        #if self.cond_no():   return self.getOperValue(op, 0)

    #def i_jnp(self, op):
        #if self.cond_np():   return self.getOperValue(op, 0)

    def i_jns(self, op):
        return self.__cond_jmp(op, cnot(Var('eflags_sf')))

    i_jnz = i_jne

    #def i_jo(self, op):
        #if self.cond_o():    return self.getOperValue(op, 0)

    #def i_jp(self, op):
        #if self.cond_p():    return self.getOperValue(op, 0)

    #i_jpe = i_jp
    #i_jpo = i_jnp

    def i_js(self, op):
        return self.__cond_jmp(op, Var('eflags_sf'))

    i_jz = i_je

    def i_lea(self, op):
        obj = self.getOperAddrObj(op, 1)
        self.setOperObj(op, 0, obj)

    def i_leave(self, op):
        self.effSetVariable('esp', Var('ebp'))
        self.effSetVariable('ebp', Mem(Var('esp'), Const(4)))
        self.effSetVariable('esp', o_add(Var('esp'), Const(4)))

    def i_neg(self, op):
        obj = self.getOperObj(op, 0)
        print 'FIXME REVIEW NEG'
        self.setOperObj(op, 0, o_sub(Const(0), obj))

    def i_nop(self, op):
        pass

    def i_not(self, op):
        v1 = self.getOperObj(op, 0)
        v1 ^= e_bits.u_maxes[v1.getWidth()]
        self.setOperObj(op, 0, v1)

    def i_push(self, op):
        v1 = self.getOperObj(op, 0)
        esp = self.getRegObj(e_i386.REG_ESP)
        self.effSetVariable('esp', esp-4)
        # NOTE: we do the write after the set, so there is no need
        # to write to esp - 4...
        self.writeMemObj(Var('esp'), 4, v1)

    def i_pushad(self, op):
        esp = self.getRegObj(e_i386.REG_ESP)
        self.writeMemObj(esp - 4, 4, self.getRegObj(e_i386.REG_EAX))
        self.writeMemObj(esp - 8, 4, self.getRegObj(e_i386.REG_ECX))
        self.writeMemObj(esp - 12, 4, self.getRegObj(e_i386.REG_EDX))
        self.writeMemObj(esp - 16, 4, self.getRegObj(e_i386.REG_EBX))
        self.writeMemObj(esp - 20, 4, esp)
        self.writeMemObj(esp - 24, 4, self.getRegObj(e_i386.REG_EBP))
        self.writeMemObj(esp - 28, 4, self.getRegObj(e_i386.REG_ESI))
        self.writeMemObj(esp - 32, 4, self.getRegObj(e_i386.REG_EDI))
        # FIXME re-order these!
        self.effSetVariable('esp', esp - 32)

    def i_pushfd(self, op):
        esp = self.getRegObj(e_i386.REG_ESP)
        eflags = self.getRegObj(e_i386.REG_EFLAGS)
        self.effSetVariable('esp', esp - 4)
        self.writeMemObj(Var('esp'), 4, eflags)

    def i_pop(self, op):
        self.setOperObj(op, 0, Mem(Var('esp'), Const(4)))
        self.effSetVariable('esp', Var('esp') + 4)

    def i_popad(self, op):
        esp = self.getRegObj(e_i386.REG_ESP)
        self.effSetVariable('edi', Mem(esp, 4))
        self.effSetVariable('esi', Mem(esp + 4, 4))
        self.effSetVariable('ebp', Mem(esp + 8, 4))
        self.effSetVariable('ebx', Mem(esp + 16, 4))
        self.effSetVariable('edx', Mem(esp + 20, 4))
        self.effSetVariable('ecx', Mem(esp + 24, 4))
        self.effSetVariable('eax', Mem(esp + 28, 4))
        self.effSetVariable('esp', esp + 32)

    def i_pxor(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        obj = o_xor(v1, v2)
        u = UNK(v1, v2)
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', lt(obj, Const(0))) # v1 & v2 < 0
        self.effSetVariable('eflags_eq', eq(obj, Const(0))) # v1 & v2 == 0
        self.setOperObj(op, 0, obj)

    def i_ret(self, op):
        self.effSetVariable('eip', Mem(Var('esp'), Const(4)))
        esp = Var('esp')
        esp += 4
        if len(op.opers):
            esp += self.getOperObj(op, 0)
        self.effSetVariable('esp', esp)

    #def i_ror(self, op):
        #v1 = self.getOperObj(op, 0)
        #v2 = self.getOperObj(op, 1)

    def i_sar(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)

        # Arithmetic shifts are multiplies and divides!
        res = o_div(v1, o_pow(Const(2), v2))

        u = UNK(v1, v2)
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', lt(res, Const(0))) # v1 | v2 < 0
        self.effSetVariable('eflags_eq', eq(res, Const(0))) # v1 & v2 == 0

        self.setOperObj(op, 0, res)

    def i_sbb(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        obj = o_sub(v1, v2) # FIXME borrow!
        self.effSetVariable('eflags_gt', gt(v1, v2)) # v1 - v2 > 0 :: v1 > v2
        self.effSetVariable('eflags_lt', lt(v1, v2)) # v1 - v2 < 0 :: v1 < v2
        self.effSetVariable('eflags_sf', lt(v1, v2)) # v1 - v2 < 0 :: v1 < v2
        self.effSetVariable('eflags_eq', eq(v1, v2)) # v1 - v2 == 0 :: v1 == v2
        self.setOperObj(op, 0, v1 - v2)

    def i_setnz(self, op):
        self.setOperObj(op, 0, cnot(Var('eflags_eq')))

    def i_setz(self, op):
        self.setOperObj(op, 0, Var('eflags_eq'))

    def i_shl(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)

        #if v2.isDiscrete() and v2.solve() > 0xff:
            #v2 = v2 & 0xff

        # No effect (not even flags) if shift is 0
        #if v2.solve() == 0:
            #return

        self.setOperObj(op, 0, v1 << v2)

        u = UNK(v1, v2) # COP OUT FOR NOW...
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', u)
        self.effSetVariable('eflags_eq', u)

    def i_shr(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)

        #if v2.isDiscrete() and v2.solve() > 0xff:
            #v2 = v2 & 0xff

        self.setOperObj(op, 0, v1 >> v2)

        u = UNK(v1, v2) # COP OUT FOR NOW...
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', u)
        self.effSetVariable('eflags_eq', u)

    def i_std(self, op):
        self.effSetVariable('eflags_df', Const(1))

    def i_stosd(self, op):
        #eax = self.getRegObj(e_i386.REG_EAX)
        #edi = self.getRegObj(e_i386.REG_EDI)
        # FIXME omg segments in symboliks?
        #base,size = self.segments[SEG_ES]
        edi = Var('edi')
        self.writeMemObj(edi, Const(4), Var('eax'))
        # FIXME flags?
        #if self.getFlag(e_i386.EFLAGS_DF):
            #edi -= 4
        #else:
            #edi += 4
        print 'FIXME DF IN stosd'
        edi += 4
        self.effSetVariable('edi', edi)

    def i_sub(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        obj = o_sub(v1, v2)
        self.effSetVariable('eflags_gt', gt(v1, v2)) # v1 - v2 > 0 :: v1 > v2
        self.effSetVariable('eflags_lt', lt(v1, v2)) # v1 - v2 < 0 :: v1 < v2
        self.effSetVariable('eflags_sf', lt(v1, v2)) # v1 - v2 < 0 :: v1 < v2
        self.effSetVariable('eflags_eq', eq(v1, v2)) # v1 - v2 == 0 :: v1 == v2
        self.setOperObj(op, 0, obj)

    def i_test(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        obj = o_and(v1, v2)
        u = UNK(v1, v2)

        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', lt(obj, 0)) # ( SF != OF ) ( OF is cleared )

        self.effSetVariable('eflags_sf', lt(obj, Const(0))) # v1 & v2 < 0
        self.effSetVariable('eflags_eq', eq(obj, Const(0))) # v1 & v2 == 0

    def i_mov(self, op):
        o = self.getOperObj(op, 1)
        self.setOperObj(op, 0, o)

    def i_movq(self, op):
        o = self.getOperObj(op, 1)
        self.setOperObj(op, 0, o)

    def i_movsx(self, op):
        dsize = op.opers[0].tsize
        v2 = self.getOperObj(op, 1)
        self.setOperObj(op, 0, v2)

    def i_movzx(self, op):
        v2 = self.getOperObj(op, 1)
        self.setOperObj(op, 0, v2)

    def i_movsd(self, op):
        esi = Var('esi')
        edi = Var('edi')
        mem = Mem(esi, Const(4))
        self.effWriteMemory(edi, Const(4), mem)

        # FIXME *symbolic* flags!
        #if self.getFlag(EFLAGS_DF):
            #esi -= 4
            #edi -= 4

        #else:
            #esi += 4
            #edi += 4
        print 'FIXME how to handle DF bit?'

        self.effSetVariable('esi', esi+4)
        self.effSetVariable('edi', edi+4)

    def i_movsb(self, op):
        esi = Var('esi')
        edi = Var('edi')
        mem = Mem(esi, Const(1))
        self.effWriteMemory(edi, Const(1), mem)
        self.effSetVariable('esi', esi+1)
        self.effSetVariable('edi', edi+1)

    def i_xadd(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        res = o_add(v1, v2)
        self.setOperObj(op, 0, res)
        self.setOperObj(op, 1, v1)
        #self.effSetVariable('eflags_gt', gt(v1, v2))
        #self.effSetVariable('eflags_lt', lt(v1, v2))
        #self.effSetVariable('eflags_sf', lt(v1, v2))
        #self.effSetVariable('eflags_eq', eq(v1+v2, 0))

    def i_xchg(self, op):
        # NOTE: requires using temp var because each asignment occurs
        # seperately. (even though the API makes it look like you've
        # got your pwn copy... ;) )
        x = self.getOperObj(op, 0)
        y = self.getOperObj(op, 1)
        self.effSetVariable('i386_xchg_tmp', x)
        self.setOperObj(op, 0, y)
        self.setOperObj(op, 1, Var('i386_xchg_tmp'))

    def i_xor(self, op):
        v1 = self.getOperObj(op, 0)
        v2 = self.getOperObj(op, 1)
        obj = o_xor(v1, v2)
        u = UNK(v1, v2)
        self.effSetVariable('eflags_gt', u)
        self.effSetVariable('eflags_lt', u)
        self.effSetVariable('eflags_sf', lt(obj, Const(0))) # v1 & v2 < 0
        self.effSetVariable('eflags_eq', eq(obj, Const(0))) # v1 & v2 == 0
        self.setOperObj(op, 0, obj)

