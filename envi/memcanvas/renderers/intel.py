"""
Render intel opcodes...
"""

import envi
import envi.memcanvas as e_canvas

class IntelOpcodeRenderer(e_canvas.MemoryRenderer):

    def __init__(self):
        import envi.intel as e_intel
        self.arch = e_intel.IntelModule()

    def renderRegister(self, mcanv, regid):
        name = self.arch.getRegisterName(regid)
        mcanv.addNameText(name, typename="registers")

    def renderOperand(self, mcanv, va, op, oidx):

        oper = op.opers[oidx]

        if oper.mode == envi.OM_IMMEDIATE:
            dest = oper.imm
            if self.arch.isBranch(op) or self.arch.isCall(op):
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

    def addrToName(self, mcanv, va):
        sym = mcanv.syms.getSymByAddr(va)
        if sym != None:
            name = repr(sym)
        else:
            name = self.arch.pointerString(va)
        return name

    def renderOpcode(self, mcanv, va, op):
        mtag = mcanv.getNameTag(op.mnem, typename="mnemonic")
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

