
"""

Yay!  It's NOT IDA!!!1!!1!one!

"""

import os
import sys
import time
import Queue
import string
import struct
import weakref
import traceback
import threading
from ConfigParser import ConfigParser
from StringIO import StringIO
from collections import deque

# The envi imports...
import envi
import envi.bits as e_bits
import envi.memory as e_mem
import envi.config as e_config
import envi.bytesig as e_bytesig
import envi.resolver as e_resolv
import envi.codeflow as e_codeflow

import vstruct
import vstruct.builder as vs_builder
import vstruct.constants as vs_const
import vstruct.primitives as vs_prims


import vivisect.base as viv_base
import vivisect.impemu as viv_imp
import vivisect.config as viv_conf
import vivisect.export as viv_export
import vivisect.parsers as viv_parsers
import vivisect.impemu.emufunc as viv_emufunc
import vivisect.impemu.impmagic as viv_impmagic

from vivisect.const import *
from vivisect.exc import *

class VivWorkspace(e_mem.MemoryObject, viv_base.VivWorkspaceCore):

    def __init__(self):

        e_mem.MemoryObject.__init__(self)
        viv_base.VivWorkspaceCore.__init__(self)

        self.vivhome = e_config.gethomedir(".viv")
        self._viv_gui = None    # If a gui is running, he will put a ref here...

        # Setup the DB
        self.verbose = False
        self.saved = True
        self.server = None
        self.rchan = None
        self.chanlock = threading.Lock()

        self.arch = None # The placeholder for the Envi architecture module
        self.psize = None # Used so much, optimization is appropriate

        self.config = e_config.EnviConfig()
        self.config.readstr( viv_conf.defaults )

        # Give ourself a structure namespace!
        self.vsbuilder = vs_builder.VStructBuilder()
        self.vsconsts  = vs_const.VSConstResolver()

        # Ideally, *none* of these are modified except by _handleFOO funcs...
        self.segments = []
        self.exports = []
        self.imports = []
        self.codeblocks = []
        self.relocations = []

        self.xrefs = []
        self.xrefs_by_to = {}
        self.xrefs_by_from = {}

        self.metadata = {}
        self.comments = {} # Comment by VA.
        self.symhints = {}

        self.filemeta = {} # Metadata Dicts stored by filename

        self.cfctx = viv_base.VivCodeFlowContext(self)

        self.va_by_name = {}
        self.name_by_va = {}
        self.codeblocks_by_funcva = {}
        self.exports_by_va = {}
        self.colormaps = {}
        self.vasetdefs = {}
        self.vasets = {}
        self.reloc_by_va = {}

        self.func_args = {}
        self.funcmeta = {} # Function metadata stored in the workspace
        self.frefs = {}

        # Extended analysis modules
        self.amods = {}
        self.amodlist = []
        # Extended *function* analysis modules
        self.fmods = {}
        self.fmodlist = []

        self.chan_lookup = {}
        self.nextchanid = 1

        # The function entry signature decision tree
        # FIXME add to export
        self.sigtree = e_bytesig.SignatureTree()
        self.siglist = []

        self.impmod = None # our import emulation namespace module

        self._initEventHandlers()

        # Some core meta types that exist
        self.setMeta('NonExiters', {})
        self.setMeta('ImportEmulation', None)
        self.setMeta('SymbolikImportEmulation', None)

        # Default to basic file storage
        self.setMeta("StorageModule", "vivisect.storage.basicfile")

        # There are a few default va sets for use in analysis
        self.addVaSet('EntryPoints', (('va',long),))
        self.addVaSet("Emulation Anomalies", (("va",int),("Message",str)))
        self.addVaSet("Bookmarks", (("va",long),("Bookmark Name", str)))

    def vprint(self, msg):
        print msg

    def loadWorkspace(self, wsname):
        mname = self.getMeta("StorageModule")
        mod = self.loadModule(mname)
        mod.loadWorkspace(self, wsname)
        self.setMeta("StorageName", wsname)
        # The event list thusfar came *only* from the load...
        self._createSaveMark()
        # Snapin our analysis modules
        self._snapInAnalysisModules()

    def addFref(self, fva, va, idx, val):
        """
        Add a reference from the operand at virtual address 'va'
        index 'idx' to a function local offset.  Positive values
        (beginning with 0) are considered argument references.  Negative
        values are considered function local storage and are relative to
        the stack pointer at function entry.
        """
        # FIXME this should probably be an argument
        r = (va,idx,val)

        if val < 0:
            # If this function doesn't know about the local, lets tell it!
            absval = abs(val)
            ltype,lname = self.getFunctionLocal(fva, absval)
            if lname == None:
                self.setFunctionLocal(fva, val, None, 'local')

        self._fireEvent(VWE_ADDFREF, r)

    def getFref(self, va, idx):
        """
        Get back the fref value (or None) for the given operand index
        from the instruction at va.
        """
        return self.frefs.get((va,idx))

    def getEmuFunc(self, fva):
        '''
        Return an emufunc object to best serve to wrap the specified
        workspace function.  This will check for functions which are
        'thunks' and may return import emufunc's for them etc...
        '''
        # lets check for a wrapper...
        wraps = self.getFunctionMeta(fva, "Thunk", None)
        if wraps != None:
            ret = self.getImpEmuFunc(wraps)
            if ret != None:
                return ret

        return viv_emufunc.WrapperFunc(self, fva)

    def getImpEmuFunc(self, impname):
        """
        Return an EmuFunc object from the impemu subsystem for
        the given import entry ("libname.funcname").
        If libname == "*", the resolver will use the workspace
        meta key "DepLibs" as a list of possible libraries to
        search.
        """
        if self.impmod == None:
            return None

        # FIXME try out caching these...

        nameparts = impname.split(".")
        fname = nameparts[-1]

        if nameparts[0] != "*":

            # First lets check for a straight up implementation
            ret = vstruct.resolve(self.impmod, nameparts) 

            if ret != None:
                ret = ret()

            return ret

        # We are now looing for a *.foo import

        # Lets check the known deplibs to see
        # if any of them contain our function...
        dl = self.getMeta("DepLibs", None)
        if dl != None:
            for name in dl:
                ret = vstruct.resolve(self.impmod, (name,fname))
                if ret != None:
                    return ret()

        # Lets see if we can find it in our workspace and at
        # then we will know which module it was from...
        # FIXME isn't this slow?  can't we just do it once for each loaded file?
        for eva,etype,ename,efname in self.getExports():
            ret = vstruct.resolve(self.impmod, (efname,fname))
            if ret != None:
                return ret()

        return None

    def getEmulator(self, logwrite=False, logread=False):
        """
        Get an instance of a WorkspaceEmulator for this workspace.

        Use logread/logwrite to enable memory access tracking.
        """
        arch = self.getMeta("Architecture")
        eclass = viv_imp.workspace_emus.get(arch)
        if eclass == None:
            raise Exception("WorkspaceEmulation not supported on %s yet!" % arch)
        return eclass(self, logwrite=logwrite, logread=logread)

    def addLibraryDependancy(self, libname):
        """
        Add a *normalized* library name to the import search
        chain for this binary.  This is only needed for formats
        whose imports don't explicitly state their library name.
        """
        # FIXME this needs to be event enabled... either plumb it special,
        # or allow the get/append/set race...
        dl = self.getMeta("DepLibs", None)
        if dl == None:
            dl = []
        dl.append(libname)
        self.setMeta("DepLibs", dl)

    def getOption(self, section, option, default=None):
        """
        Get a config option from the workspace as a string.
        """
        if not self.config.has_section(section):
            return default
        if not self.config.has_option(section, option):
            return default
        return self.config.get(section, option)

    def getOptionInt(self, section, option, default=None):
        """
        Get a config option from the workspace as an int.
        """
        if not self.config.has_section(section):
            return default
        if not self.config.has_option(section, option):
            return default
        return int(self.config.get(section, option), 0)

    def getOptionBool(self, section, option, default=None):
        """
        Get a config option from the workspace as a boolean.
        """
        if not self.config.has_section(section):
            return default
        if not self.config.has_option(section, option):
            return default
        return self.config.getboolean(section, option)

    def setOption(self, secname, optname, value):
        """
        Set a workspace configuration option.

        Example:
            vw.setOption('sectname', 'optname', 'value')
        """
        if not self.config.has_section(secname):
            self.config.add_section(secname)
        self.config.set(secname, optname, str(value))

    def setComment(self, va, comment):
        '''
        Set the humon readable comment for a given virtual.
        Comments will be displayed by the code renderer, and
        are an important part of this balanced breakfast.

        Example:
            vw.setComment(callva, "This actually calls FOO...")
        '''
        self._fireEvent(VWE_COMMENT, (va,comment))

    def getComment(self, va):
        '''
        Returns the comment string (or None) for a given
        virtual address.

        Example:
            cmnt = vw.getComment(va)
            print('COMMENT: %s' % cmnt)
        '''
        return self.comments.get(va)

    def getComments(self):
        '''
        Retrieve all the comments in the viv workspace as 
        (va, cmnt) tuples.

        Example:
            for va,cmnt in vw.getComments():
                print 'Comment at 0x%.8x: %s' % (va, cmnt)
        '''
        return self.comments.items()

    def addRelocation(self, va, rtype):
        """
        Add a relocation entry for tracking.
        """
        self._fireEvent(VWE_ADDRELOC, (va, rtype))

    def getRelocations(self):
        """
        Get the current list of relocation entries.
        """
        return self.relocations

    def getRelocation(self, va):
        """
        Return the type of relocation at the specified
        VA or None if there isn't a relocation entry for
        the address.
        """
        return self.reloc_by_va.get(va)

    def pointerString(self, va):
        return self.arch.pointerString(va)

    def getAnalysisModuleNames(self):
        return list(self.amodlist)

    def getFuncAnalysisModuleNames(self):
        return list(self.fmodlist)

    def addFunctionSignatureBytes(self, bytes, mask=None):
        """
        Add a function signature entry by bytes.  This is mostly used by
        file parsers/loaders to manually tell the workspace about known
        entry signature types.

        see envi.bytesig for details.
        """
        self.sigtree.addSignature(bytes, mask)
        self.siglist.append((bytes,mask))

    def isFunctionSignature(self, va):
        """
        Check if the specified va is a function entry signature
        according to the current entry point signature tree...
        """
        if not self.isValidPointer(va):
            return False
        offset, bytes = self.getByteDef(va)
        return self.sigtree.isSignature(bytes, offset=offset)

    def addNonExiter(self, funcname):
        """
        Inform vivisect code-flow disassembly that any call target
        which matches the specified name ("funcname" or "libname.funcname"
        for imports) does *not* exit and code-flow should be stopped...
        """
        #FIXME these should be vtrace style "libname.funcname"
        #FIXME this will break for remote
        self.getMeta("NonExiters")[funcname] = True

    def isNonExiter(self, targva):
        """
        If the target va is a function or an import, return True
        if the function/import does NOT exit.
        """
        targname = self.getName(targva)
        return self.getMeta("NonExiters").get(targname, False)

    def addAnalysisModule(self, modname):
        """
        Add an analysis module by python import path
        """
        if self.amods.has_key(modname):
            return
        mod = self.loadModule(modname)
        self.amods[modname] = mod
        self.amodlist.append(modname)
        # If the module has a config, add it to ours.
        if hasattr(mod, "config"):
            self.mergeConfig(mod.config)

    def delAnalysisModule(self, modname):
        """
        Remove an analysis module from the list used during analysis()
        """
        if not self.amods.has_key(modname):
            raise Exception("Unknown Module in delAnalysisModule: %s" % modname)
        x = self.amods.pop(modname, None)
        if x != None:
            self.amodlist.remove(modname)

    def loadModule(self, modname):
        __import__(modname)
        return sys.modules[modname]

    def mergeConfig(self, configbuf):
        """
        Add the options from the given config to the workspace config.
        If options already exist, assume that they were set by the user
        and do *not* over-ride.
        """
        x = StringIO(configbuf)
        cfg = ConfigParser()
        cfg.readfp(x)
        for sec in cfg.sections():
            if not self.config.has_section(sec):
                self.config.add_section(sec)
            for opt in cfg.options(sec):
                if not self.config.has_option(sec, opt):
                    val = cfg.get(sec, opt)
                    self.config.set(sec, opt, val)

    def addFuncAnalysisModule(self, modname):
        """
        Snap in a per-function analysis module (by name) which
        will be triggered during the creation of a new function
        (makeFunction).
        """
        if self.fmods.has_key(modname):
            return
        mod = self.loadModule(modname)
        self.fmods[modname] = mod
        self.fmodlist.append(modname)
        # FIXME sort out this config bullshit!
        if hasattr(mod, "config"):
            self.mergeConfig(mod.config)

    def delFuncAnalysisModule(self, modname):
        '''
        Remove a currently registered function analysis module.

        Example:
            vw.delFuncAnalysisModule('mypkg.mymod')
        '''
        if not self.fmods.has_key(modname):
            raise Exception("Unknown Module in delAnalysisModule: %s" % modname)
        x = self.fmods.pop(modname, None)
        if x != None:
            self.fmodlist.remove(modname)

    def createEventChannel(self):
        self.chanlock.acquire()
        try:
            chanid = self.nextchanid
            self.nextchanid += 1
        finally:
            self.chanlock.release()
        self.chan_lookup[chanid] = Queue.Queue()
        return chanid

    def importWorkspace(self, wsevents):
        """
        Import and initialize data from the given vivisect workspace
        export.
        """
        # If they hand us a dict, it's an old-style viv file.
        # process the old style dictionary and re-save out an
        # event list.
        if isinstance(wsevents, dict):
            self.vprint('Converting old style viv file! (This may take a moment)')
            viv_export.vivimport(self, wsevents)
            self.saveWorkspace(fullsave=True)
            return

        # During import, if we have a server, be sure not to notify
        # the server about the events he just gave us...
        local = False
        if self.server != None:
            local = True

        # Process the events from the import data...
        fe = self._fireEvent
        for event, einfo in wsevents:
            fe(event, einfo, local=local)
        return

    def exportWorkspace(self):
        '''
        Return the (probably big) list of events which define this
        workspace.
        '''
        return self._event_list

    def exportWorkspaceChanges(self):
        '''
        Export the list of events which have been applied to the
        workspace since the last save.
        '''
        return self._event_list[self._event_saved:]

    def initWorkspaceClient(self, remotevw):
        """
        Initialize this workspace as a workspace
        client to the given (potentially cobra remote)
        workspace object.
        """
        uname = e_config.getusername()
        self.server = remotevw
        self.rchan = remotevw.createEventChannel()

        self.server.vprint('%s connecting...' % uname)
        wsevents = self.server.exportWorkspace()
        self.importWorkspace(wsevents)
        self.server.vprint('%s connection complete!' % uname)

        thr = threading.Thread(target=self._clientThread)
        thr.setDaemon(True)
        thr.start()

    def _clientThread(self):
        """
        The thread that monitors events on a server to stay
        in sync.
        """
        if self.server == None:
            raise Exception("_clientThread() with no server?!?!")

        while self.server != None:
            event, einfo = self.server.waitForEvent(self.rchan)
            self._fireEvent(event, einfo, local=True)

    def waitForEvent(self, chanid, timeout=None):
        """
        Return an event,meta tuple.
        """
        q = self.chan_lookup.get(chanid)
        if q == None:
            raise Exception("Invalid Channel")
        return q.get(timeout=timeout)

    def deleteEventChannel(self, chanid):
        """
        Remove a previously allocated event channel from
        the workspace.
        """
        self.chan_lookup.pop(chanid)

    def reprVa(self, va):
        """
        A quick way for scripts to get a string for a given virtual address.
        """
        loc = self.getLocation(va)
        if loc != None:
            return self.reprLocation(loc)
        return "None"

    def reprLocation(self, loctup):
        lva,lsize,ltype,tinfo = loctup
        if ltype == LOC_OP:
            op = self.parseOpcode(lva)
            return repr(op)

        elif ltype == LOC_STRING:
            return repr(self.readMemory(lva, lsize))

        elif ltype == LOC_UNI:
            #FIXME super ghetto "simple" unicode handling for now
            bytes = self.readMemory(lva, lsize)
            return "u'%s'" % string.join(bytes.split("\x00"),sep="")

        elif ltype == LOC_STRUCT:
            lstruct = self.getStructure(lva, tinfo)
            return repr(lstruct)

        elif ltype == LOC_NUMBER:
            hexstr = "0x%%.%dx" % lsize
            hexstr = hexstr % tinfo
            if lsize == 1:
                return "BYTE: %d (%s)" % (tinfo, hexstr)
            else:
                return "%d BYTES: %d (%s)" % (lsize, tinfo, hexstr)

        elif ltype == LOC_IMPORT:
            return "IMPORT: %s" % tinfo

        elif ltype == LOC_POINTER:
            return "PTR: %s" % self.arch.pointerString(self.getXrefsFrom(lva)[0][XR_TO])

        else:
            n = self.getName(lva)
            if n != None:
                return n
            return self.readMemory(lva, lsize).encode('hex')

    def followPointer(self, va):
        """
        Do pointer analysis and folllow up the recomendation
        by creating locations etc...
        """
        ltype = self.analyzePointer(va)
        if ltype == None:
            return False

        # Note, we only implement the types possibly
        # returned from analyzePointer...
        if ltype == LOC_OP:
            # NOTE: currently analyzePointer returns LOC_OP
            # based on function entries, lets make a func too...
            self.makeFunction(va)
            return True

        elif ltype == LOC_STRING:
            self.makeString(va)
            return True

        elif ltype == LOC_UNI:
            self.makeUnicode(va)
            return True

        return False
         
    def analyze(self):
        """
        Call this to ask any available analysis modules
        to do their thing...
        """
        if self.verbose: self.vprint('Beginning analysis...')
        if self.verbose: self.vprint('...analyzing exports.')

        starttime = time.time()

        for eva in self.getEntryPoints():
            if self.isFunction(eva):
                continue
            if not self.probeMemory(eva, 1, e_mem.MM_EXEC):
                continue
            self.makeFunction(eva)

        if self.verbose: self.vprint('...analyzing pointers.')

        # Now, lets find likely free-hanging pointers
        for addr, pval in self.findPointers():
            try:
                self.followPointer(pval)
                if self.getLocation(addr) == None:
                    if not self.isExecutable(addr):
                        self.makePointer(addr)
            except Exception, e:
                if self.verbose: self.vprint("followPointer() failed for 0x%.8x (pval: 0x%.8x)" % (addr,pval))

        # Now lets engage any extended analysis modules.  If any modules return
        # true, they managed to change things and we should run again...
        for mname in self.amodlist:
            mod = self.amods.get(mname)
            if self.verbose: self.vprint("Extended Analysis: %s" % mod.__name__)
            try:
                mod.analyze(self)
            except Exception, e:
                traceback.print_exc()
                self.vprint("Extended Analysis Exception %s: %s" % (mod.__name__,e))

        endtime = time.time()
        if self.verbose: self.vprint('...analysis complete! (%d sec)' % (endtime-starttime))

    def getImports(self):
        """
        Return a list of imports in location tuple format.
        """
        return self.getLocations(LOC_IMPORT)

    def makeImport(self, va, libname, impname):
        """
        Add an import entry.
        """
        libname = self.normFileName(libname)
        tinfo = "%s.%s" % (libname, impname)
        self.makeName(va, "%s_%.8x" % (tinfo, va))
        return self.addLocation(va, self.psize, LOC_IMPORT, tinfo=tinfo)

    def getExports(self):
        """
        Return a list of exports in (va,etype,name,filename) tuples.
        """
        return list(self.exports)

    def addExport(self, va, etype, name, filename):
        """
        Add an already created export object.
        """
        rname = "%s.%s" % (filename,name)
        if self.vaByName(rname) != None:
            raise Exception("Duplicate Name: %s" % rname)
        self._fireEvent(VWE_ADDEXPORT, (va,etype,name,filename))

    def getExport(self, va):
        """
        Get a reference to the export object at the given va
        (or none).
        """
        return self.exports_by_va.get(va)

    def findPointers(self):
        """
        Search through all currently "undefined" space and see
        if you can find pointers there...  Returns a list of tuples
        where the tuple is (<ptr at>,<pts to>).
        """
        ret = []
        size = self.psize

        for mva, msize, mperm, mname in self.getMemoryMaps():

            maxsize = msize - size
            offset, bytes = self.getByteDef(mva)
            while offset + size < maxsize:
                va = mva + offset
                loctup = self.getLocation(va)
                if loctup != None:
                    offset += loctup[L_SIZE]
                    continue

                x = e_bits.parsebytes(bytes, offset, size)
                if self.isValidPointer(x):
                    ret.append((va, x))
                    offset += size
                    continue

                offset += 1
        return ret

    def isProbablyString(self, va):
        offset, bytes = self.getByteDef(va)
        maxlen = len(bytes) - offset
        count = 0
        while count < maxlen:
            # If we hit another thing, then probably not...
            if self.getLocation(va+count) != None:
                return False
            c = bytes[offset+count]
            # The "strings" algo basically says 4 or more...
            if ord(c) == 0 and count >= 4:
                return True
            if c not in string.printable:
                return False
            count += 1
        return False

    def isProbablyUnicode(self, va):
        """
        This will return true if the memory location is likely
        *simple* UTF16-LE unicode (<ascii><0><ascii><0><0><0>).
        """
        #FIXME this totally sucks...

        offset, bytes = self.getByteDef(va)
        maxlen = len(bytes) + offset
        count = 0
        while count < maxlen:
            if self.getLocation(va+count) != None:
                return False

            c0 = bytes[offset+count]
            c1 = bytes[offset+count+1]

            # If it's not null,char,null,char then it's
            # not simple unicode...
            if ord(c1) != 0:
                return False

            # If we find our null terminator after more
            # than 4 chars, we're probably a real string
            if ord(c0) == 0:
                if count > 8:
                    return True
                return False

            # If the first byte char isn't printable, then
            # we're probably not a real "simple" ascii string
            if c0 not in string.printable:
                return False

            count += 2

    def isProbablyCode(self, va):
        """
        Most of the time, absolute pointes which point to code
        point to the function entry, so test it for the sig.
        """
        if not self.isExecutable(va):
            return False
        return self.isFunctionSignature(va)

    #################################################################
    #
    # Opcode API
    #
    def makeOpcode(self, va, op=None):
        """
        Create a single opcode location.  If you have already parsed the
        opcode object, you may pass it in.
        """
        if op == None:
            try:

                op = self.parseOpcode(va)

            except envi.InvalidInstruction, msg:
                bytes = self.readMemory(va, 16)
                print "Invalid Instruct Attempt At:",hex(va),bytes.encode("hex")
                raise InvalidLocation(va,msg)

            except Exception, msg:
                traceback.print_exc()
                raise InvalidLocation(va,msg)

        # Add our opcode location first (op flags become ldata)
        loc = self.addLocation(va, op.size, LOC_OP, op.iflags)

        # This takes care of all normal indirect immediates

        brdone = {}
        brlist = op.getBranches()
        for tova,bflags in brlist:

            # If there were unresolved dynamic branches, oh well...
            if tova == None: continue
            if not self.isValidPointer(tova): continue

            brdone[tova] = True

            # Special case, if it's a table branch, lets resolve it now.
            if bflags & envi.BR_TABLE:
                ptrbase = tova
                rdest = self.castPointer(ptrbase)

                i = 0
                tabdone = {}
                while self.isValidPointer(rdest):

                    if not tabdone.get(rdest):
                        tabdone[rdest] = True
                        self.addXref(va, rdest, REF_CODE, envi.BR_COND)
                        if self.getName(rdest) == None:
                            self.makeName(rdest, "case%d_%.8x" % (i,rdest))

                    ptrbase += self.psize
                    if len(self.getXrefsTo(ptrbase)):
                        break # Another xref means not our table anymore
                    i += 1
                    rdest = self.castPointer(ptrbase)

                # This must be second (len(xrefsto))
                self.addXref(va, tova, REF_PTR, None)

            elif bflags & envi.BR_DEREF:

                self.addXref(va, tova, REF_DATA)
                ptrdest = None
                if self.getLocation(tova) == None:
                    ptrdest = self.makePointer(tova, follow=False)

                # If the actual dest is executable, make a code ref fixup
                # which *removes* the deref flag...
                if ptrdest and self.probeMemory(ptrdest, 1, e_mem.MM_EXEC):
                    self.addXref(va, ptrdest, REF_CODE, bflags & ~envi.BR_DEREF)
                else:
                    self.addXref(va, tova, REF_CODE, bflags)

            else:
                # vivisect does NOT create REF_CODE entries for
                # instruction fall through
                if bflags & envi.BR_FALL: continue

                self.addXref(va, tova, REF_CODE, bflags)

        # Check the instruction for static d-refs
        for o in op.opers:
            # FIXME it would be nice if we could just do this one time
            # in the emulation pass (or hint emulation that some have already
            # been done.

            # Does the operand touch memory ?
            if o.isDeref():

                ref = o.getOperAddr(op, None)

                if brdone.get(ref, False):
                    continue

                if ref != None and self.isValidPointer(ref):

                    # It's a data reference. lets also check if the data is
                    # a pointer.

                    self.addXref(va, ref, REF_DATA)

                    # If we don't already know what type this location is,
                    # lets make it either a pointer or a number...
                    if self.getLocation(ref) == None:

                        offset, bytes = self.getByteDef(ref)

                        val = e_bits.parsebytes(bytes, offset, o.tsize)

                        if (self.psize == o.tsize and self.isValidPointer(val)):
                            self.makePointer(ref, tova=val)
                        else:
                            self.makeNumber(ref, o.tsize, val=val)

            else:
                ref = o.getOperValue(op)
                if brdone.get(ref, False):
                    continue
                if ref != None and self.isValidPointer(ref):
                    self.addXref(va, ref, REF_PTR)

        return loc

    def makeCode(self, va):
        """
        Attempt to begin code-flow based disassembly by
        starting at the given va.  The va will be made into
        an OpcodeLoc and refs will be walked continuing to 
        make code where possible.
        """
        # If this is already a location, bail.
        if self.isLocation(va):
            return

        calls_from = self.cfctx.addCodeFlow(va)

        for callva in calls_from:
            self.cfctx.addEntryPoint(callva)

    def parseOpcode(self, va):
        """
        Return an envi opcode parsed from the bytes at the specified VA.
        This does *not* require that the location be a defined location
        and may even be used to parse where there are already locations.
        """
        offset, bytes = self.getByteDef(va)
        return self.arch.makeOpcode(bytes, offset, va)

    #################################################################
    #
    # Function API
    #

    def isFunction(self, funcva):
        """
        Return True if funcva is a function entry point.
        """
        return self.funcmeta.get(funcva) != None

    def getFunctions(self):
        """
        Return a list of the function virtual addresses
        defined in the workspace.
        """
        return self.funcmeta.keys()

    def getFunction(self, va):
        """
        Return the VA for this function.  This will search code blocks
        and check for a function va.
        """
        if self.funcmeta.get(va) != None:
            return va
        cbtup = self.getCodeBlock(va)
        if cbtup != None:
            return cbtup[CB_FUNCVA]
        return None

    def makeFunction(self, va, meta=None):
        """
        Do parsing for function information and add a new function doodad.
        This function should probably only be called once code-flow for the
        area is complete.
        """

        if self.isFunction(va):
            return

        if meta == None:
            meta = {}

        if not self.isValidPointer(va):
            raise InvalidLocation(va)

        self.cfctx.addEntryPoint(va)

    def delFunction(self, funcva):
        """
        Remove a function, it's code blocks and all associated meta
        """
        if self.funcmeta.get(funcva) == None:
            raise InvalidLocation(funcva)

        self._fireEvent(VWE_DELFUNCTION, funcva)

    def setFunctionArgs(self, funcva, args):
        """
        Set the argument information for a given function. This
        information is a list of (atype, aname) tuples where atype
        is either an impemu EmuMagic type or a vstruct type...
        """
        self.setFunctionMeta(funcva, 'FunctionArguments', args)

    def setFunctionArg(self, funcva, index, atype, aname=None, doprec=True):
        """
        Set *one* funtion argument for for this function.
        (This will automatically update the length of the args
        if you go beyond what it was previously aware of.)

        doprec controls the use of the type precedence subsystem (on by default).
        If you try to set something that you know, and it's precedence is lower
        than the one that is already there, it will be silently ignored.
        """
        if aname == None:
            aname = atype.getDefName()

        alist = self.getFunctionArgs(funcva)

        deftype = viv_impmagic.Unknown
        defname = viv_impmagic.Unknown.__defname__

        while len(alist) <= index:
            alist.append((deftype,defname))

        etype,ename = alist[index]

        if doprec:
            if etype.__precedence__ >= atype.__precedence__:
                return

        alist[index] = (atype,aname)

        self.setFunctionArgs(funcva, alist)

    def getFunctionArgs(self, funcva):
        """
        Return the list of known args for this function.
        The list contains (atype,aname) tuples.
        """
        #ret = self.func_args.get(funcva)
        ret = self.getFunctionMeta(funcva, 'FunctionArguments')
        if ret == None:
            ret = []
        return ret

    def getFunctionArgNames(self, funcva):
        '''
        Get the index-adjusted names for the function arguments (as you see in the
        interface...)
        '''
        return [ '%s%d' % (aname,j) for j,(atype,aname) in enumerate(self.getFunctionArgs(funcva)) ]

    def getFunctionArg(self, funcva, idx):
        '''
        Get the (atype, aname) tuple describing the argument index for
        the function.  Returns (None,None) if not found.
        '''
        args = self.getFunctionArgs(funcva)
        if args == None:
            return None, None
        if len(args) > idx:
            return args[idx]
        return None, None

    def getFunctionLocals(self, funcva):
        return self.getFunctionMeta(funcva, 'FunctionLocals', [])

    def setFunctionLocals(self, funcva, flocals):
        '''
        Set the known list of function local variables.  The list consists
        of (offset, type, name) tuples where offset is the *negagive* offset
        of the local from the entry stack pointer.

        Example: vw.setFunctionLocals( [ 8, Unknown, 'myarg' ]
        '''
        return self.setFunctionMeta(funcva, 'FunctionLocals', flocals)

    def getFunctionLocal(self, funcva, offset):
        offset = abs(offset)
        locals = self.getFunctionLocals(funcva)
        for loffset, ltype, lname in locals:
            if offset == loffset:
                return (ltype,lname)
        return (None, None)

    def setFunctionLocal(self, funcva, offset, ltype, lname):
        offset = abs(offset)

        locals = self.getFunctionLocals(funcva)

        idx = None
        for i,(toff, ttype, tname) in enumerate(locals):
            if toff == offset:
                idx = i
                break

        if idx == None: # We have no match...
            locals.append( (offset, ltype, lname) )

        else:
            locals[idx] = (offset, ltype, lname)

        self.setFunctionLocals(funcva, locals)

    def getFunctionSymbol(self, funcva, offset):
        # FIXME should we unify this?
        if offset < 0:
            return self.getFunctionLocal(funcva, offset)
        return self.getFunctionArg(funcva, offset)

    def setFunctionMeta(self, funcva, key, value):
        """
        Set meta key,value pairs that describe a particular
        function (by funcva).

        Example: vw.setFunctionMeta(fva, "WootKey", 10)
        """
        if not self.isFunction(funcva):
            raise InvalidFunction(funcva)
        self._fireEvent(VWE_SETFUNCMETA, (funcva, key, value))

    def getFunctionMeta(self, funcva, key, default=None):
        m = self.funcmeta.get(funcva)
        if m == None:
            raise InvalidFunction(funcva)
        return m.get(key, default)

    def getFunctionMetaDict(self, funcva):
        """
        Return the entire dictionary of function metadata
        for the function specified at funcva
        """
        return self.funcmeta.get(funcva)

    def getFunctionBlocks(self, funcva):
        """
        Return the code-block objects for the given function va
        """
        ret = self.codeblocks_by_funcva.get(funcva)
        if ret == None:
            ret = []
        return ret

    def makeFunctionThunk(self, funcva, thname):
        """
        Inform the workspace that a given function is considered a "thunk" to another.
        This allows the workspace to process argument inheritance and several other things.

        Usage: vw.makeThunk(0xvavavava, "kernel32.CreateProcessA")

        """
        self.setFunctionMeta(funcva, "Thunk", thname)
        n = self.getName(funcva)
        if n.find("sub_") == 0:
            base = thname.split(".")[-1]
            self.makeName(funcva, "%s_%.8x" % (base,funcva))

        # Steal the calling convention and args from real target
        # function if we manage to resolve it
        efunc = self.getImpEmuFunc(thname)
        if efunc != None:
            self.setFunctionMeta(funcva, "CallingConvention", efunc.callconv)
            fargs = []
            for i in range(efunc.argc):
                fargs.append((efunc.argt[i], efunc.argn[i]))
            self.setFunctionArgs(funcva, fargs)

    def getCallers(self, va):
        '''
        Get the va for all the callers of the given function/import.

        Example:
            for va in vw.getCallers( importva ):
                dostuff(va)
        '''
        ret = []
        for fromva, tova, rtype, rflags in self.getXrefsTo(va, rtype=REF_CODE):
            if rflags & envi.BR_PROC:
                ret.append(fromva)
        return ret

    def getImportCallers(self, name):
        """
        Get a list of all the callers who reference the specified import
        by name. (If we detect that the name is actually *in* our workspace,
        return those callers too...
        """
        ret = []

        # If it's a local function, do that too..
        fva = self.vaByName(name)
        if fva != None and self.isFunction(fva):
            ret = self.getCallers(fva)

        for fva in self.getFunctions():
            if self.getFunctionMeta(fva, 'Thunk') == name:
                ret.extend( self.getCallers( fva ) )

        for lva,lsize,ltype,tinfo in self.getLocations(LOC_IMPORT):
            if tinfo == name:
                ret.extend( self.getCallers( lva ) )

        return ret

    #################################################################
    #
    # Xref API
    #

    def getXrefs(self):
        """
        Return the entire list of XREF tuples for this workspace.
        """
        return self.xrefs

    def getXrefsFrom(self, va, rtype=None):
        """
        Return a list of tuples for the xrefs whose origin is the
        specified va.  Optionally, only return xrefs whose type
        field is rtype if specified.

        example:
        for fromva, tova, rtype, rflags in vw.getXrefsFrom(0x41414141):
            dostuff(tova)
        """
        ret = []
        xrefs = self.xrefs_by_from.get(va, None)
        if xrefs == None:
            return ret
        if rtype == None:
            return xrefs
        for xtup in xrefs:
            if xtup[XR_RTYPE] == rtype:
                ret.append(xtup)
        return ret

    def getXrefsTo(self, va, rtype=None):
        """
        Get a list of xrefs which point to the given va. Optionally,
        specify an rtype to get only xrefs of that type.
        """
        # FIXME make xrefs use MapLookup!
        ret = []
        xrefs = self.xrefs_by_to.get(va, None)
        if xrefs == None:
            return ret
        if rtype == None:
            return xrefs
        for xtup in xrefs:
            if xtup[XR_RTYPE] == rtype:
                ret.append(xtup)
        return ret

    def addMemoryMap(self, va, perms, fname, bytes):
        """
        Add a memory map to the workspace.  This is the *only* way to
        get memory backings into the workspace.
        """
        self._fireEvent(VWE_ADDMMAP, (va, perms, fname, bytes))

    def delMemoryMap(self, va):
        raise "OMG"

    def addSegment(self, va, size, name, filename):
        """
        Add a "segment" to the workspace.  A segment is generally some meaningful
        area inside of a memory map.  For PE binaries, a segment and a memory map
        are synonymous.  However, some platforms (Elf) specify their memory maps
        (program headers) and segments (sectons) seperately.
        """
        self._fireEvent(VWE_ADDSEGMENT, (va,size,name,filename))

    def getSegment(self, va):
        """
        Return the tuple representation of a segment. With the
        following format:

        (va, size, name, filename)
        """
        for seg in self.segments:
            sva, ssize, sname, sfile = seg
            if va >= sva and va < (sva + ssize):
                return seg
        return None

    def getSegments(self):
        """
        Return a list of segment tuples (see getSegment) for all
        the segments defined in the current worksace
        """
        return list(self.segments)

    def addCodeBlock(self, va, size, funcva):
        """
        Add a region of code which belongs to a function.  Code-block boundaries
        are at all logical branches and have more in common with a logical
        graph view than function chunks.
        """
        self._fireEvent(VWE_ADDCODEBLOCK, (va,size,funcva))

    def getCodeBlock(self, va):
        """
        Return the codeblock which contains the given va.  A "codeblock"
        is a location compatable tuple: (va, size, funcva)
        """
        return self.blockmap.getMapLookup(va)

    def delCodeBlock(self, va):
        """
        Remove a code-block definition from the codeblock namespace.
        """
        cb = self.getCodeBlock(va)
        if cb == None:
            raise Exception("Unknown Code Block: 0x%x" % va)
        self._fireEvent(VWE_DELCODEBLOCK, cb)

    def getCodeBlocks(self):
        """
        Return a list of all the codeblock objects.
        """
        return list(self.codeblocks)

    def addXref(self, fromva, tova, reftype, rflags=0):
        """
        Add an xref with the specified fromva, tova, and reftype
        (see REF_ macros).  This will *not* trigger any analysis.
        Callers are expected to do their own xref analysis (ie, makeCode() etc)
        """
        ref = (fromva,tova,reftype,rflags)
        if ref in self.getXrefsFrom(fromva):
            return
        self._fireEvent(VWE_ADDXREF, (fromva, tova, reftype, rflags))

    def delXref(self, ref):
        """
        Remove the given xref.  This *will* exception if the
        xref doesn't already exist...
        """
        if ref not in self.getXrefsFrom(ref[XR_FROM]):
            raise Exception("Unknown Xref: %x %x %d" % ref)
        self._fireEvent(VWE_DELXREF, ref)

    def analyzePointer(self, va):
        """
        Assume that a new pointer has been created.  Check if it's
        target has a defined location and if not, try to figgure out
        wtf is there...  Will return the location type of the location
        it recommends or None if a location is already there or it has
        no idea.
        """
        if self.getLocation(va) != None:
            return None
        if self.isProbablyString(va):
            return LOC_STRING
        elif self.isProbablyCode(va):
            return LOC_OP
        elif self.isProbablyUnicode(va):
            return LOC_UNI
        return None

    def getMeta(self, name, default=None):
        return self.metadata.get(name, default)

    def setMeta(self, name, value):
        """
        Set a meta key,value pair for this workspace.
        """
        self._fireEvent(VWE_SETMETA, (name,value))

    def initMeta(self, name, value):
        """
        Set a metakey ONLY if it is not already set. Either
        way return the value of the meta key.
        """
        m = self.getMeta(name)
        if m == None:
            self.setMeta(name, value)
            m = value
        return m

    def castPointer(self, va):
        """
        Return the value for a pointer in memory at
        the given location.  This method does NOT
        create a location object or do anything other
        than parse memory.
        """
        offset, bytes = self.getByteDef(va)
        return e_bits.parsebytes(bytes, offset, self.psize)

    def makePointer(self, va, tova=None, follow=True):
        """
        Create a new pointer location in the workspace.  If you have already
        parsed out the pointers value, you may specify tova to speed things
        up.
        """
        psize = self.psize

        # Get and document the xrefs created for the new location
        if tova == None:
            offset, bytes = self.getByteDef(va)
            tova = e_bits.parsebytes(bytes, offset, psize)

        self.addXref(va, tova, REF_PTR)

        ploc = self.addLocation(va, psize, LOC_POINTER)

        if follow and self.isValidPointer(tova):
            self.followPointer(tova)

        return ploc

    def makePad(self, va, size):
        """
        A special utility for making a pad of a particular size.
        """
        return self.addLocation(va, size, LOC_PAD, None)

    def makeNumber(self, va, size, val=None):
        """
        Create a number location in memory of the given size.

        (you may specify val if you have already parsed the value
         from memory and would like to save CPU cycles)
        """
        offset, bytes = self.getByteDef(va)
        if val == None:
            val = e_bits.parsebytes(bytes, offset, size)
        return self.addLocation(va, size, LOC_NUMBER, val)

    def makeString(self, va, size=None):
        """
        Create a new string location at the given VA.  You may optionally
        specify size.  If size==None, the string will be parsed as a NULL
        terminated ASCII string.
        """
        if size == None:
            size = self.asciiStringSize(va)

        if size <= 0:
            raise Exception("Invalid String Size: %d" % size)

        if self.getName(va) == None:
            m = self.readMemory(va, size-1).replace("\n","")
            self.makeName(va, "str_%s_%.8x" % (m[:16],va))
        return self.addLocation(va, size, LOC_STRING)

    def makeUnicode(self, va, size=None):
        if size == None:
            size = self.uniStringSize(va)

        if size <= 0:
            raise Exception("Invalid Unicode Size: %d" % size)

        if self.getName(va) == None:
            self.makeName(va, "wstr_%.8x" % va)
        return self.addLocation(va, size, LOC_UNI)

    def addConstModule(self, modname):
        '''
        Add constants declared within the named module
        to the constants resolver namespace.

        Example: vw.addConstModule('vstruct.constants.ntstatus')
        '''
        mod = self.loadModule(modname)
        self.vsconsts.addModule(mod)

    def addStructureModule(self, namespace, modname):
        '''
        Add a vstruct structure module to the workspace with the given
        namespace.

        Example: vw.addStructureModule('ntdll', 'vstruct.defs.windows.win_5_1_i386.ntdll')

        This allows subsequent struct lookups by names like
        '''

        mod = self.loadModule(modname)
        self.vsbuilder.addVStructNamespace(namespace, mod)

    def getStructure(self, va, vstructname):
        """
        Parse and return a vstruct object for the given name.  This
        (like parseOpcode) does *not* require that the location be a struct
        and will not create one (use makeStructure).
        """
        s = vstruct.getStructure(vstructname)
        if s == None:
            s = self.vsbuilder.buildVStruct(vstructname)
        bytes = self.readMemory(va, len(s))
        s.vsParse(bytes)
        return s

    def makeStructure(self, va, vstructname):
        """
        Make a location which is a structure and will be parsed/accessed
        by vstruct.  You must specify the vstruct name for the structure
        you wish to have at the location.  Returns a vstruct from the
        location.
        """
        s = self.getStructure(va, vstructname)
        self.addLocation(va, len(s), LOC_STRUCT, vstructname)

        # Determine if there are any pointers we need make
        # xrefs for...
        offset = 0
        for p in s.vsGetPrims():
            if isinstance(p, vs_prims.v_ptr):
                vptr = p.vsGetValue()
                if self.isValidPointer(vptr):
                    self.addXref(va+offset, vptr, REF_PTR)

            offset += len(p)

        return s

    def asciiStringSize(self, va):
        """
        Return the size (in bytes) of the ascii string
        at the specified location (or -1 if no terminator
        is found in the memory map)
        """
        offset,bytes = self.getByteDef(va)
        foff = bytes.find('\x00', offset)
        if foff == -1:
            return foff
        return (foff - offset) + 1

    def uniStringSize(self, va):
        """
        Return the size (in bytes) of the unicode string
        at the specified location (or -1 if no terminator
        is found in the memory map)
        """
        offset,bytes = self.getByteDef(va)
        foff = bytes.find('\x00\x00', offset)
        if foff == -1:
            return foff
        return (foff - offset) + 2

    def addLocation(self, va, size, ltype, tinfo=None):
        """
        Add a location tuple.
        """
        ltup = (va, size, ltype, tinfo)
        self._fireEvent(VWE_ADDLOCATION, ltup)
        return ltup

    def getLocations(self, ltype=None):
        """
        Return a list of location objects from the workspace
        of a particular type.
        """
        if ltype == None:
            return list(self.loclist)

        ret = []
        for loc in self.loclist:
            lva, lsize, xtype, linfo = loc
            if xtype == ltype:
                ret.append(loc)
        return ret

    def isLocation(self, va, range=False):
        """
        Return True if the va represents a location already.
        """
        if self.getLocation(va, range=range) != None:
            return True
        return False

    def isLocType(self, va, ltype):
        """
        You may use this to test if a given VA represents
        a location of the specified type.

        example:
        if vw.isLocType(0x41414141, LOC_STRING):
            print "string at: 0x41414141"
        """
        tup = self.getLocation(va)
        if tup == None:
            return False
        return tup[L_LTYPE] == ltype

    def getLocation(self, va, range=False):
        """
        Return the va,size,ltype,tinfo tuple for the given location.
        (specify range=True to potentially match a va that is inside
        a location rather than the beginning of one)
        """
        return self.locmap.getMapLookup(va)

    def getLocationRange(self, va, size):
        """
        A "location range" is a list of location tuples where
        undefined space *will* be represented by LOC_UNDEF tuples
        to provide a complete accounting of linear workspace.
        """
        ret = []
        endva = va+size
        undefva = None
        while va < endva:
            ltup = self.getLocation(va)
            if ltup == None:
                if undefva == None:
                    undefva = va
                va += 1
            else:
                if undefva != None:
                    ret.append((undefva, va-undefva, LOC_UNDEF, None))
                    undefva = None
                ret.append(ltup)
                va += ltup[L_SIZE]

        # Mop up any hanging udefs
        if undefva != None:
            ret.append((undefva, va-undefva, LOC_UNDEF, None))

        return ret

    def delLocation(self, va):
        """
        Delete the given Location object from the binary
        (removes any xrefs/etc for the location as well)

        This will raise InvalidLocation if the va is not
        an exact match for the beginning of a location.
        """
        loc = self.getLocation(va)
        if loc == None:
            raise InvalidLocation(va)
        self._fireEvent(VWE_DELLOCATION, loc)

    def getRenderInfo(self, va, size):
        """
        Get nearly everything needed to render a workspace area
        to a display.  This function *greatly* speeds up interface
        code and is considered "tightly coupled" with the asmview
        code.  (and is therefore subject to change).
        """
        locs = []
        funcs = {}
        names = {}
        comments = {}
        extras = {}

        for loc in self.getLocationRange(va, size):
            lva, lsize, ltype, tinfo = loc
            locs.append(loc)

            name = self.getName(lva)
            isfunc = self.isFunction(lva)
            cmnt = self.getComment(lva)

            if name != None:
                names[lva] = name
            if isfunc == True:
                funcs[lva] = True
            if cmnt != None:
                comments[lva] = cmnt

            if ltype == LOC_UNDEF:
                # Expand out all undefs so we can send all the info
                endva = lva + lsize
                while lva < endva:
                    uname = self.getName(lva)
                    ucmnt = self.getComment(lva)
                    if uname != None:
                        names[lva] = uname
                    if ucmnt != None:
                        comments[lva] = ucmnt
                    #ret.append(((lva, 1, LOC_UNDEF, None), self.getName(lva), False, self.getComment(lva)))
                    lva += 1

            elif ltype == LOC_OP:
                extras[lva] = self.parseOpcode(lva)

            elif ltype == LOC_STRUCT:
                extras[lva] = self.getStructure(lva, tinfo)
            
        return locs, funcs, names, comments, extras

    def getPrevLocation(self, va, adjacent=True):
        """
        Get the previous location behind this one.  If adjacent
        is true, only return a location which is IMMEDIATELY behind
        the given va, otherwise search backward for a location until
        you find one or hit the edge of the segment.
        """
        va -= 1
        ret = self.locmap.getMapLookup(va)
        if ret != None:
            return ret
        if adjacent:
            return None
        va -= 1
        while va > 0:
            ret = self.locmap.getMapLookup(va)
            if ret != None:
                return ret
            va -= 1
        return None

    def vaByName(self, name):
        return self.va_by_name.get(name, None)

    def getLocationByName(self, name):
        """
        Return a location object by the name of the
        location.
        """
        va = self.vaByName(name)
        if va == None:
            raise InvalidLocation(0, "Unknown Name: %s" % name)
        return self.getLocation(va)

    def getNames(self):
        """
        Return a list of tuples containing (va, name)
        """
        return self.name_by_va.items()

    def getName(self, va):
        '''
        Returns the name of the specified virtual address (or None).
        '''
        return self.name_by_va.get(va, None)

    def makeName(self, va, name, filelocal=False):
        """
        Set a readable name for the given location by va. There
        *must* be a Location defined for the VA before you may name
        it.  You may set a location's name to None to remove a name.
        """
        if filelocal:
            segtup = self.getSegment(va)
            if segtup == None:
                print "Failed to find file for 0x%.8x (%s) (and filelocal == True!)"  % (va, name)
            if segtup != None:
                fname = segtup[SEG_FNAME]
                if fname != None:
                    name = "%s.%s" % (fname, name)

        oldva = self.vaByName(name)
        # If that's already the name, ignore the event
        if oldva == va:
            return

        if oldva != None:
            raise DuplicateName(oldva, va, name)

        self._fireEvent(VWE_SETNAME, (va,name))

    def saveWorkspace(self, fullsave=True):

        if self.server != None:
            self.server.saveWorkspace()
            return

        modname = self.getMeta("StorageModule")
        filename = self.getMeta("StorageName")
        if modname == None:
            raise Exception("StorageModule not specified!")
        if filename == None:
            raise Exception("StorageName not specified!")

        # Usually this is "vivisect.storage.basicfile
        mod = self.loadModule(modname)

        # If they specified a full save, *or* this event list
        # has never been saved before, do a full save.
        if fullsave:
            mod.saveWorkspace(self, filename)
        else:
            mod.saveWorkspaceChanges(self, filename)

        self._createSaveMark()

    def loadFromFile(self, filename, fmtname=None):
        """
        Read the first bytes of the file and see if we can identify the type.
        If so, load up the parser for that file type, otherwise raise an exception.

        Returns the basename the file was given on load.
        """
        mod = None
        if fmtname == None:
            bytes = file(filename, "rb").read(32)
            fmtname = viv_parsers.guessFormat(bytes)

        mod = viv_parsers.getParserModule(fmtname)
        if hasattr(mod, "config"):
            self.mergeConfig(mod.config)

        fname = mod.parseFile(self, filename)

        self.initMeta("StorageName", filename+".viv")

        # Snapin our analysis modules
        self._snapInAnalysisModules()

        return fname

    def loadFromMemory(self, memobj, baseaddr, fmtname=None):
        """
        Load a memory map (or potentially a mapped binary file)
        from the memory object's map at baseaddr.
        """
        mod = None
        if fmtname == None:
            bytes = memobj.readMemory(baseaddr, 32)
            fmtname = viv_parsers.guessFormat(bytes)

        mod = viv_parsers.getParserModule(fmtname)
        if hasattr(mod, "config"):
            self.mergeConfig(mod.config)

        mod.parseMemory(self, memobj, baseaddr)

        mapva, mapsize, mapperm, mapfname = memobj.getMemoryMap(baseaddr)
        if not mapfname:
            mapfname = 'mem_map_%.8x' % mapva

        self.initMeta('StorageName', mapfname+".viv")
        # Snapin our analysis modules
        self._snapInAnalysisModules()

    def getFiles(self):
        """
        Return the current list of file objects in this
        workspace.
        """
        return self.filemeta.keys()

    def normFileName(self, filename):
        normname = os.path.basename(filename).lower()

        # Strip off an extension
        if normname.find('.') != -1:
            parts = normname.split('.')
            normname = '_'.join(parts[:-1])

        ok = string.letters + string.digits + '_'

        chars = list(normname)
        for i in xrange(len(chars)):
            if chars[i] not in ok:
                chars[i] = '_'

        normname = ''.join(chars)

        return normname

    def addFile(self, filename, imagebase, md5sum):
        """
        Create and add a new vivisect File object for the
        specified information.  This will return the file
        object which you may then use to do things like
        add imports/exports/segments etc...
        """
        nname = self.normFileName(filename)
        if self.filemeta.has_key(nname):
            raise Exception("Duplicate File Name: %s" % nname)
        self._fireEvent(VWE_ADDFILE, (nname, imagebase, md5sum))
        return nname

    def addEntryPoint(self, va):
        '''
        Add an entry point to the definition for the given file.  This
        will hint the analysis system to create functions when analysis
        is run.
        '''
        self.setVaSetRow('EntryPoints', (va,))

    def getEntryPoints(self):
        '''
        Get all the parsed entry points for all the files loaded into the
        workspace.

        Example:  for va in vw.getEntryPoints():
        '''
        return [ x for x, in self.getVaSetRows('EntryPoints') ]

    def setFileMeta(self, fname, key, value):
        """
        Store a piece of file specific metadata (python primatives are best for values)
        """
        if not self.filemeta.has_key(fname):
            raise Exception("Invalid File: %s" % fname)
        self._fireEvent(VWE_SETFILEMETA, (fname, key, value))

    def getFileMeta(self, filename, key, default=None):
        """
        Retrieve a piece of file specific metadata
        """
        d = self.filemeta.get(filename)
        if d == None:
            raise Exception("Invalid File: %s" % filename)
        return d.get(key, default)

    def getFileMetaDict(self, filename):
        '''
        Retrieve the file metadata for this file as a key:val dict.
        '''
        d = self.filemeta.get(filename)
        if d == None:
            raise Exception('Invalid File: %s' % filename)
        return d
        
    def getFileByVa(self, va):
        segtup = self.getSegment(va)
        if segtup == None:
            return None
        return segtup[SEG_FNAME]

    def getLocationDistribution(self):
        # NOTE: if this changes, don't forget the report module!
        totsize = float(0)
        for mapva, mapsize, mperm, mname in self.getMemoryMaps():
            totsize += mapsize
        loctot = 0
        ret = {}
        for i in xrange(LOC_MAX):
            cnt = 0
            size = 0
            for lva,lsize,ltype,tinfo in self.getLocations(i):
                cnt += 1
                size += lsize
            loctot += size

            tname = loc_type_names.get(i, 'Unknown')
            ret[i] = (tname, cnt, size, int((size/totsize)*100))

        # Update the undefined based on totals...
        undeftot = totsize-loctot
        ret[LOC_UNDEF] = ('Undefined', 0, undeftot, int((undeftot/totsize)*100))

        return ret

#################################################################
#
#  VA Set API
#

    def getVaSetNames(self):
        """
        Get a list of the names of the current VA lists.
        """
        return self.vasets.keys()

    def getVaSetDef(self, name):
        """
        Get the list of (name, type) pairs which make up the
        rows for this given VA set (the first one *always* the VA, but
        you can name it as you like...)
        """
        x = self.vasetdefs.get(name)
        if x == None: raise InvalidVaSet(name)
        return x

    def getVaSetRows(self, name):
        """
        Get a list of the rows in this VA set.
        """
        x = self.vasets.get(name)
        if x == None: InvalidVaSet(name)
        return x.values()

    def getVaSet(self, name):
        """
        Get the dictionary of va:<rowdata> entries.
        """
        x = self.vasets.get(name)
        if x == None: raise InvalidVaSet(name)
        return x

    def addVaSet(self, name, defs, rows=()):
        """
        Add a va set:

        name - The name for this VA set
        defs - List of (<name>,<type>) tuples for the rows (va is always first)
        rows - An initial set of rows for values in this set.
        """
        self._fireEvent(VWE_ADDVASET, (name, defs, rows))

    def delVaSet(self, name):
        """
        Delete a VA set by name.
        """
        if not self.vasets.has_key(name):
            raise Exception("Unknown VA Set: %s" % name)
        self._fireEvent(VWE_DELVASET, name)

    def setVaSetRow(self, name, rowtup):
        """
        Use this API to update the row data for a particular
        entry in the VA set. Create a new empty set if one
        does not already exist.
        """
        self._fireEvent(VWE_SETVASETROW, (name, rowtup))

    def delVaSetRow(self, name, va):
        """
        Use this API to delete the rowdata associated
        with the specified VA from the set.
        """
        if not self.vasets.has_key(name):
            raise Exception("Unknown VA Set: %s" % name)
        self._fireEvent(VWE_DELVASETROW, (name, va))

#################################################################
#
#  Shared Workspace APIs
#
    def chat(self, msg):
        uname = e_config.getusername()
        # FIXME this should be part of a UI event model.
        self._fireEvent(VWE_CHAT, (uname, msg))

#################################################################
#
#  Color Map API
#

    def getColorMaps(self):
        """
        Return a list of the names of the given color maps
        """
        return self.colormaps.keys()

    def addColorMap(self, mapname, colormap):
        """
        Add a colormap dictionary with the given name for the map.
        (A colormap dictionary is va:color entries)
        """
        self._fireEvent(VWE_ADDCOLOR, (mapname, colormap))

    def delColorMap(self, mapname):
        self._fireEvent(VWE_DELCOLOR, mapname)

    def getColorMap(self, mapname):
        """
        Return the colormap dictionary for the given map name.
        """
        return self.colormaps.get(mapname)

##########################################################
#
# The envi.resolver.SymbolResolver API...
#

    def getSymByName(self, name):

        # Check for a sym
        va = self.vaByName(name)
        if va != None:
            return e_resolv.Symbol(name, va, 0)

        # check for the need for a deref.
        d = self.filemeta.get(name)
        if d != None:
            return VivFileSymbol(self, name, d.get("imagebase"), 0, self.psize)

    def getSymByAddr(self, addr, exact=True):
        name = self.getName(addr)
        if name == None:
            if self.isValidPointer(addr):
                name = "loc_%.8x" % addr

        if name != None:
            #FIXME fname
            #FIXME functions/segments/etc...
            return e_resolv.Symbol(name, addr, 0)

    def setSymHint(self, va, idx, hint):
        '''
        Set a symbol hint which will be used in place of operand
        values during disassembly among other things...

        You may also set hint=None to delete sym hints.
        '''
        self._fireEvent(VWE_SYMHINT, (va,idx,hint))

    def getSymHint(self, va, idx):
        h = self.getFref(va, idx)
        if h != None:
            f = self.getFunction(va)

            lname = None
            if f != None:
                ltype,lname = self.getFunctionSymbol(f, h)

            if lname == None:
                # FIXME these belong in the resolvers?
                if h < 0:
                    lname = 'unkn_local'
                else:
                    lname = 'unkn_arg'

            return '%s_%d' % (lname, abs(h))

        return self.symhints.get((va,idx), None)

class VivFileSymbol(e_resolv.FileSymbol):
    # A namespace tracker thingie...
    def __init__(self, vw, fname, base, size, width=4):
        self.vw = vw
        e_resolv.FileSymbol.__init__(self, fname, base, size, width)

    def getSymByName(self, name):
        return self.vw.getSymByName("%s.%s" % (self.name, name))

def getVivPath(*pathents):
    dname = os.path.dirname(__file__)
    dname = os.path.abspath(dname)
    return os.path.join(dname, *pathents)


