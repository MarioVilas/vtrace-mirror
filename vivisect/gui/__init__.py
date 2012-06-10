
import os
import gtk
import time
import gobject
import threading
import traceback

import envi.bits as e_bits
import envi.config as e_config

import vwidget
import vwidget.main as vw_main
import vwidget.views as vw_views
import vwidget.layout as vw_layout
import vwidget.memview as vw_memview
import vwidget.windows as vw_windows
import vwidget.vwvtrace as vw_vtrace
import vwidget.pydialog as vw_pydialog
import vwidget.vwvstruct as vw_vstruct
import vwidget.menubuilder as vw_menu

import vivisect
import vivisect.base as viv_base
import vivisect.vdbext as viv_vdbext
import vivisect.server as viv_server
import viv_views
import vivisect.reports as viv_reports

import vtrace
import vtrace.envitools as vt_envitools

import vdb
import vdb.gui as vdb_gui

from vivisect.const import *
from envi.threads   import firethread
from vwidget.main   import idlethread,idlethreadsync

def cmpoffset(x,y):
    return cmp(x[0], y[0])

class VivWindow(vw_layout.LayoutWindow):
    def __init__(self, vw, gui):
        vw_layout.LayoutWindow.__init__(self)
        self.vw = vw
        self.gui = gui
        self.vivBuildWindow()

    def vivBuildWindow(self):
        pass

class VivVaSetViewWindow(VivWindow):

    def __init__(self, vw, gui, setname=None):
        self.vasetname = setname
        self.vivview = None
        VivWindow.__init__(self, vw, gui)

    def getWindowState(self):
        return self.vasetname

    def setWindowState(self, state):
        self.set_title("Va Set: %s" % state)
        self.vasetname = state
        self.vivview.va_set_name = state
        self.vivview.vwLoad()

    def vivBuildWindow(self):
        self.vivview = viv_views.VaSetView(self.vw, self.gui, self.vasetname)
        self.set_title("Va Set: %s" % self.vasetname)
        self.add(self.vivview)

class VivCallersWindow(VivWindow):

    def __init__(self, vw, gui, funcva=None):
        self.funcva = funcva
        VivWindow.__init__(self, vw, gui)

    def getWindowState(self):
        return self.funcva

    def setWindowState(self, funcva):
        self.funcva = funcva
        self.vivview.funcva = funcva
        pstr = self.vw.arch.pointerString(self.funcva)
        self.set_title("Callers: %s" % pstr)
        self.vivview.vwLoad()

    def vivBuildWindow(self):
        self.vivview = viv_views.CallersView(self.vw, self.gui, self.funcva)
        if self.funcva != None:
            pstr = self.vw.arch.pointerString(self.funcva)
            self.set_title("Callers: %s" % pstr)
        self.add(self.vivview)

class InputDialog(gtk.Dialog):
    def __init__(self, parent):
        self.prompt = gtk.Label()
        buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OK,gtk.RESPONSE_OK)
        gtk.Dialog.__init__(self, "Input Required", parent, buttons=buttons)
        hb = gtk.HBox()
        hb.pack_start(self.prompt)
        self.entry = gtk.Entry()
        self.entry.connect("activate", self.entryActivate)
        hb.pack_start(self.entry)
        hb.show_all()
        self.vbox.pack_start(hb)

    def setPrompt(self, prompt):
        self.prompt.set_text(' %s' % prompt)

    def setDefault(self, default=None):
        if default == None:
            default = ''
        self.entry.set_text(default)

    def entryActivate(self, *args):
        self.response(gtk.RESPONSE_OK)

    def getInputText(self):
        ret = None
        if self.run() == gtk.RESPONSE_OK:
            ret = self.entry.get_text()
        self.hide()
        return ret

class VivMemoryView(vw_memview.MemoryView):

    def __init__(self, vw, gui, memwin):
        self.vw = vw
        self.gui = gui
        self.memwin = memwin
        vw_memview.MemoryView.__init__(self, vw, syms=vw)
        for name in vw.canvas.getRendererNames():
            self.addRenderer(name, vw.canvas.getRenderer(name))

        self.registerHotKey(ord('c'), self.hkCode)
        self.registerHotKey(ord('s'), self.hkString)
        self.registerHotKey(ord('S'), self.hkStruct)
        self.registerHotKey(ord('p'), self.hkPointer)
        self.registerHotKey(ord('f'), self.hkFunc)
        self.registerHotKey(ord('u'), self.hkUnicode)
        self.registerHotKey(ord('x'), self.hkXrefs)
        self.registerHotKey(ord('n'), self.hkName)
        self.registerHotKey(ord('U'), self.hkUndef)
        self.registerHotKey(ord(';'), self.hkComment)
        self.registerHotKey(ord('B'), self.hkBookmark)
        self.registerHotKey(ord('G'), self.hkFuncGraph)

    def hkFuncGraph(self, *args):
        if self.selectva == None:
            return
        fva = self.vw.getFunction(self.selectva)
        if fva == None:
            return
        self.popFunctionGraph(None, fva)

    def hkBookmark(self, *args):
        if self.selectva == None:
            return
        name = self.gui.getInputText("Bookmark Name:", parent=self.memwin)
        if name != None:
            self.vw.setVaSetRow("Bookmarks",(self.selectva, name))

    def hkFlow(self, *args):
        if self.selectva == None:
            return

    def hkComment(self, *args):
        if self.selectva == None:
            return
        cmnt = self.gui.getInputText("Comment:", parent=self.memwin)
        if cmnt != None:
            self.vw.setComment(self.selectva, cmnt)

    def hkXrefs(self, *args):
        if self.selectva == None:
            return
        win = self.gui.presentWindow("VivXrefWindow")
        win.addXrefTab(self.selectva)

    def hkUndef(self, *args):
        if self.selectva == None:
            return
        if self.vw.getLocation(self.selectva) == None:
            return
        self.vw.delLocation(self.selectva)

    def hkName(self, *args):
        if self.selectva == None:
            return
        name = self.gui.getInputText("Name:", parent=self.memwin)
        if name != None:
            self.vw.makeName(self.selectva, name)

    def hkFunc(self, *args):
        if self.selectva == None:
            return
        loc = self.vw.getLocation(self.selectva)
        if loc != None:
            if loc[L_LTYPE] != LOC_OP:
                return
        self.vw.makeFunction(self.selectva)

    def hkStruct(self, *args):
        if self.selectva == None:
            return
        if self.vw.getLocation(self.selectva) != None:
            return
        sname = vw_vstruct.selectStructure(self.vw.vsbuilder, parent=self.memwin)
        if sname == None:
            return
        self.vw.makeStructure(self.selectva, sname)

    def hkUnicode(self, *args):
        if self.selectva == None:
            return
        if self.vw.getLocation(self.selectva) != None:
            return
        self.vw.makeUnicode(self.selectva)

    @firethread
    def hkCode(self, *args):
        if self.selectva == None:
            return
        if self.vw.getLocation(self.selectva) != None:
            return
        self.vw.makeCode(self.selectva)

    def hkString(self, *args):
        if self.selectva == None:
            return
        if self.vw.getLocation(self.selectva) != None:
            return
        self.vw.makeString(self.selectva)

    def hkPointer(self, *args):
        if self.selectva == None:
            return
        if self.vw.getLocation(self.selectva) != None:
            return
        self.vw.makePointer(self.selectva)

    def renderMemory(self, va, size, rend=None):
        # We're a little special, when we get asked to render, 
        # render twice the size, starting at va-size and then scroll
        # to the actual VA location.
        base = va-size
        map = self.vw.getMemoryMap(va)
        if map != None:
            mapbase, mapsize, mperm, mfile = map
            if mapbase > base:
                base = mapbase

        vw_memview.MemoryView.renderMemory(self, base, size*2, rend=rend)
        # We need everything to think our last requested size was real
        self.lastsize = size

    def vwGetPopup(self, textview, menu, vwfaddr=None):
        pos = 0
        va = self.selectva

        vwmenu = vwfaddr
        if vwmenu == None:
            vwmenu = vw_menu.FieldAdder(menu, splitchar='/')

        if va != None:

            vwmenu.addField('Rename (n)', self.hkName)
            vwmenu.addField('Comment (;)', self.hkComment)

            # Check for and add xrefs right click option
            for x,tova,xrtype,xrflag in self.vw.getXrefsTo(va):
                p = self.vw.arch.pointerString(x)
                locstr = "Undefined"
                loc = self.vw.getLocation(x)
                if loc != None:
                    locstr = self.vw.reprLocation(loc)

                locstr = locstr.replace('.','_')
                vwmenu.addField('Xrefs To/%s: %s' % (p, locstr[:32]), self.popSelectXref, (x,))

            for fromva,x,xrtype,xrflag in self.vw.getXrefsFrom(va):
                p = self.vw.arch.pointerString(x)
                locstr = "Undefined"
                loc = self.vw.getLocation(x)
                if loc != None:
                    locstr = self.vw.reprLocation(loc)

                locstr = locstr.replace('.','_')
                vwmenu.addField('Xrefs From/%s: %s' % (p, locstr[:32]), self.popSelectXref, (x,))

            fva = self.vw.getFunction(va)
            if fva != None:
                fname = self.vw.getName(fva)

                vwmenu.addField('Function/%s' % fname, self.popGoto, (fva,))

                for i,(atype,aname) in enumerate(self.vw.getFunctionArgs(fva)):
                    vwmenu.addField('Function/Arguments/%s_%d' % (aname,i), self.popEditFuncArg, (fva, i, atype, aname))

                locals = self.vw.getFunctionLocals(fva)
                locals.sort(cmp=cmpoffset)
                for aoffset, atype, aname in locals:
                    vwmenu.addField('Function/Locals/%s_%d' % (aname,aoffset), self.popEditFuncLocal, (fva, aoffset, atype, aname))

                vwmenu.addField('Function/Edit...', self.popEditFunc, (fva,))
                vwmenu.addField('Function/Emulation/Emulate To Here', self.popEmulateFunc, (fva,va))
                vwmenu.addField('Function/Emulation/Show Emu State', self.popEmulateShow, (fva,va))
                vwmenu.addField('Function/Highlight', self.popHighlightFunc, (fva,))
                vwmenu.addField('Function/Show Callers', self.popShowCallers, (fva,))
                vwmenu.addField('Function/Graph (alpha)(G)', self.popFunctionGraph, (fva,))
                # FIXME function code flow to here with highlight

            loc = self.vw.getLocation(va)
            if loc == None:
                vwmenu.addField('Make/Code (c)', self.hkCode)
                vwmenu.addField('Make/Function (f)', self.hkFunc)
                vwmenu.addField('Make/String (s)', self.hkString)
                vwmenu.addField('Make/Pointer (p)', self.hkPointer)
                vwmenu.addField('Make/Unicode (u)', self.hkUnicode)
                vwmenu.addField('Make/Structure (S)', self.hkStruct)

            elif loc[L_LTYPE] == LOC_OP:
                op = self.vw.parseOpcode(va)
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

                        vwmenu.addField('Immediate/Decimal (%d)' % val, self.symHintThunk, (va, idx, str(val)))
                        vwmenu.addField('Immediate/Hex (%s)' % hval, self.symHintThunk, (va, idx, hval))
                        vwmenu.addField('Immediate/Chars (%s)' % cstr, self.symHintThunk, (va, idx, cstr))
                        names = self.vw.vsconsts.revLookup(val)
                        if names != None:
                            for name in names:
                                vwmenu.addField('Immediate/%s' % name, self.symHintThunk, (va, idx, name))

                if not self.vw.isFunction(va):
                    vwmenu.addField('Make/Function (f)', self.hkFunc)

            vwmenu.addField('Color Maps/Clear All...', self.popColorMap, (None, ))
            names = self.vw.getColorMaps()
            names.sort()
            for name in names:
                map = self.vw.getColorMap(name)
                vwmenu.addField('Color Maps/%s' % name, self.popColorMap, (map,))

            vwmenu.addField('Bookmark (B)', self.hkBookmark)
            
    def popEditFuncArg(self, item, fva, idx, atype, aname):
        newname = self.gui.getInputText('Argument Name', default=aname)
        if newname != None:
            self.vw.setFunctionArg(fva, idx, atype, aname=newname, doprec=False)

    def popEditFuncLocal(self, item, fva, offset, atype, aname):
        newname = self.gui.getInputText('Local Name', default=aname)
        if newname != None:
            self.vw.setFunctionLocal(fva, offset, atype, newname)

    def popHighlightFunc(self, item, funcva):
        map = {}
        for cbva, cbsize, fva in self.vw.getFunctionBlocks(funcva):
            endva = cbva+cbsize
            while cbva < endva:
                lva,lsize,ltype,linfo = self.vw.getLocation(cbva)
                map[lva] = "yellow"
                cbva+=lsize
        self.setColorMap(map)

    def popEditFunc(self, item, fva):
        w = VivFunctionWindow(self.vw, self.gui, fva)
        self.gui.manageWindow(w)

    def popColorMap(self, item, map):
        self.setColorMap(map)

    def popFunctionGraph(self, item, fva):
        import vivisect.gui.funcgraph as viv_funcgraph
        thr = threading.Thread(target=viv_funcgraph.makeFuncGraphWindow, args=(self.vw,fva))
        thr.setDaemon(True)
        thr.start()
        
    def popShowCallers(self, item, fva):
        w = VivCallersWindow(self.vw, self.gui, fva)
        self.gui.manageWindow(w)

    @firethread
    def popEmulateFunc(self, item, fva, va):
        self.vw.vprint('Running emulator to: 0x%.8x' % (va,))
        emu = self.vw.getEmulator()
        emu.runFunction(fva, stopva=va)
        trace = vt_envitools.TraceEmulator(emu)
        db = vdb.Vdb(trace=trace)
        vdb_gui.VdbGui(db, ismain=False)
        db.onecmd('dis')
        db.vprint('Emulation Stepped To: 0x%.8x (in 0x%.8x)' % (va, fva))

    def symHintThunk(self, item, va, idx, hint):
        self.vw.setSymHint(va, idx, hint)

    @firethread
    def popEmulateShow(self, item, fva, va):
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
            base = "%.8x (%d)" % (oval,oval)
            if mag != None:
                if mag.va > oval:
                    base += " %s - %d" % (repr(mag), mag.va - oval)
                else:
                    base += " %s + %d" % (repr(mag), oval - mag.va)
            self.vw.vprint(base)

    def popGoto(self, item, va):
        self.goto(va)

    def popSelectXref(self, item, va):
        self.gui.goto(va)

class VivMemoryWindow(vw_memview.MemoryWindow, viv_base.VivEventCore):

    def __init__(self, vw, gui):
        self.vw = vw
        self.gui = gui
        canvas = VivMemoryView(vw, gui, self)
        vw_memview.MemoryWindow.__init__(self, canvas)
        viv_base.VivEventCore.__init__(self, vw)
        gui.addEventCore(self)

    def vwDestroy(self):
        self.gui.delEventCore(self)

    def _refreshFunction(self, fva):
        for cbva, cbsize, cbfva in self.vw.getFunctionBlocks(fva):
            self.canvas.refresh(cbva, cbsize)

    def VWE_SYMHINT(self, vw, event, einfo):
        va, idx, hint = einfo
        self.canvas.refresh(va, 1)

    def VWE_ADDLOCATION(self, vw, event, einfo):
        va,size,ltype,tinfo = einfo
        self.canvas.refresh(va, size)

    def VWE_DELLOCATION(self, vw, event, einfo):
        va,size,ltype,tinfo = einfo
        self.canvas.refresh(va, size)

    def VWE_ADDFUNCTION(self, vw, event, einfo):
        va,meta = einfo
        self.canvas.refresh(va, 1)

    def VWE_SETFUNCMETA(self, vw, event, einfo):
        fva, key, val = einfo
        self._refreshFunction(fva)

    def VWE_SETFUNCARGS(self, vw, event, einfo):
        fva, fargs = einfo
        self._refreshFunction(fva)

    def VWE_COMMENT(self, vw, event, einfo):
        va,cmnt = einfo
        self.canvas.refresh(va, 1)

    def VWE_SETNAME(self, vw, event, einfo):
        va,name = einfo
        self.canvas.refresh(va, 1)
        for fromva,tova,rtype,rflag in self.vw.getXrefsTo(va):
            self.canvas.refresh(fromva, 1)

class VivNaviWindow(VivWindow):

    def vivBuildWindow(self):

        self.set_title("Viv Navi")

        notebook = gtk.Notebook()
        self.funcview = viv_views.FunctionsView(self.vw, self.gui)
        self.exportsview = viv_views.ExportsView(self.vw, self.gui)
        self.importsview = viv_views.ImportsView(self.vw, self.gui)

        notebook.append_page(self.funcview, gtk.Label("Functions"))
        notebook.append_page(self.importsview, gtk.Label("Imports"))
        notebook.append_page(self.exportsview, gtk.Label("Exports"))

        self.add(notebook)

class VivDataWindow(VivWindow):

    def vivBuildWindow(self):
        self.set_title("Viv Data")

        notebook = gtk.Notebook()

        self.filesview = viv_views.FilesView(self.vw, self.gui)
        self.stringsview = viv_views.StringsView(self.vw, self.gui)
        self.structsview = viv_views.StructsView(self.vw, self.gui)

        notebook.append_page(self.filesview, gtk.Label("Files/Sections"))
        notebook.append_page(self.stringsview, gtk.Label("Strings"))
        notebook.append_page(self.structsview, gtk.Label("Structures"))

        self.add(notebook)

class VivXrefWindow(VivWindow):

    def vivBuildWindow(self):
        self.notebook = gtk.Notebook()
        self.add(self.notebook)

    def addXrefTab(self, va):
        view = viv_views.XrefView(self.vw, self.gui, va)
        l = gtk.Label(view.vwGetDisplayName())
        self.notebook.append_page(view, l)
        self.notebook.set_current_page(-1)
        l.show_all()
        view.show_all()

    def getWindowState(self):
        ret = []
        for i in range(self.notebook.get_n_pages()):
            p = self.notebook.get_nth_page(i)
            ret.append(p.xrefva)
        return ret

    def setWindowState(self, state):
        for va in state:
            self.addXrefTab(va)

    #FIXME update on events

class VivSearchWindow(VivWindow):

    def vivBuildWindow(self):
        self.set_title("Search Results")
        self.notebook = gtk.Notebook()
        self.add(self.notebook)

    def addSearchPattern(self, pattern, res=None):
        if res == None:
            res = self.vw.searchMemory(pattern)
        l = gtk.Label("Pattern: %s" % pattern.encode('hex')[:20])
        view = viv_views.SearchView(self.vw, self.gui, res)
        l.show_all()
        view.show_all()
        self.notebook.append_page(view, l)

class VivReportWindow(VivWindow):
    def __init__(self, vw, gui, repmod, report=None):
        self.repmod = repmod
        self.report = report
        VivWindow.__init__(self, vw, gui)
        self.lyt_restore = False # We don't want to be saved

    def vivBuildWindow(self):
        self.set_title("Report Results: %s" % self.repmod.__name__)
        self.reportview = viv_views.ReportView(self.vw, self.gui, self.repmod, self.report)
        self.add(self.reportview)

class VivFunctionWindow(VivWindow, viv_base.VivEventCore):

    def __init__(self, vw, gui, fva):
        self.fva = fva
        VivWindow.__init__(self, vw, gui)
        viv_base.VivEventCore.__init__(self,vw)
        gui.addEventCore(self)
        self.set_title('Editing: 0x%.8x %s' % (fva, vw.getName(fva)))

    def vwDestroy(self):
        self.gui.delEventCore(self)

    def vivBuildWindow(self):
        vbox = gtk.VBox()

        hbox1 = gtk.HBox()
        h1_vbox1 = gtk.VBox()
        h1_vbox2 = gtk.VBox()

        h1_vbox1.pack_start(gtk.Label('Function Parameters'), expand=False)
        parmview = viv_views.VivFuncParamView(self.vw, self.gui, self.fva)
        h1_vbox1.pack_start(parmview)

        fcconv = self.vw.getFunctionMeta(self.fva, 'CallingConvention')
        matchidx = None
        h1_vbox2.pack_start(gtk.Label('Calling Convention'), expand=False)
        callconv = gtk.combo_box_new_text()
        callconv.connect('changed', self.cbCallConvChanged)
        conventions = self.vw.arch.getCallingConventions()
        for i,(name,obj) in enumerate(conventions):
            if name == fcconv:
                matchidx = i
            callconv.append_text(name)
        callconv.append_text('__unknown')
        if matchidx == None:
            # Set ourself to '__unknown'
            matchidx = len(conventions)
        callconv.set_active(matchidx)
        h1_vbox2.pack_start(callconv, expand=False)

        hbox1.pack_start(h1_vbox1)
        hbox1.pack_start(h1_vbox2)
        vbox.pack_start(hbox1)

        vbox.pack_start(gtk.Label('Function Code Blocks'), expand=False)
        cbview = viv_views.VivCodeBlockView(self.vw, self.gui, self.fva)
        vbox.pack_start(cbview)

        vbox.pack_start(gtk.Label('Function Meta Data'), expand=False)
        mview = viv_views.VivFuncMetaView(self.vw, self.gui, self.fva)
        vbox.pack_start(mview)

        vbox.show_all()
        self.add(vbox)
        self.resize(800, 600)

        self._initFunctionData()


    def getWindowState(self):
        return self.fva

    def setWindowState(self, fva):
        self.fva = fva
        self._initFunctionData()

    def _initFunctionData(self):

        name = self.vw.getName(self.fva)
        self.set_title('Function: 0x%.8x %s' % (self.fva, name))

    def cbCallConvChanged(self, cbox):
        model = cbox.get_model()
        idx   = cbox.get_active()
        cconv = model[idx][0]
        if cconv == 'Unknown':
            cconv = None
        self.vw.setFunctionMeta(self.fva, 'CallingConvention', cconv)

class VivMainWindow(vw_windows.MainWindow):

    def __init__(self, vw, gui):
        self.vw = vw
        self.gui = gui

        # The viv workspace is cli/memobj/symboj
        vw_windows.MainWindow.__init__(self, vw, vw, syms=vw)
        self.connect('delete_event', self._mainDelete)

        self.set_title("Vivisect Console")

        self.menubar.addField("_File._Open._Workspace", self.file_open_workspace)
        self.menubar.addField("_File._Open._Binary._PE", self.file_open_binary, args=("pe",))
        self.menubar.addField("_File._Open._Binary._Elf", self.file_open_binary, args=("elf",))
        self.menubar.addField("_File._Open._Binary._blob", self.file_open_binary, args=("blob",))

        self.menubar.addField("_File._Save", self.file_save)
        self.menubar.addField("_File.Save As", self.file_saveas)

        self.menubar.addField("_File._Quit", self.file_quit)
        #self.menubar.addField("Edit", None)

        self.menubar.addField("_View._Memory", self.view_window, args=("VivMemoryWindow",))

        self.menubar.addField("_View._Navigation", self.view_window, args=("VivNaviWindow",))
        self.menubar.addField("_View._Data/Structures", self.view_window, args=("VivDataWindow",))

        self.menubar.addField("_Search._String (asdf)", self.search_string)
        self.menubar.addField("_Search._Hex (414243)", self.search_bytes)
        #FIXME endian
        self.menubar.addField("_Search._Expression (0xf0 + 20)", self.search_expression)

        self.menubar.addField('_Share._Share Workspace', self.share_workspace)
        self.menubar.addField('_Share._Connect To Workspace', self.share_connect)
        self.menubar.addField('_Share._Lead/Follow._Lead', self.share_lead)
        self.menubar.addField('_Share._Lead/Follow._Follow', self.share_follow)
        self.menubar.addField('_Share._Lead/Follow._Get Out Of The Way', self.share_outtheway)

        self.menubar.addField('_Debug._Vdb', self.debug_local)
        self.menubar.addField('_Debug._Remote Vdb', self.debug_remote)

        self.menubar.addField("_Tools._Python", self.tools_python)
        self.menubar.addField('_Tools._Structures._Add Namespace', self.tools_struct_addns)

        for descr, modname in viv_reports.listReportModules():
            self.menubar.addField("_Tools._Reports._%s" % descr, self.tools_reports, args=(modname,))

        self.menubar.addField("_Tools._Extended Analysis._Crypto Constants", self.tools_eanalysis, args=("vivisect.analysis.crypto.constants",))

        i = self.menubar.addField("_Tools._Va Sets")
        i.set_submenu(gtk.Menu())
        i.connect("select", self.tools_vasets_select)
        i.show_all()

    def _mainDelete(self, *args):
        if self.vw.vivhome:
            lfile = os.path.join(self.vw.vivhome, "viv.lyt2")
            self.gui.saveLayoutFile(file(lfile,"wb"))
        self.gui.deleteAllWindows(omit=self)
        self.vw.shutdown.set()
        if self.gui.ismain:
            vw_main.shutdown()

    def share_workspace(self, item):
        self.vw.vprint('Sharing workspace...')
        daemon = viv_server.shareWorkspace(self.vw)
        self.vw.vprint('Workspace Listening Port: %d' % daemon.port)

    def share_connect(self, item):
        self.vw.vprint('Viv now uses a client command... (to allow code sync)')
        self.vw.vprint('Use python vivclient <host> <port>')
        self.vw.vprint('Example: bash$ python vivclient 172.16.1.1 17384')

    def share_lead(self, item):
        self.vw.vprint('Leading Share GOTO...')
        self.gui.leadstate = LEADSTATE_LEAD

    def share_follow(self, item):
        self.vw.vprint('Following Share GOTO...')
        self.gui.leadstate = LEADSTATE_FOLLOW

    def share_outtheway(self, item):
        self.vw.vprint('Ignoring Share GOTO...')
        self.gui.leadstate = LEADSTATE_OUTTHEWAY

    def debug_local(self, item):
        t = vtrace.getTrace()
        dia = vw_vtrace.SelectProcessDialog(t)
        pid = dia.selectProcess()
        viv_vdbext.runVdb(self.gui, pid=pid)

    def debug_remote(self, item):
        x = self.gui.getInputText('Remote Host:', parent=self, default='<vdb server>')
        if x == None:
            return
        vtrace.remote = x
        self.debug_local(item)

    def search_string(self, item):
        x = self.gui.getInputText('String:', parent=self, default="invisigoth")
        if x != None:
            self.searchAndShow(x)

    def search_bytes(self, item):
        x = self.gui.getInputText('Hex Bytes:', parent=self, default="56565656")
        if x != None:
            self.searchAndShow(x.decode('hex'))

    def search_expression(self, item):
        self.vw.vprint("FIXME search_expression")

    def searchAndShow(self, pattern):
        win = self.gui.presentWindow("VivSearchWindow")
        win.addSearchPattern(pattern)

    def tools_python(self, item):
        l = self.vw.getExpressionLocals()
        p = vw_pydialog.PyDialog(l)
        p.show()

    def tools_struct_addns(self, item):
        n = vw_vstruct.selectNamespace(parent=self)
        if n != None:
            nsname, modname = n
            self.vw.addStructureModule(nsname, modname)

    def tools_eanalysis(self, mitem, modname):
        mod = self.vw.loadModule(modname)
        self.vw.vprint("Running: %s" % modname)
        thr = threading.Thread(target=mod.analyze, args=(self.vw,))
        thr.setDaemon(True)
        thr.start()

    def tools_vaset(self, mitem, setname):
        w = VivVaSetViewWindow(self.vw, self.gui, setname)
        self.gui.manageWindow(w)

    def tools_vasets_select(self, mitem):
        subm = mitem.get_submenu()
        for n in subm.get_children():
            subm.remove(n)

        for name in self.vw.getVaSetNames():
            mi = gtk.MenuItem(label=name)
            mi.show()
            mi.connect("activate", self.tools_vaset, name)
            subm.append(mi)

    @firethread
    def runReport(self, rmod):
        rep = rmod.report(self.vw)
        self.showReport(rmod, rep)

    @idlethread
    def showReport(self, rmod, rep):
        self.vw.vprint("%d results" % len(rep))
        rwin = VivReportWindow(self.vw, self.gui, rmod, rep)
        self.gui.manageWindow(rwin)

    def tools_reports(self, menuitem, reportname):
        r = self.vw.loadModule(reportname)
        self.vw.vprint("Running: %s" % reportname)
        self.runReport(r)

    def file_quit(self, *args):
        self.gui.deleteAllWindows()

    def file_save(self, menuitem):
        self.saveWorkspace(fullsave=False)

    @firethread
    def saveWorkspace(self, fullsave=True):
        self.vw.vprint('Saving %s...' % (self.vw.getMeta('StorageName')))
        s = time.time()
        self.vw.saveWorkspace(fullsave=fullsave)
        e = time.time()
        self.vw.vprint('...save complete! (%d sec)' % (e-s))

    @firethread
    def loadBinaryFile(self, filename, fmtname):
        self.vw.vprint("Loading %s..." % filename)
        self.vw.loadFromFile(filename, fmtname=fmtname)
        self.analyzeWorkspace()

    @firethread
    def analyzeWorkspace(self):
        self.vw.analyze()

    @firethread
    def loadWorkspace(self, wsname):
        self.vw.vprint('Loading %s...' % wsname)
        s = time.time()
        self.vw.loadWorkspace(wsname)
        e = time.time()
        self.vw.vprint('...load complete! (%d sec)' % (e-s))

    def file_saveas(self, menuitem):
        buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK)
        f = gtk.FileChooserDialog("Open Vivisect Workspace", self, action=gtk.FILE_CHOOSER_ACTION_SAVE, buttons=buttons)
        if f.run() == gtk.RESPONSE_OK:
            self.vw.setMeta('StorageName', f.get_filename())
            self.saveWorkspace(fullsave=True)
        f.destroy()

    def file_open_workspace(self, menuitem):
        buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK)
        f = gtk.FileChooserDialog("Open Vivisect Workspace", self, action=gtk.FILE_CHOOSER_ACTION_OPEN, buttons=buttons)
        if f.run() == gtk.RESPONSE_OK:
            self.loadWorkspace(f.get_filename())
        f.destroy()

    def file_open_binary(self, menuitem, parsemod):
        buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK)
        f = gtk.FileChooserDialog("Open %s Binary" % parsemod, self, action=gtk.FILE_CHOOSER_ACTION_OPEN, buttons=buttons)
        if f.run() == gtk.RESPONSE_OK:
            self.loadBinaryFile(f.get_filename(), parsemod)
        f.destroy()

    def view_window(self, menuitem, winname):
        self.gui.presentWindow(winname)

    def getMainToolbar(self):
        return None # FIXME for now...

LEADSTATE_OUTTHEWAY = 0
LEADSTATE_LEAD      = 1
LEADSTATE_FOLLOW    = 2

class VivGui(vw_layout.LayoutManager, viv_base.VivEventDist):

    def __init__(self, vw, ismain=True):

        self.vw = vw
        self.vw._viv_gui = self

        self.leadstate = LEADSTATE_OUTTHEWAY
        self.ismain = ismain
        self.inputdia = None
        vw_layout.LayoutManager.__init__(self)
        viv_base.VivEventDist.__init__(self, vw)

        self.defgeom = (20,20,600,450)
        self.addWindowClass(VivMainWindow, args=(vw, self), defgeom=self.defgeom)
        self.addWindowClass(VivMemoryWindow, args=(vw, self), defgeom=self.defgeom)
        self.addWindowClass(VivVaSetViewWindow, args=(vw, self), defgeom=self.defgeom)
        self.addWindowClass(VivReportWindow, args=(vw, self), defgeom=self.defgeom)
        self.addWindowClass(VivCallersWindow, args=(vw, self), defgeom=self.defgeom)

        self.addWindowClass(VivNaviWindow, args=(vw, self), defgeom=self.defgeom)
        self.addWindowClass(VivDataWindow, args=(vw, self), defgeom=self.defgeom)
        self.addWindowClass(VivXrefWindow, args=(vw, self), defgeom=self.defgeom)
        self.addWindowClass(VivSearchWindow, args=(vw, self), defgeom=self.defgeom)

        if not self.loadDefaultLayout():
            self.createWindow('VivMainWindow')
            self.createWindow('VivMemoryWindow')
        self.getOrCreateWindow('VivMainWindow')

    @idlethread
    def _ve_fireEvent(self, event, edata):
        return viv_base.VivEventDist._ve_fireEvent(self, event, edata)
        
    @idlethreadsync
    def getInputText(self, prompt, parent=None, default=None):
        """
        Request a single line of input from the user. Specify "default"
        for the default text in the input box, and parent for the parent
        window of the dialog box.
        """
        if self.inputdia == None:
            self.inputdia = InputDialog(parent)

        self.inputdia.setPrompt(prompt)
        self.inputdia.setDefault(default)

        return self.inputdia.getInputText()

    def VWE_FOLLOWME(self, event, einfo):
        if self.leadstate == LEADSTATE_FOLLOW:
            self.goto(einfo)

    @idlethread
    def goto(self, va):
        win = self.presentWindow('VivMemoryWindow')
        # If somebody uses GOTO and they are the leader, notify followers
        if self.leadstate == LEADSTATE_LEAD:
            self.vw._fireEvent(VWE_FOLLOWME, va)
        pstr = self.vw.arch.pointerString(va)
        oldva,oldsize,oldfmt = win.getWindowState()
        win.setWindowState((pstr, oldsize, oldfmt))

    @idlethread
    def setColorMap(self, cmap):
        win = self.presentWindow('VivMemoryWindow')
        win.canvas.setColorMap(cmap)

    def loadDefaultLayout(self):
        if self.vw.vivhome != None:
            lfile = os.path.join(self.vw.vivhome, "viv.lyt2")
            if os.path.exists(lfile):
                return self.loadLayoutFile(file(lfile, "rb"))
        return False

    def presentWindow(self, name):
        match = None
        for win in self.windows:
            if win.getWindowName() == name:
                match = win
                break
        if match == None:
            match = self.createWindow(name)
        match.present()
        return match

    def waitOnCli(self):
        self.vw.shutdown.wait()

