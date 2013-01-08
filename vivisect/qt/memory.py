

import envi.qt as envi_qt
import envi.bits as e_bits
import envi.qt.memory as e_mem_qt
import envi.qt.memcanvas as e_mem_canvas

import vstruct.qt as vs_qt

import vqt.menubuilder as vqt_menu

import vivisect.base as viv_base
import vivisect.renderers as viv_rend
import vivisect.qt.views as viv_q_views
import vivisect.qt.funcgraph as viv_q_funcgraph
import vivisect.qt.funcviews as viv_q_funcviews

from PyQt4          import QtCore, QtGui, QtWebKit
from envi.threads   import firethread
from vivisect.const import *

# FIXME HACK where do these really live?
qt_horizontal   = 1
qt_vertical     = 2

def cmpoffset(x,y):
    return cmp(x[0], y[0])

class VQVivMemoryCanvas(e_mem_canvas.VQMemoryCanvas):

    def __init__(self, *args, **kwargs):
        e_mem_canvas.VQMemoryCanvas.__init__(self, *args, **kwargs)
        self.vw = self.mem
        self._last_sname = None

        self.vqAddHotKey('c', self._hotkey_c)
        self.vqAddHotKey('f', self._hotkey_f)
        self.vqAddHotKey('s', self._hotkey_s)
        self.vqAddHotKey('p', self._hotkey_p)
        self.vqAddHotKey('u', self._hotkey_u)
        self.vqAddHotKey('n', self._hotkey_n)
        self.vqAddHotKey(';', self._hotkey_semi)
        self.vqAddHotKey('S', self._hotkey_S)
        self.vqAddHotKey('ctrl+S', self._hotkey_cS)

        self.vqAddHotKey('U', self._hotkey_U)

    def wheelEvent(self, event):
        frame = self.page().mainFrame()

        sbcur = frame.scrollBarValue(qt_vertical)
        sbmin = frame.scrollBarMinimum(qt_vertical)
        sbmax = frame.scrollBarMaximum(qt_vertical)

        if sbcur == sbmax:

            lastva, lastsize = self._canv_rendvas[-1]
            mapva, mapsize, mperm, mfname = self.vw.getMemoryMap(lastva)
            sizeremain = (mapva + mapsize) - (lastva + lastsize)
            if sizeremain:
                self.renderMemoryAppend(min(sizeremain, 128))

        elif sbcur == sbmin:
            firstva, firstsize = self._canv_rendvas[0]
            mapva, mapsize, mperm, mfname = self.vw.getMemoryMap(firstva)
            #presize = 1
            #prevloc = self.vw.getPrevLocation(firstva)
            #if prevloc:
                #presize = prevloc[1]
            sizeremain = firstva - mapva
            if sizeremain:
                self.renderMemoryPrepend(min(sizeremain, 128))

        return e_mem_canvas.VQMemoryCanvas.wheelEvent(self, event)

    def _hotkey_c(self, canv, key):
        if self._canv_curva:
            self.vw.makeCode(self._canv_curva)

    def _hotkey_f(self, canv, key):
        if self._canv_curva:
            self.vw.makeFunction(self._canv_curva)

    def _hotkey_s(self, canv, key):
        if self._canv_curva:
            self.vw.makeString(self._canv_curva)

    def _hotkey_p(self, canv, key):
        if self._canv_curva:
            self.vw.makePointer(self._canv_curva)

    def _hotkey_u(self, canv, key):
        if self._canv_curva:
            self.vw.makeUnicode(self._canv_curva)

    def _hotkey_U(self, canv, key):
        if self._canv_curva:
            self.vw.delLocation(self._canv_curva)

    def _hotkey_n(self, canv, key):
        if self._canv_curva:
            self._menuRename(self._canv_curva)

    def _hotkey_semi(self, canv, key):
        if self._canv_curva:
            self._menuComment(self._canv_curva)

    def _hotkey_S(self, canv, key):
        if self._canv_curva:
            self._menuMakeStruct(self._canv_curva)

    def _hotkey_cS(self, canv, key):
        if self._canv_curva:
            if self._last_sname != None:
                self.vw.makeStructure(self._canv_curva, self._last_sname)

    def _clearColorMap(self):
        frame = self.page().mainFrame()
        style = frame.findFirstElement('#cmapstyle')
        style.setInnerXml('');

    def _applyColorMap(self, cmap):

        frame = self.page().mainFrame()
        style = frame.findFirstElement('#cmapstyle')

        rows = []
        for va,color in cmap.items():
            rows.append('.va_0x%.8x { color: #000000; background-color: %s }' % (va, color))

        style.setInnerXml('\n'.join(rows))

    def _navExpression(self, expr):
        if self._canv_navcallback:
            self._canv_navcallback(expr)

    def _menuRename(self, va):
        name, ok = QtGui.QInputDialog.getText(self, 'Enter...', 'Name')
        if ok:
            self.vw.makeName(va, str(name))

    def _menuComment(self, va):
        comment, ok = QtGui.QInputDialog.getText(self, 'Enter...', 'Comment')
        if ok:
            self.vw.setComment(va, str(comment))

    def _menuBookmark(self, va):
        bname, ok = QtGui.QInputDialog.getText(self, 'Enter...', 'Bookmark Name')
        if ok:
            self.vw.setVaSetRow('Bookmarks', (va, str(bname)))

    def _menuEditFunctionArgument(self, fva, idx, atype, aname):
        newname, ok = QtGui.QInputDialog.getText(self, 'Enter...', 'Argument Name')
        if ok:
            self.vw.setFunctionArg(fva, idx, atype, aname=str(newname), doprec=False)

    def _menuEditFunctionLocal(self, fva, offset, atype, aname):
        newname, ok = QtGui.QInputDialog.getText(self, 'Enter...', 'Local Name')
        if ok:
            self.vw.setFunctionLocal(fva, offset, atype, str(newname))

    def _menuMakeStruct(self, va):
        sname = vs_qt.selectStructure(self.vw.vsbuilder)
        if sname != None:
            self.vw.makeStructure(va, sname)
            self._last_sname = sname

    def _menuFunctionGraph(self, fva):
        #docwid = self.parentWidget().vwqgui.vqBuildDockWidget('VQVivFuncgraphView', floating=True)
        vwqgui = self.parentWidget().vwqgui
        fgraph = viv_q_funcgraph.VQVivFuncgraphView(self.vw, vwqgui)
        #fgwid = docwid.widget()
        fgraph.renderFunctionGraph(fva)
        fgraph.show()
        vwqgui.vqDockWidget(fgraph, floating=True)

    @firethread
    def _menuFuncEmuShow(self, fva, va):
        self.vw.vprint('Running emulator to: 0x%.8x' % (va,))
        emu = self.vw.getEmulator()
        emu.runFunction(fva, stopva=va)

        regs = emu.getRegisters()
        rnames = regs.keys()
        rnames.sort()

        self.vw.vprint("Showing Register/Magic State At: 0x%.8x" % va)

        op = self.vw.parseOpcode(va)
        self.vw.canvas.addVaText("0x%.8x: " % va, va)
        op.render(self.vw.canvas)
        self.vw.canvas.addText("\n")
        for i in xrange(len(op.opers)):
            o = op.opers[i]
            o.render(self.vw.canvas, op, i)
            self.vw.canvas.addText(" = ")
            oval = o.getOperValue(op, emu)
            mag = emu.getMagic(oval)
            base = "0x%.8x (%d)" % (oval,oval)
            if mag != None:
                if mag.va > oval:
                    base += " %s - %d" % (repr(mag), mag.va - oval)
                else:
                    base += " %s + %d" % (repr(mag), oval - mag.va)
            self.vw.vprint(base)

    def _locMenuRepr(self, va):

        vw = self.mem
        p = vw.arch.pointerString(va)
        locstr = "Undefined"
        loc = vw.getLocation(va)
        if loc != None:
            locstr = vw.reprLocation(loc)
        return '%s: %s' % (p, locstr[:32])

    def _menuFuncCallGraph(self, fva):
        vivgui = self.vw.getVivGui()
        callview = viv_q_funcviews.FuncCallsView( self.vw )
        callview.functionSelected( fva )
        callview.show()
        vivgui.vqDockWidget( callview, floating=True )

        #blockview = viv_q_funcviews.FunctionBlocksView( self.vw )
        #blockview.functionSelected( fva )
        #blockview.show()
        #vivgui.vqDockWidget( blockview, floating=True )

    def _menuFuncCodeBlocks(self, fva):
        vivgui = self.vw.getVivGui()
        #blockview = viv_q_funcviews.FunctionBlocksView( self.vw, parent=vivgui )
        blockview = viv_q_funcviews.FunctionBlocksView( self.vw )
        blockview.functionSelected( fva )
        blockview.show()
        vivgui.vqDockWidget( blockview, floating=True )
        #self.testtest.functionSelected( fva )
        #self.testtest.show()

    def _woot(self, *args, **kwargs):
        self.vw.vprint('Still working on it....')

    def contextMenuEvent(self, event):

        vw = self.mem # Our mem object is a viv workspace!

        menu = vqt_menu.VQMenu('context', parent=self)
        menu.splitchar = '/'

        va = self._canv_curva
        if va != None:

            menu.addField('Rename (n)', self._menuRename, (self._canv_curva,))
            menu.addField('Comment (;)', self._menuComment, (self._canv_curva,))

            # Check for and add xrefs right click option
            for x,tova,xrtype,xrflag in vw.getXrefsTo(va):
                locstr = self._locMenuRepr(x)
                menu.addField('Xrefs To/%s' % locstr, self._navExpression, args=('0x%.8x' % x,))

            for fromva,x,xrtype,xrflag in vw.getXrefsFrom(va):
                locstr = self._locMenuRepr(x)
                menu.addField('Xrefs From/%s' % locstr, self._navExpression, ('0x%.8x' % x,))

            fva = vw.getFunction(va)
            if fva != None:

                fname = vw.getName(fva)
                menu.addField('Function/%s' % fname, self._navExpression, args=(fname,))

                for i,(atype,aname) in enumerate(vw.getFunctionArgs(fva)):
                    menu.addField('Function/Arguments/%s_%d' % (aname,i), self._menuEditFunctionArgument, (fva, i, atype, aname))

                locals = vw.getFunctionLocals(fva)
                locals.sort(cmp=cmpoffset)
                for aoffset, atype, aname in locals:
                    menu.addField('Function/Locals/%s_%d' % (aname,aoffset), self._menuEditFunctionLocal, (fva, aoffset, atype, aname))

                #menu.addField('Function/Edit...', self._woot, (fva,))
                menu.addField('Function/Emulation/Emulate To Here', self._woot, (fva,va))
                menu.addField('Function/Emulation/Show Emu State', self._menuFuncEmuShow, (fva,va))
                menu.addField('Function/Highlight', self._woot, (fva,))
                menu.addField('Function/Show Callers', self._woot, (fva,))
                menu.addField('Function/Code Blocks', self._menuFuncCodeBlocks, (fva, ))
                menu.addField('Function/Call Graph', self._menuFuncCallGraph, (fva, ))
                # FIXME function code flow to here with highlight

            loc = vw.getLocation(va)
            if loc == None:
                menu.addField('Make/Code (c)',     vw.makeCode,     (self._canv_curva,))
                menu.addField('Make/Function (f)', vw.makeFunction, (self._canv_curva,))
                menu.addField('Make/String (s)',   vw.makeString,   (self._canv_curva,))
                menu.addField('Make/Pointer (p)',  vw.makePointer,  (self._canv_curva,))
                menu.addField('Make/Unicode (u)',  vw.makeUnicode,  (self._canv_curva,))
                menu.addField('Make/Structure (S)', self._menuMakeStruct, (self._canv_curva,))

            else:

                if loc[L_LTYPE] == LOC_OP:

                    op = vw.parseOpcode(va)
                    for idx,oper in enumerate(op.opers):
                        # Give the option to switch ('hint') that you want
                        # the immediate operand displayed differently...
                        if oper.isImmed():
                            val = oper.getOperValue(op)
                            hval = e_bits.hex(val)

                            cval = val
                            r = []
                            while cval:
                                r.append(chr(cval & 0xff))
                                cval = cval >> 8
                            cstr = repr(''.join(r))

                            menu.addField('Immediate/Decimal (%d)' % val, vw.setSymHint, args=(va, idx, str(val)))
                            menu.addField('Immediate/Hex (%s)' % hval,    vw.setSymHint, args=(va, idx, hval))
                            menu.addField('Immediate/Chars (%s)' % cstr,  vw.setSymHint, args=(va, idx, cstr))

                            names = vw.vsconsts.revLookup(val)
                            if names != None:
                                for name in names:
                                    menu.addField('Immediate/%s' % name, vw.setSymHint, args=(va, idx, name))

                menu.addField('Undefine ()',    vw.delLocation, (self._canv_curva,))


            menu.addField('Color Maps/Clear All...', self._clearColorMap)
            names = vw.getColorMaps()
            names.sort()
            for name in names:
                map = vw.getColorMap(name)
                menu.addField('Color Maps/%s' % name, self._applyColorMap, (map,))

            menu.addField('Bookmark (B)', self._menuBookmark, args=(self._canv_curva, ))

        menu.exec_(event.globalPos())


class VQVivMemoryView(e_mem_qt.VQMemoryWindow, viv_base.VivEventCore):

    __canvas_class__ = VQVivMemoryCanvas

    def __init__(self, vw, vwqgui):
        self.vw = vw
        self.vwqgui = vwqgui

        e_mem_qt.VQMemoryWindow.__init__(self, vw, syms=vw, parent=vwqgui)
        viv_base.VivEventCore.__init__(self, vw)

        vwqgui.addEventCore(self)
        vwqgui.vivNavSignal.connect( self.vivMemNavSlot )
        vwqgui.vivMemColorSignal.connect( self.mem_canvas._applyColorMap )

        self.mem_canvas.setNavCallback(self._navGotoExpr)
        self.mem_canvas._canv_rend_middle = True
        self.mem_canvas.vqAddHotKey('x', self._hotkey_x)

    def _hotkey_x(self, canv, key):
        if self.mem_canvas._canv_curva:
            xrefs = self.vw.getXrefsTo(self.mem_canvas._canv_curva)
            if len(xrefs) == 0:
                self.vw.vprint('No xrefs found!')
                return

            title = 'Xrefs To: 0x%.8x' % self.mem_canvas._canv_curva
            view = viv_q_views.VQXrefView(self.vw, self.vwqgui, xrefs=xrefs, title=title)
            self.vwqgui.vqDockWidget(view, floating=True)

    def closeEvent(self, event):
        # FIXME this doesn't actually do anything...
        self.parentWidget().delEventCore(self)
        return e_mem_qt.VQMemoryWindow.closeEvent(self, event)

    def _navGotoExpr(self, expr):
        parent = self.parentWidget()
        if parent.isFloating():
            # If we are floating, consume nav events internally
            self.vqMemNavSlot(expr)
            return 
        self.vwqgui.vivNavSignal.emit(expr)

    def vivMemNavSlot(self, expr, sizeexpr=None):
        parent = self.parentWidget()
        if parent.isFloating():
            return
        if parent.vqIsVisible():
            self.vqMemNavSlot(expr, sizeexpr=sizeexpr)

    def loadDefaultRenderers(self):

        import envi.memcanvas.renderers as e_render

        # FIXME check endianness
        self.mem_canvas.addRenderer("bytes",    e_render.ByteRend())
        self.mem_canvas.addRenderer("u_int_16", e_render.ShortRend())
        self.mem_canvas.addRenderer("u_int_32", e_render.LongRend())
        self.mem_canvas.addRenderer("u_int_64", e_render.QuadRend())

        vivrend = viv_rend.WorkspaceRenderer(self.vw)
        self.mem_canvas.addRenderer('Viv', vivrend)
        self.mem_canvas.setRenderer('Viv')

    def _updateFunction(self, fva):
        for cbva, cbsize, cbfva in self.vw.getFunctionBlocks(fva):
            self.mem_canvas.renderMemoryUpdate(cbva, cbsize)

    def VWE_SYMHINT(self, vw, event, einfo):
        va, idx, hint = einfo
        self.mem_canvas.renderMemoryUpdate(va, 1)

    def VWE_ADDLOCATION(self, vw, event, einfo):
        va,size,ltype,tinfo = einfo
        self.mem_canvas.renderMemoryUpdate(va, size)

    def VWE_DELLOCATION(self, vw, event, einfo):
        va,size,ltype,tinfo = einfo
        self.mem_canvas.renderMemoryUpdate(va, size)

    def VWE_ADDFUNCTION(self, vw, event, einfo):
        va,meta = einfo
        self.mem_canvas.renderMemoryUpdate(va, 1)

    def VWE_SETFUNCMETA(self, vw, event, einfo):
        fva, key, val = einfo
        self._updateFunction(fva)

    def VWE_SETFUNCARGS(self, vw, event, einfo):
        fva, fargs = einfo
        self._updateFunction(fva)

    def VWE_COMMENT(self, vw, event, einfo):
        va,cmnt = einfo
        self.mem_canvas.renderMemoryUpdate(va, 1)

    def VWE_SETNAME(self, vw, event, einfo):
        va,name = einfo
        self.mem_canvas.renderMemoryUpdate(va, 1)
        for fromva,tova,rtype,rflag in self.vw.getXrefsTo(va):
            self.mem_canvas.renderMemoryUpdate(fromva, 1)

