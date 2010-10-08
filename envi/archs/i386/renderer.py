"""
Render intel opcodes...
"""

import envi
import envi.memcanvas as e_canvas

class i386OpcodeRenderer(e_canvas.MemoryRenderer):

    def __init__(self):
        import envi.archs.i386 as e_i386
        # FIXME just inherit one...
        self.arch = e_i386.i386Module()
        self.rctx = e_i386.i386RegisterContext()

    def renderRegister(self, mcanv, regid):
        name = self.rctx.getRegisterName(regid)
        print "ID 0x%.8x %s" % (regid,name)
        mcanv.addNameText(name, typename="registers")

    def renderOperand(self, mcanv, va, op, oidx):

        oper = op.opers[oidx]

        if oper.mode == envi.OM_IMMEDIATE:
            dest = oper.imm
            # All branches/calls for immediates on intel are relative
            if op.iflags & envi.IF_BRANCH:
                dest = va + oper.imm + len(op)

            name = None
            tag = None
            if mcanv.mem.isValidPointer(dest):
                name = self.addrToName(mcanv, dest)
                mcanv.addVaText(name, dest)

            else:
                name = str(dest)
                mcanv.addNameText(name)

        elif oper.mode == envi.OM_REGISTER:
            self.renderRegister(mcanv, oper.reg)

        else:
            # We're in deref types
            if oper.tsize == 1:
                mcanv.addNameText("byte")
                mcanv.addText(" ")

            elif oper.tsize == 2:
                mcanv.addNameText("word")
                mcanv.addText(" ")

            elif oper.tsize == 4:
                mcanv.addNameText("dword")
                mcanv.addText(" ")

            elif oper.tsize == 8:
                mcanv.addNameText("qword")
                mcanv.addText(" ")

            mcanv.addText("[")

            if oper.mode == envi.OM_IMMMEM:

                name = self.addrToName(mcanv, oper.imm)
                mcanv.addVaText(name, oper.imm)

            elif oper.mode == envi.OM_REGMEM:
                self.renderRegister(mcanv, oper.reg)

            elif oper.mode == envi.OM_SIBMEM:

                if oper.reg != None:
                    self.renderRegister(mcanv, oper.reg)

                if oper.imm != None:
                    name = self.addrToName(mcanv, oper.imm)
                    mcanv.addVaText(name, oper.imm)

                if oper.indexreg != None:
                    mcanv.addText(" + ")
                    self.renderRegister(mcanv, oper.indexreg)
                    if oper.scale > 1:
                        mcanv.addText(" * %d" % oper.scale)

            # In any case... lets close up and do displacement
            if oper.disp != None:
                aval = abs(oper.disp)
                if mcanv.mem.isValidPointer(aval):

                    name = self.addrToName(mcanv, aval)
                    mcanv.addText(" + ")
                    mcanv.addVaText(name, aval)

                else:
                    if oper.disp >= 0:
                        mcanv.addText(" + ")
                    else:
                        mcanv.addText(" - ")
                    mcanv.addNameText(str(aval))

            mcanv.addText("]")

    def addrToName(mcanv, va):
        sym = mcanv.syms.getSymByAddr(va)
        if sym != None:
            return repr(sym)
        return "0x%.8x" % va

    def renderOpcode(self, mcanv, va, op):
        if op.prefixes:
            pfx = self.arch.getPrefixName(op.prefixes)
            if pfx:
                mcanv.addNameText("%s: " % pfx, pfx)

        mcanv.addNameText(op.mnem, typename="mnemonic")
        mcanv.addText(" ")

        imax = len(op.opers)
        lasti = imax - 1
        for i in xrange(imax):
            self.renderOperand(mcanv, va, op, i)
            if i != lasti:
                mcanv.addText(",")

    def renderOpBytes(self, mcanv, bytes, size, maxsize=10):
        hbytes = bytes[:min(maxsize, size)].encode('hex')
        mcanv.addText(hbytes.ljust((maxsize*2)+1))

    def render(self, mcanv, va):

        self.rendSymbol(mcanv, va)
        self.rendVa(mcanv, va)
        mcanv.addText(" ")

        bytes = mcanv.mem.readMemory(va, 16)
        try:
            op = self.arch.makeOpcode(bytes)
            self.renderOpBytes(mcanv, bytes, len(op))
            self.renderOpcode(mcanv, va, op)
            mcanv.addText("\n")
        except envi.InvalidInstruction, e:
            mcanv.addText("%.2x (invalid)\n" % ord(bytes[0]))
            return 1

        return len(op)

