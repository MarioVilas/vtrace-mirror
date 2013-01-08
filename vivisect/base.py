import Queue
import traceback
import threading

import envi
import envi.memory as e_mem
import envi.pagelookup as e_page
import envi.codeflow as e_codeflow

import vstruct.cparse as vs_cparse
import vstruct.builder as vs_builder
import vstruct.constants as vs_const

import vivisect.const as viv_const
import vivisect.impapi as viv_impapi
import vivisect.analysis as viv_analysis
import visgraph.graphcore as vg_graphcore

from envi.threads import firethread

from vivisect.exc import *
from vivisect.const import *

"""
Mostly this is a place to scuttle away some of the inner workings
of a workspace, so the outer facing API is a little cleaner.
"""
class VivEventCore(object):
    '''
    A class to facilitate event monitoring in the viv workspace.
    '''

    def __init__(self, vw):
        self._ve_vw = vw
        self._ve_ehand = [None for x in xrange(VWE_MAX)]
        self._ve_lock = threading.Lock()

        # Find and put handler functions into the list
        for name in dir(self):
            if not name.startswith('VWE_'):
                continue
            idx = getattr(viv_const, name, None)
            if idx != None:
                self._ve_ehand[idx] = getattr(self, name)

    def _ve_fireEvent(self, event, edata):
        h = self._ve_ehand[event]
        if h != None:
            try:
                h(self._ve_vw, event, edata)
            except Exception, e:
                traceback.print_exc()

    @firethread
    def _ve_fireListener(self):
        chanid = self._ve_vw.createEventChannel()
        try:
            etup = self._ve_vw.waitForEvent(chanid)
            while etup != None:
                self._ve_lock.acquire()
                self._ve_lock.release()

                self._ve_fireEvent(*etup)

                etup = self._ve_vw.waitForEvent(chanid)

        finally:
            self._ve_vw.deleteEventChannel(chanid)

    def _ve_freezeEvents(self):
        self._ve_lock.acquire()

    def _ve_thawEvents(self):
        self._ve_lock.release()


class VivEventDist(VivEventCore):
    '''
    Similar to an event core, but does optimized distribution
    to a set of sub eventcore objects (think GUI windows...)
    '''
    def __init__(self, vw):
        VivEventCore.__init__(self, vw)
        self._ve_subs = [ [] for x in xrange(VWE_MAX) ]

        self.addEventCore(self)

        # event distributors pretty much always need a thread
        self._ve_fireListener()

    def addEventCore(self, core):
        for i in xrange(VWE_MAX):
            h = core._ve_ehand[i]
            if h != None:
                self._ve_subs[i].append(h)

    def delEventCore(self, core):
        for i in xrange(VWE_MAX):
            h = core._ve_ehand[i]
            if h != None:
                self._ve_subs[i].remove(h)

    def _ve_fireEvent(self, event, edata):
        '''
        We don't have events of our own, we just hand them down.
        '''
        hlist = self._ve_subs[event]
        for h in hlist:
            try:
                h(self._ve_vw, event, edata)
            except Exception, e:
                traceback.print_exc()

        VivEventCore._ve_fireEvent(self, event, edata)

class VivWorkspaceCore(object,viv_impapi.ImportApi):

    def __init__(self):
        viv_impapi.ImportApi.__init__(self)
        self.loclist = []
        self.locmap   = e_page.MapLookup()
        self.blockmap = e_page.MapLookup()
        self._mods_loaded = False

        self._call_uniq = {}
        self._call_graph = vg_graphcore.Graph()
        # Just in case of the GUI... :)
        self._call_graph.setMeta('bgcolor', '#000')
        self._call_graph.setMeta('nodecolor', '#00ff00')
        self._call_graph.setMeta('edgecolor', '#00802b')

        self._event_list = []
        self._event_saved = 0 # The index of the last "save" event...

        # Give ourself a structure namespace!
        self.vsbuilder = vs_builder.VStructBuilder()
        self.vsconsts  = vs_const.VSConstResolver()

    def _addCallEdge(self, fva1, fva2):
        etup = (fva1, fva2)
        if not self._call_uniq.get( etup ):
            self._call_graph.addEdge( fva1, fva2 )
            self._call_uniq[ etup ] = True

    def _snapInAnalysisModules(self):
        '''
        Snap in the analysis modules which are appropriate for the 
        format/architecture/platform of this workspace by calling
        '''
        if self._mods_loaded:
            return

        viv_analysis.addAnalysisModules(self)
        self._mods_loaded = True

    def _createSaveMark(self):
        '''
        Update the index of the most recent saved event to the current
        length of the event list (called after successful save)..
        '''
        self._event_saved = len(self._event_list)

    def _handleADDLOCATION(self, loc):
        lva, lsize, ltype, linfo = loc
        self.locmap.setMapLookup(lva, lsize, loc)
        self.loclist.append(loc)

        # A few special handling cases...
        if ltype == LOC_IMPORT:
            # Check if the import is registered in NoReturnApis
            if self.getMeta('NoReturnApis', {}).get(linfo.lower()):
                self.cfctx.addNoReturnAddr( lva )

    def _handleDELLOCATION(self, loc):
        # FIXME delete xrefs
        lva, lsize, ltype, linfo = loc
        self.locmap.setMapLookup(lva, lsize, None)
        self.loclist.remove(loc)

    def _handleADDSEGMENT(self, einfo):
        self.segments.append(einfo)

    def _handleADDRELOC(self, einfo):
        self.reloc_by_va[einfo[0]] = einfo[1]
        self.relocations.append(einfo)

    def _handleADDMODULE(self, einfo):
        print('DEPRICATED (ADDMODULE) ignored: %s' % einfo)

    def _handleDELMODULE(self, einfo):
        print('DEPRICATED (DELMODULE) ignored: %s' % einfo)

    def _handleADDFMODULE(self, einfo):
        print('DEPRICATED (ADDFMODULE) ignored: %s' % einfo)

    def _handleDELFMODULE(self, einfo):
        print('DEPRICATED (DELFMODULE) ignored: %s' % einfo)

    def _handleADDFUNCTION(self, einfo):
        va, meta = einfo
        self._initFunction(va)

        # Tell the codeflow subsystem about this one!
        calls_from = meta.get('CallsFrom')
        self.cfctx.addFunctionDef(va, calls_from)

        self.funcmeta[va] = meta

        for name,value in meta.items():
            mcbname = "_fmcb_%s" % name.split(':')[0]
            mcb = getattr(self, mcbname, None)
            if mcb != None:
                mcb(va, name, value)

        self._call_graph.addNode( nodeid=va, repr=self.getName( va ) ) #, color='#00ff00' )

    def _handleDELFUNCTION(self, einfo):
        self.funcmeta.pop(einfo)
        self.func_args.pop(einfo)
        self.codeblocks_by_funcva.pop(einfo)
        self._call_graph.delNode( einfo )

    def _handleSETFUNCMETA(self, einfo):
        funcva, name, value = einfo
        m = self.funcmeta.get(funcva)
        if m != None:
            m[name] = value
        mcbname = "_fmcb_%s" % name.split(':')[0]
        mcb = getattr(self, mcbname, None)
        if mcb != None:
            mcb(funcva, name, value)

    def _handleADDCODEBLOCK(self, einfo):
        va,size,funcva = einfo
        self.blockmap.setMapLookup(va, size, einfo)
        self.codeblocks_by_funcva.get(funcva).append(einfo)
        self.codeblocks.append(einfo)

    def _handleDELCODEBLOCK(self, cb):
        va,size,funcva = cb
        self.codeblocks.remove(cb)
        self.codeblocks_by_funcva.get(cb[CB_FUNCVA]).remove(cb)
        self.blockmap.setMapLookup(va, size, None)

    def _handleADDXREF(self, einfo):
        fromva, tova, reftype, rflags = einfo
        xr_to = self.xrefs_by_to.get(tova, None)
        xr_from = self.xrefs_by_from.get(fromva, None)
        if xr_to == None:
            xr_to = []
            self.xrefs_by_to[tova] = xr_to

        if xr_from == None:
            xr_from = []
            self.xrefs_by_from[fromva] = xr_from

        if einfo not in xr_to: # Just check one for now
            xr_to.append(einfo)
            xr_from.append(einfo)
            self.xrefs.append(einfo)

    def _handleDELXREF(self, einfo):
        fromva, tova, reftype = einfo
        self.xrefs_by_to[tova].remove(einfo)
        self.xrefs_by_from[fromva].remove(einfo)

    def _handleSETNAME(self, einfo):
        va,name = einfo
        if name == None:
            oldname = self.name_by_va.pop(va, None)
            self.va_by_name.pop(oldname, None)
        else:
            self.va_by_name[name] = va
            self.name_by_va[va] = name

        if self.isFunction( va ):
            self._call_graph.setNodeInfo( va, 'repr', name )

    def _handleADDMMAP(self, einfo):
        va, perms, fname, mbytes = einfo
        e_mem.MemoryObject.addMemoryMap(self, va, perms, fname, mbytes)

        blen = len(mbytes)
        self.locmap.initMapLookup(va, blen)
        self.blockmap.initMapLookup(va, blen)

    def _handleADDEXPORT(self, einfo):
        va, etype, name, filename = einfo
        self.exports.append(einfo)
        self.exports_by_va[va] = einfo
        fullname = "%s.%s" % (filename,name)
        self.makeName(va, fullname)

    def _handleSETMETA(self, einfo):
        name,value = einfo
        # See if there's a callback handler for this meta set.
        # For "meta namespaces" use the first part to find the
        # callback name....
        mcbname = "_mcb_%s" % name.split(':')[0]
        mcb = getattr(self, mcbname, None)
        if mcb != None:
            mcb(name, value)
        self.metadata[name] = value

    def _handleCOMMENT(self, einfo):
        va,comment = einfo
        if comment == None:
            self.comments.pop(va)
        else:
            self.comments[va] = comment

    def _handleADDFILE(self, einfo):
        normname, imagebase, md5sum = einfo
        self.filemeta[normname] = {"md5sum":md5sum,"imagebase":imagebase}

    def _handleSETFILEMETA(self, einfo):
        fname, key, value = einfo
        self.filemeta.get(fname)[key] = value

    def _handleADDCOLOR(self, coltup):
        mapname, colmap = coltup
        self.colormaps[mapname] = colmap

    def _handleDELCOLOR(self, mapname):
        self.colormaps.pop(mapname)

    def _handleADDVASET(self, argtup):
        name, defs, rows = argtup
        self.vasetdefs[name] = defs
        vals = {}
        for row in rows:
            vals[row[0]] = row
        self.vasets[name] = vals

    def _handleDELVASET(self, setname):
        self.vasetdefs.pop(setname)
        self.vasets.pop(setname)

    def _handleADDFREF(self, frtup):
        va, idx, val = frtup
        self.frefs[(va,idx)] = val

    def _handleDELFREF(self, frtup):
        va, idx, val = frtup
        self.frefs.pop((va,idx), None)

    def _handleSETVASETROW(self, argtup):
        name, row = argtup
        self.vasets[name][row[0]] = row

    def _handleDELVASETROW(self, argtup):
        name, va = argtup
        self.vasets[name].pop(va, None)

    def _handleADDFSIG(self, einfo):
        print('DEPRICATED (ADDFSIG) ignored: %s' % (einfo,))

    def _handleFOLLOWME(self, va):
        pass

    def _handleCHAT(self, msgtup):
        # FIXME make a GUI window for this...
        user, msg = msgtup
        self.vprint('%s: %s' % (user, msg))

    def _handleSYMHINT(self, msgtup):
        va, idx, hint = msgtup
        if hint == None:
            self.symhints.pop((va,idx), None)
        else:
            self.symhints[(va,idx)] = hint

    def _handleSETFUNCARGS(self, einfo):
        fva, args = einfo
        self.func_args[fva] = args

    def _initEventHandlers(self):
        self.ehand = [None for x in xrange(VWE_MAX)]
        self.ehand[VWE_ADDLOCATION] = self._handleADDLOCATION
        self.ehand[VWE_DELLOCATION] = self._handleDELLOCATION
        self.ehand[VWE_ADDSEGMENT] = self._handleADDSEGMENT
        self.ehand[VWE_DELSEGMENT] = None
        self.ehand[VWE_ADDRELOC] = self._handleADDRELOC
        self.ehand[VWE_DELRELOC] = None
        self.ehand[VWE_ADDMODULE] = self._handleADDMODULE
        self.ehand[VWE_DELMODULE] = self._handleDELMODULE
        self.ehand[VWE_ADDFMODULE] = self._handleADDFMODULE
        self.ehand[VWE_DELFMODULE] = self._handleDELFMODULE
        self.ehand[VWE_ADDFUNCTION] = self._handleADDFUNCTION
        self.ehand[VWE_DELFUNCTION] = self._handleDELFUNCTION
        self.ehand[VWE_SETFUNCARGS] = self._handleSETFUNCARGS
        self.ehand[VWE_SETFUNCMETA] = self._handleSETFUNCMETA
        self.ehand[VWE_ADDCODEBLOCK] = self._handleADDCODEBLOCK
        self.ehand[VWE_DELCODEBLOCK] = self._handleDELCODEBLOCK
        self.ehand[VWE_ADDXREF] = self._handleADDXREF
        self.ehand[VWE_DELXREF] = self._handleDELXREF
        self.ehand[VWE_SETNAME] = self._handleSETNAME
        self.ehand[VWE_ADDMMAP] = self._handleADDMMAP
        self.ehand[VWE_DELMMAP] = None
        self.ehand[VWE_ADDEXPORT] = self._handleADDEXPORT
        self.ehand[VWE_DELEXPORT] = None
        self.ehand[VWE_SETMETA] = self._handleSETMETA
        self.ehand[VWE_COMMENT] = self._handleCOMMENT
        self.ehand[VWE_ADDFILE] = self._handleADDFILE
        self.ehand[VWE_DELFILE] = None
        self.ehand[VWE_SETFILEMETA] = self._handleSETFILEMETA
        self.ehand[VWE_ADDCOLOR] = self._handleADDCOLOR
        self.ehand[VWE_DELCOLOR] = self._handleDELCOLOR
        self.ehand[VWE_ADDVASET] = self._handleADDVASET
        self.ehand[VWE_DELVASET] = self._handleDELVASET
        self.ehand[VWE_SETVASETROW] = self._handleSETVASETROW
        self.ehand[VWE_DELVASETROW] = self._handleDELVASETROW
        self.ehand[VWE_ADDFSIG] = self._handleADDFSIG
        self.ehand[VWE_ADDFREF] = self._handleADDFREF
        self.ehand[VWE_DELFREF] = self._handleDELFREF
        self.ehand[VWE_FOLLOWME] = self._handleFOLLOWME
        self.ehand[VWE_CHAT]     = self._handleCHAT
        self.ehand[VWE_SYMHINT]  = self._handleSYMHINT

    def _fireEvent(self, event, einfo, local=False, skip=None):
        '''
        Fire an event down the hole.  "local" specifies that this is
        being called on a client (self.server != None) but we got it
        from the server in the first place so no need to send it back.

        skip is used to tell the server to bypass our channelid when
        putting the event into channel queues (we took care of our own).
        '''

        try:
            # Do our main event processing
            self.ehand[event](einfo)

            # If we're supposed to call a server, do that.
            if self.server != None and local == False:
                self.server._fireEvent(event, einfo, skip=self.rchan)

            # FIXME perhaps we should only process events *via* our server
            # if we have one? Just to confirm it works before we apply it...
            self._event_list.append((event, einfo))

            for id,q in self.chan_lookup.items():
                if id == skip:
                    continue
                try:
                    q.put_nowait((event, einfo))
                except Queue.Full, e:
                    print "FULL QUEUE DO SOMETHING"

        except Exception, e:
            traceback.print_exc()
            print "THIS SHOULD NEVER HAPPEN"

    def _initFunction(self, funcva):
        # Internal function to initialize all datastructures necissary for
        # a function, but only if they haven't been done already.
        if self.funcmeta.get(funcva) == None:
            self.funcmeta[funcva] = {} # His metadata
            self.codeblocks_by_funcva[funcva] = [] # Init code block list

    #def _loadImportApi(self, apidict):
        #self._imp_api.update( apidict )

#################################################################
#
#  setMeta key callbacks
#
    def _mcb_Architecture(self, name, value):
        self.arch = envi.getArchModule(value)
        self.psize = self.arch.getPointerSize()
        self.imem_psize = self.psize

    def _mcb_ustruct(self, name, ssrc):
        # All meta values in the "ustruct" namespace are user defined
        # structure defintions in C.
        sname = name.split(':')[1]
        ctor = vs_cparse.ctorFromCSource( ssrc )
        self.vsbuilder.addVStructCtor( sname, ctor )

    def _fmcb_Thunk(self, funcva, th, thunkname):
        # If the function being made a thunk is registered
        # in NoReturnApis, update codeflow...
        if self.getMeta('NoReturnApis').get( thunkname.lower() ):
            self.cfctx.addNoReturnAddr( funcva )

    def _fmcb_CallsFrom(self, funcva, th, callsfrom):
        for va in callsfrom:
            f2va = self.getFunction( va )
            if f2va != None:
                self._addCallEdge( funcva, f2va )

class VivCodeFlowContext(e_codeflow.CodeFlowContext):

    def _cb_noflow(self, srcva, dstva):
        vw = self._mem
        loc = vw.getLocation( srcva )
        if loc == None:
            return

        lva,lsize,ltype,linfo = loc
        if ltype != LOC_OP:
            return

        # Update the location def for NOFALL bit
        vw.addLocation(lva, lsize, ltype, linfo | envi.IF_NOFALL)
        vw.setVaSetRow('NoReturnCalls', (lva,))

    # NOTE: self._mem is the viv workspace...
    def _cb_opcode(self, va, op, branches):

        if self._mem.getLocation(va) == None:
            self._mem.makeOpcode(va, op=op)
            return branches

        return ()

    def _cb_function(self, fva, fmeta):

        vw = self._mem
        if vw.isFunction(fva):
            return

        # If the function doesn't have a name, make one
        if vw.getName(fva) == None:
            vw.makeName(fva, "sub_%.8x" % fva)

        vw._fireEvent(VWE_ADDFUNCTION, (fva,fmeta))

        # Go through the function analysis modules in order
        for fmname in vw.fmodlist:
            fmod = vw.fmods.get(fmname)
            try:
                fmod.analyzeFunction(vw, fva)
            except Exception, e:
                traceback.print_exc()
                vw.vprint("Function Analysis Exception %s: %s" % (fmod.__name__, e))
                vw.setFunctionMeta(fva, "%s fail" % fmod.__name__, traceback.format_exc())

        fname = vw.getName( fva )
        if vw.getMeta('NoReturnApis').get( fname.lower() ):
            self._cf_noret[ fva ] = True

    def _cb_branchtable(self, tablebase, tableva, destva):

        if tablebase != tableva and self._mem.getXrefsTo(tableva):
            return False

        if self._mem.getLocation(tableva) == None:
            self._mem.makePointer(tableva, tova=destva, follow=False)
    
        return True
