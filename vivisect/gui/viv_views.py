

import gtk
import gtk.gdk as gdk

import envi
import vivisect
import vwidget.views as vw_views
import vivisect.base as viv_base

from vivisect.const import *

class VivTreeView(vw_views.VTreeView, viv_base.VivEventCore):

    def __init__(self, vw, gui):
        self.vw = vw
        self.gui = gui
        self.addr_iter_map = {}
        vw_views.VTreeView.__init__(self)
        viv_base.VivEventCore.__init__(self, vw)
        gui.addEventCore(self)

    def vwDestroy(self, arg):
        self.gui.delEventCore(self)

    def getViewState(self):
        return None

    def setViewState(self, state):
        pass

    def vivRemove(self, va):
        iter = self.iters_by_va.pop(va, None)
        if iter != None:
            self.model.remove(iter)

class LocationListView(VivTreeView):
    __cols__ = (
        (None, 0, object),
        ("Address",1, str),
        ("Stuff",2, str)
    )
    
    def VWE_DELLOCATION(self, vw, event, einfo):
        self.vivRemove(einfo[L_VA])

    def vivInsert(self, *stuff):
        # Over-ride this
        pass

    def vivRemove(self, address):
        """
        Remove the row at the given address.
        """
        iter = self.addr_iter_map.pop(address, None)
        if iter != None:
            self.vwRemove(iter)

    def vwClear(self):
        self.addr_iter_map = {}
        self.vwClear()

    def vwActivated(self, tree, path, column):
        iter = self.model.get_iter(path)
        va = self.model.get_value(iter, 0)
        self.gui.goto(va)

class XrefView(LocationListView):
    __cols__ = (
        (None, 0, object),
        ("Address", 1, str),
        ("Repr", 2, str),
        ("Function Name", 3, str),
    )

    def __init__(self, vw, gui, va):
        self.xrefva = va
        LocationListView.__init__(self, vw, gui)

    def vwLoad(self):
        for fromva, tova, rtype, rflags in self.vw.getXrefsTo(self.xrefva):
            loc = self.vw.getLocation(fromva, range=True)
            locstr = self.vw.reprLocation(loc)
            self.vivInsert(fromva, locstr)

    def vivInsert(self, va, info):
        vastr = self.vw.arch.pointerString(va)
        cb = self.vw.getCodeBlock(va)
        if cb != None:
            cva,size,funcva = cb
            name = "%s+%d" % (self.vw.getName(funcva),va-funcva)
        else:
            name = ""

        name = name[:32]
        info = info[:32]
            
        iter = self.model.append((va, vastr, info, name))
        self.addr_iter_map[va] = iter

    def vwGetDisplayName(self):
        return "XRefs To: 0x%.8x" % self.xrefva

class SearchView(LocationListView):
    __cols__ = (
        (None, 0, object),
        ("Address", 1, str),
    )

    def __init__(self, vw, gui, res):
        self.res = res
        LocationListView.__init__(self, vw, gui)

    def vwLoad(self):
        for va in self.res:
            pstr = self.vw.arch.pointerString(va)
            iter = self.model.append((va, pstr))
            self.addr_iter_map[va] = iter

class VaSetView(LocationListView):

    __cols__ = (
        (None, 0, object),
    )

    def __init__(self, vw, gui, name):
        self.va_set_name = name
        self.defsdone = False
        LocationListView.__init__(self, vw, gui)

    def vwLoad(self):

        if self.va_set_name == None:
            return

        if not self.defsdone:

            cols = [(None, 0, object),]
            defs = self.vw.getVaSetDef(self.va_set_name)
            for idx,(name,rtype) in enumerate(defs):
                idx += 1
                if idx == 1:
                    cols.append((name, idx, str))
                else:
                    cols.append((name, idx, rtype))

            self.vwInitModel(cols, gtk.ListStore)

            self.defsdone = True

        for row in self.vw.getVaSetRows(self.va_set_name):
            self.vivInsert(row)

    def vivInsert(self, row):
        va = row[0]
        frow = (va, "0x%.8x" % va) + tuple(row[1:])
        iter = self.model.append(frow)
        self.addr_iter_map[va] = iter

    def VWE_SETVASETROW(self, vw, event, einfo):
        name, row = einfo
        if name == self.va_set_name:
            # Is this a mod?
            va = row[0]
            i = self.addr_iter_map.get(va)
            if i != None:
                self.vivRemove(va)
            self.vivInsert(row)
        
    def VWE_DELVASETROW(self, vw, event, einfo):
        name, va = einfo
        if name == self.va_set_name:
            self.vivRemove(va)

    def vwGetDisplayName(self):
        return self.va_set_name

class ReportView(LocationListView):
    __cols__ = (
        (None, 0, object),
        ("Address", 1, str),
    )

    def __init__(self, vw, gui, repmod, report):
        self.report = report
        self.repmod = repmod
        LocationListView.__init__(self, vw, gui)

    def vwInitModel(self, cols, modclass):
        cols = list(cols)
        for i,(cname,ctype) in enumerate(self.repmod.columns):
            cols.append((cname, len(cols), ctype))
        LocationListView.vwInitModel(self, cols, modclass)

    def vwLoad(self):
        for va, row in self.report.items():
            self.vivInsert(va, row)

    def vivInsert(self, va, row):
        pstr = self.vw.arch.pointerString(va)
        row = (va, pstr) + row
        iter = self.model.append(row)
        self.addr_iter_map[va] = iter

class StructsView(LocationListView):
    __cols__ = (
        (None, 0, object),
        ("Address",1,str),
        ("Struct Type", 2, str),
    )
    __display_name__ = "Structures"

    def vwLoad(self):
        for ltup in self.vw.getLocations(LOC_STRUCT):
            self.vivInsert(ltup[L_VA], ltup[L_TINFO])

    def vivInsert(self, va, sname):
        iter = self.model.append((va, "0x%.8x" % va, sname))
        self.addr_iter_map[va] = iter

    def VWE_ADDLOCATION(self, vw, event, einfo):
        va,size,ltype,tinfo = einfo
        if ltype == LOC_STRUCT:
            self.vivInsert(va, tinfo)

class StringsView(LocationListView):
    __cols__ = (
        (None, 0, object),
        ("Address", 1, str),
        ("String", 2, str),
    )
    __display_name__ = "Strings"

    def vwLoad(self):
        for ltup in self.vw.getLocations(LOC_STRING):
            self.vivInsert(ltup[L_VA], self.vw.reprLocation(ltup))

        for ltup in self.vw.getLocations(LOC_UNI):
            self.vivInsert(ltup[L_VA], self.vw.reprLocation(ltup))

    def VWE_ADDLOCATION(self, vw, event, einfo):
        va,size,ltype,tinfo = einfo
        if ltype in [LOC_STRING, LOC_UNI]:
            self.vivInsert(va, self.vw.reprLocation(einfo))

    def vivInsert(self, address, strbuf):
        iter = self.model.append((address, "0x%.8x" % address, strbuf))
        self.addr_iter_map[address] = iter

class FunctionsView(LocationListView):
    __model_class__ = gtk.TreeStore
    __cols__ = (
        (None, 0, object),
        ("Address", 1, str),
        ("Size", 2, int),
        ("Refs", 3, int),
        ("Function", 4, str),
    )
    __display_name__ = "Functions"

    def vivInsert(self, funcva):
        fname = self.vw.getName(funcva)
        size = self.vw.getFunctionMeta(funcva, "Size", -1)
        xcount = len(self.vw.getXrefsTo(funcva))
        iter = self.model.append(None, (funcva, "0x%.8x" % funcva, size, xcount, fname))
        self.addr_iter_map[funcva] = iter

    def VWE_ADDFUNCTION(self, vw, event, einfo):
        funcva, meta = einfo
        self.vivInsert(funcva)

    def VWE_DELFUNCTION(self, vw, event, einfo):
        funcva, meta = einfo
        self.vivRemove(funcva)

    def VWE_SETNAME(self, vw, event, einfo):
        va,name = einfo
        iter = self.addr_iter_map.get(va)
        if iter != None:
            self.model.set_value(iter, 4, name)

    def VWE_ADDXREF(self, vw, event, einfo):
        fromva, tova, rtype, rflag = einfo
        iter = self.addr_iter_map.get(tova)
        if iter != None:
            cnt = self.model.get_value(iter, 3)
            cnt += 1
            self.model.set_value(iter, 3, cnt)

    def VWE_DELXREF(self, vw, event, einfo):
        fromva, tova, rtype, rflag = einfo
        iter = self.addr_iter_map.get(tova)
        if iter != None:
            cnt = self.model.get_value(iter, 3)
            cnt -= 1
            self.model.set_value(iter, 3, cnt)

    def VWE_SETFUNCMETA(self, vw, event, einfo):
        funcva, key, value = einfo
        if key == "Size":
            iter = self.addr_iter_map.get(funcva)
            if iter != None:
                self.model.set_value(iter, 2, value)

        #FIXME handle add xref!

    def vwLoad(self):
        for f in self.vw.getFunctions():
            self.vivInsert(f)

class ImportsView(LocationListView):
    __cols__ = (
        (None, 0, object),
        ("Address", 1, str),
        ("Function", 2, str),
    )
    __display_name__ = "Imports"

    def VWE_ADDLOCATION(self, vw, event, einfo):
        va,size,ltype,tinfo = einfo
        if ltype == vivisect.LOC_IMPORT:
            self.vivInsert(va, self.vw.reprLocation(einfo))

    def vwLoad(self):
        for l in self.vw.getLocations(vivisect.LOC_IMPORT):
            self.vivInsert(l[L_VA], self.vw.reprLocation(l))

    def vivInsert(self, address, funcname):
        iter = self.model.append((address, "0x%.8x" % address, funcname))
        self.addr_iter_map[address] = iter

class ExportsView(LocationListView):
    __cols__ = (
        (None, 0, object),
        ("Address", 1, str),
        ("File Name", 2, str),
        ("Export Entry", 3, str),
    )
    __display_name__ = "Exports"

    def vwLoad(self):
        for exp in self.vw.getExports():
            self.vivInsert(exp)

    def vivInsert(self, etup):
        eva,etype,ename,efname = etup
        addrstr = self.vw.arch.pointerString(eva)
        iter = self.model.append((eva, addrstr, efname, ename))
        self.addr_iter_map[eva] = iter

    def VWE_ADDEXPORT(self, vw, event, einfo):
        self.vivInsert(einfo)

    def VWE_DELEXPORT(self, vw, event, einfo):
        va,etype,name,fname = einfo
        self.vivRemove(va)

class FilesView(LocationListView):
    __model_class__ = gtk.TreeStore
    __cols__ = (
        (None, 0, object),
        ("Filename/Segment", 1, str),
        ("Base Address", 2, str),
        ("Size", 3, int),
        ("File MD5", 4, str),
    )
    __display_name__ = "Files"

    def vwLoad(self):

        filesize = {}
        segs = self.vw.getSegments()
        for segva, segsize, segname, filename in segs:
            filesize[filename] = filesize.get(filename, 0) + segsize

        for fname in self.vw.getFiles():
            self.vivInsert(fname, filesize.get(fname, 0))

        for seg in segs:
            self.vivInsertSegment(seg)

    def vivInsert(self, fname, fsize):
        baseaddr = self.vw.getFileMeta(fname, "imagebase")
        md5sum   = self.vw.getFileMeta(fname, "md5sum")
        ptrstr = self.vw.arch.pointerString(baseaddr)
        iter = self.model.append(None, (baseaddr, fname, ptrstr, fsize, md5sum))
        self.addr_iter_map[fname] = iter

    def vivInsertSegment(self, segtup):
        """
        """
        segva, segsize, segname, filename = segtup
        ptrstr = self.vw.arch.pointerString(segva)
        iter = self.addr_iter_map.get(filename)
        self.model.append(iter, (segva, segname, ptrstr, segsize, ""))

    def VWE_ADDSEGMENT(self, vw, event, einfo):
        self.vivInsertSegment(einfo)

    def VWE_ADDFILE(self, vw, event, einfo):
        name,baseaddr,md5sum = einfo
        # FIXME filesize is going to need to go in the event...
        self.vivInsert(name,0)

    def VWE_DELSEGMENT(self, vw, event, einfo):
        #FIXME IMPLEMENT
        pass

    def VWE_DELFILE(self, vw, event, einfo):
        #FIXME IMPLEMENT
        pass

class CallersView(LocationListView):
    __model_class__ = gtk.TreeStore
    __cols__ = (
        (None, 0, object),
        ("Function", 1, str),
        ("Address", 2, str),
        ("Comment", 3, str),
        # FIXME emulate and show args!
    )

    def __init__(self, vw, gui, funcva):
        self.funcva = funcva
        LocationListView.__init__(self, vw, gui)

    def vwLoad(self):

        if self.funcva == None:
            return

        for fromva, tova, xrtype, xrflags in self.vw.getXrefsTo(self.funcva):
            if xrtype != REF_CODE:
                continue

            # if the branch is not a call, we don't care...
            if not xrflags & envi.BR_PROC:
                continue

            loc = self.vw.getLocation(fromva)

            fromfunc = "Unknown"
            fva = self.vw.getFunction(fromva)
            if fva != None:
                fromfunc = self.vw.getName(fva)

            fromstr = self.vw.arch.pointerString(fromva)

            #self.vivInsert(fromva, fromfunc, fromstr, self.vw.reprLocation(loc))
            cmnt = self.vw.getComment(fromva)
            if cmnt == None:
                cmnt = ""
            self.vivInsert(fromva, fromfunc, fromstr, cmnt)

    def vivInsert(self, fromva, fromfunc, fromstr, cmnt):
        iter = self.model.append(None, (fromva, fromfunc, fromstr, cmnt))
        self.addr_iter_map[fromva] = iter

class VivFuncParamView(VivTreeView):

    __cols__ = (
        (None, 0, int),
        (None, 1, object),
        ("Arg Type",2, str),
        ("Arg Base Name",3, str)
    )

    __editors__ = {'Arg Base Name':'editArgBaseName'}

    def __init__(self, vw, gui, fva):
        self.fva = fva
        VivTreeView.__init__(self, vw, gui)

    def vwLoad(self):
        args = self.vw.getFunctionArgs(self.fva)
        self._loadArgs(args)

    def _loadArgs(self, args):
        self.model.clear()
        i = 0
        for fatype, faname in args:
            self.model.append((i, fatype, fatype.__name__, faname))
            i += 1

    def editArgBaseName(self, rend, path, newval):
        iter = self.model.get_iter(path)
        idx = self.model.get_value(iter, 0)
        fatype = self.model.get_value(iter, 1)
        self.vw.setFunctionArg(self.fva, idx, fatype, newval, doprec=False)

    def VWE_SETFUNCMETA(self, vw, event, einfo):
        fva, key, val = einfo
        if key == 'FunctionArguments':
            self._loadArgs(val)

class VivCodeBlockView(LocationListView):
    __cols__ = (
        (None, 0, object),
        (None, 1, object),
        ('Address', 2, str),
        ('Size',    3, int),
        ('Function',4, str)
    )

    def __init__(self, vw, gui, fva=None):
        self.fva = fva
        LocationListView.__init__(self, vw, gui)

    def vwLoad(self):
        if self.fva != None:
            for cb in self.vw.getFunctionBlocks(self.fva):
                self.vivInsert(cb)
        else:
            for cb in self.getCodeBlocks():
                self.vivInsert(cb)

    def vivInsert(self, codeblock):
        cbva, cbsize, cbfunc = codeblock
        fname = self.vw.getName(cbfunc)
        bname = self.vw.getName(cbva)
        if bname == None:
            bname = 'loc_%.8x' % cbva
        self.model.append((cbva, codeblock, bname, cbsize, fname))

    def VWE_ADDCODEBLOCK(self, vw, event, einfo):
        fva, cblock = einfo
        if self.fva != None and self.fva != fva:
            return
        self.vwInsert(cblock)

    def VWE_DELCODEBLOCK(self, vw, event, einfo):
        print 'FIXME VWE_ADDCODEBLOCK in VivCodeBlocksView!'

class VivFuncMetaView(vw_views.VTreeView, viv_base.VivEventCore):

    __cols__ = (
        ('Meta Key', 0, str),
        ('Meta Repr',1, str),
    )

    __editors__ = {'Meta Repr':'editMetaValue'}

    def __init__(self, vw, gui, fva):
        self.vw = vw
        self.gui = gui
        self.fva = fva
        self.meta_iter = {}
        vw_views.VTreeView.__init__(self)
        viv_base.VivEventCore.__init__(self, vw)
        gui.addEventCore(self)

    def vwLoad(self):
        m = self.vw.getFunctionMetaDict(self.fva)
        keys = m.keys()
        keys.sort()
        for key in keys:
            val = m.get(key)
            self.vivInsert(key, val)
        

    def vivInsert(self, key, value):
        iter = self.model.append((key, repr(value)))
        self.meta_iter[key] = iter

    def editMetaValue(self, rend, path, newval):
        iter = self.model.get_iter(path)

        key = self.model.get_value(iter, 0)
        val = self.model.get_value(iter, 1)
        if val == newval:
            return

        try:
            val = eval(newval)
        except Exception, e:
            self.vw.vprint('Eval Meta Value Failed: ->%s<- (%s)' % (newval, e))
            return

        self.vw.setFunctionMeta(self.fva, key, val)

    def VWE_SETFUNCMETA(self, vw, event, einfo):
        # update our list!
        funcva, key, value = einfo
        if funcva != self.fva:
            return

        iter = self.meta_iter.get(key)
        if iter == None:
            iter = self.model.append((key, repr(value)))
            self.meta_iter[key] = iter
            return

        self.model.set_value(iter, 1, repr(value))

