
import os
import re
import code
import time
import socket
import struct
import platform
import tempfile

import PE
import vdb
import envi
import envi.bits as e_bits
import envi.resolver as e_resolv
import vtrace

import envi.registers as e_registers
import vtrace.platforms.base as v_base

'''
VMWare config options...
debugStub.listen.guest64 = "TRUE" # ends up on port 8864 (or next avail)
debugStub.listen.guest32 = "TRUE" # ....            8832

debugStub.listen.guest32.remote = "TRUE"

debugStub.hideBreakpoints = "TRUE" # Enable breakpoints

From GDB stuff...  
===== i386 
src/gdb/i386-tdep.c
src/gdb/regformats/reg-i386.dat
===== amd64
src/gdb/amd64-tdep.c
src/gdb/regformats/reg-x86-64.dat
===== arm
name:arm
expedite:r11,sp,pc
32:r0
32:r1
32:r2
32:r3
32:r4
32:r5
32:r6
32:r7
32:r8
32:r9
32:r10
32:r11
32:r12
32:sp
32:lr
32:pc
96:f0
96:f1
96:f2
96:f3
96:f4
96:f5
96:f6
96:f7
32:fps
32:cpsr
'''

gdb_reg_defs = {
    'i386': (
        ['eax','ecx','edx','ebx','esp','ebp','esi','edi','eip','eflags','cs','ss','ds','es','fs','gs'
        ],
        '<16I'
    ),

    'amd64': (
        ['rax','rbx','rcx','rdx','rsi','rdi','rbp','rsp',
         'r8','r9','r10','r11','r12','r13','r14','r15','rip',
         'eflags','cs','ss','ds','es','fs','gs',
         #'st0','st1','st2','st3','st4','st5','st6','st7',
         #'fctrl','fstat','ftag','fiseg','fioff','foseg','fooff','fop'
        ],

        #'<17Q7L' + ('10s' * 8) + '8L'
        '<17Q7L'
    ),

    # FIXME we will need arm flavors...
    'arm': (
        ["r0","r1","r2","r3","r4","r5","r6","r7","r8","r9","sl","fp","ip","sp",
         "lr","pc", None, "cpsr"],
        '<16I96sI'
    ),
}

exit_types = ('X', 'W')

def pkt(cmd):
    return '$%s#%.2x' % (cmd, csum(cmd))

def csum(bytes):
    sum = 0
    for b in bytes:
        sum += ord(b)
    return sum & 0xff

SIGINT  = 2
SIGTRAP = 5

trap_sigs = (SIGINT, SIGTRAP)

class GdbServerDisconnected(Exception):
    pass

class KeBugCheckBreak(vtrace.Breakpoint):
    def __init__(self, symname):
        vtrace.Breakpoint.__init__(self, None, expression=symname)
        self.fastbreak = True

    def notify(self, event, trace):
        sp = trace.getStackCounter()
        savedpc, exccode = trace.readMemoryFormat(sp, '<PP')
        trace._fireSignal(exccode)

class GdbStubMixin(e_registers.RegisterContext):

    def __init__(self):

        self.sock = None
        self.stepping = False
        self.attaching = False
        self.breaking = False

        self.bigmask = e_bits.u_maxes[ self.getPointerSize() ]

        aname = self.getMeta('Architecture')
        self._addArchNamespace(aname)

        self.setMeta('Platform', 'gdbstub')

        self.setMeta('GdbServerHost', 'localhost')
        self.setMeta('GdbServerPort', 0)
        self.setMeta('GdbPlatform', 'Unknown')
        self.setMeta('GdbTargetPlatform', 'Unknown')

        self.setMeta('BinaryFormat', None)

        arch_reg_info = gdb_reg_defs.get(aname)
        if arch_reg_info == None:
            raise Exception('We dont know the GDB register definition for arch: %s' % name)

        self._arch_regnames, self._arch_regfmt = arch_reg_info
        self._arch_regsize = struct.calcsize(self._arch_regfmt)

        self._arch_rctx = self.arch.archGetRegCtx()
        self._arch_reg_xlat = []
        for i,name in enumerate(self._arch_regnames):
            if name == None: # So we can skip parts of the gdb definition...
                continue
            j = self._arch_rctx.getRegisterIndex(name)
            if j != None:
                self._arch_reg_xlat.append((i,j))

        # Load up our register definition!
        e_registers.RegisterContext.__init__(self)
        rinfo = self._arch_rctx.getRegisterInfo(meta=True)
        self.setRegisterInfo(rinfo)

    def _addArchNamespace(self, aname):
        if aname == 'arm':
            import vstruct.defs.arm7 as vs_arm7
            self.vsbuilder.addVStructNamespace('arm7', vs_arm7)

    def normFileName(self, fname):
        # We don't know if it's / or \ ...   do both!
        basename = fname.split('/')[-1].split('\\')[-1]
        return basename.split(".")[0].split("-")[0].lower()

    def platformParseBinary(self, filename, baseaddr, normname):
        print 'platformParseBinary: 0x%.8x %s' % (baseaddr, normname)

    def platformParseBinaryPe(self, filename, baseaddr, normname):

        # If we're on windows, fake out the PE header and use dbghelp
        #if platform.system() in ['Microsoft', 'Windows']:
        if False:
            # FIXME this code is stolen and should be a function!
            import vtrace.platforms.win32 as vt_win32
            fakepe = self.readMemory(baseaddr, 1024)
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfilename = tfile.name
            import ctypes
            pebuf = ctypes.create_string_buffer(fakepe)
            try:
                try:
                    tfile.write(fakepe)
                    tfile.close()
                    #parser = vt_win32.Win32SymbolParser(-1, tfilename, baseaddr)
                    parser = vt_win32.Win32SymbolParser(-1, None, ctypes.addressof(pebuf))
                    parser.parse()
                    parser.loadSymsIntoTrace(self, normname)
                finally:
                    os.unlink(tfilename)
            except Exception, e:
                print e

        else:
            pe = PE.peFromMemoryObject(self, baseaddr)
            for rva, ord, name in pe.getExports():
                self.addSymbol(e_resolv.Symbol(name, baseaddr+rva, 0, normname))

    def _connectSocket(self):
        if self.sock != None:
            self.sock.shutdown(2)

        tries = 0
        while tries < 10:
            self.sock = socket.socket()
            try:
                self.sock.connect((self.getMeta('GdbServerHost'), self.getMeta('GdbServerPort')))
                # Some gdb stubs seem to send/expect an initial '+'
                try:
                    self.sock.settimeout(1)
                    self.sock.recv(1)
                    self.sock.sendall('+')
                except socket.timeout, t:
                    pass
                self.sock.settimeout(None)
                break
            except Exception, e:
                time.sleep(0.2)
                tries += 1

    def platformPs(self):
        return [ (1, 'SystemProcess'), ]

    def platformAttach(self, pid):
        self._connectSocket()
        self.attaching = True
        # Wait for the debug stub to stop the target
        while True:
            pkt = self._cmdTransact('?')
            if len(pkt) == 0:
                raise Exception('Attach Response Error!')
            if int(pkt[1:3], 16) == 0:
                import time
                time.sleep(0.1)
                self.platformSendBreak()
                pkt = self._cmdTransact('?')
            break
        self._sendPkt('?')

    def platformContinue(self):
        sig = self.getCurrentSignal()
        cmd = 'c'
        if sig != None:
            cmd = 'C%.2x' % sig
        self._sendPkt(cmd)
        #self._cmdTransact(cmd)

    def platformStepi(self):
        # FIXME by selected thread? and address?
        #self._cmdTransact('s')
        self._sendPkt('s')
        self.stepping = True

    def platformDetach(self):
        if not self.running:
            self.platformContinue()
        self.sock.shutdown(2)
        self.sock = None

    def platformSendBreak(self):
        '''
        For now, the only way I know how to re-break the target
        is to disconnect and re-connect...  TOTALLY GHETTO HACK!
        '''
        # If this isn't a break during attach, tell everybody we are
        # breaking...
        if not self.attaching:
            self.breaking = True
        self.sock.sendall('\x03')

    def platformWait(self):
        while True:
            pkt = self._recvPkt()
            if pkt.startswith('O'):
                print 'GDBSTUB SAID: %s' % pkt[1:].decode('hex')
                continue
            break
        return pkt

    def _getVmwareReg(self, rname):
        '''
        Use VMWare's monitor extension to get a register we wouldn't
        normally have...
        '''
        #fs 0x30 base 0xffdff000 limit 0x00001fff type 0x3 s 1 dpl 0 p 1 db 1
        fsstr = self._monitorCommand('r %s' % rname)
        fsparts = fsstr.split()
        return int(fsparts[3], 16)

    def _getVmwareIdtr(self):
        istr = self._monitorCommand('r idtr')
        m = re.match('.* base=(0x\w+) .*', istr)
        idtr = long(m.groups()[0], 0)
        return idtr

    def _getNtOsKrnl(self, idtr):
        x1, kptr, x2 = self.readMemoryFormat(idtr, '<IQI')
        try:
            kptr -= kptr & 0xfff
            while not self.readMemory(kptr, 16).startswith('MZ\x90\x00'):
                kptr -= 4096
            return kptr
        except Exception, e:
            return None

    def _enumGdbTarget(self):
        psize = self.getPointerSize()
        vercmd = self._monitorCommand('version')

        if self._monitorCommand('help').find('linuxoffsets') != -1:

            self.setMeta('GdbPlatform', 'VMware%d' % (psize * 8))

            if psize == 4: # Use the fs register to get KPCR
                fsbase = self._getVmwareReg('fs')
                self.setVariable('fsbase', fsbase)

                fs_fields = self.readMemoryFormat(fsbase, '<8I')

                # Windows has a self reference in the KPCR...
                if fs_fields[7] == fsbase:

                    # Use KPCR from XP for now...
                    import vstruct.defs.windows.win_5_1_i386.ntoskrnl as vs_w_ntoskrnl
                    self.vsbuilder.addVStructNamespace('nt', vs_w_ntoskrnl)

                    self.setMeta('GdbTargetPlatform', 'Windows')
                    self.casesens = False

                    kpcr = self.getStruct('nt.KPCR', fsbase)
                    kver = self.getStruct('nt.DBGKD_GET_VERSION64', kpcr.KdVersionBlock)

                    #print kpcr.tree()
                    #print kver.tree()

                    kernbase = kver.KernBase & self.bigmask
                    modlist = kver.PsLoadedModuleList & self.bigmask

                    self.setVariable('PsLoadedModuleList', modlist)
                    self.setVariable('KernelBase', kernbase)

                    self.platformParseBinary = self.platformParseBinaryPe

                    self.fireNotifiers(vtrace.NOTIFY_ATTACH)

                    self.addLibraryBase('nt', kernbase, always=True)
                    ldr_entry = self.readMemoryFormat(modlist, '<I')[0]
                    while ldr_entry != modlist:
                        ldte = self.getStruct('nt.LDR_DATA_TABLE_ENTRY', ldr_entry)
                        dllname = self.readMemory(ldte.FullDllName.Buffer, ldte.FullDllName.Length).decode('utf-16le')
                        dllbase = ldte.DllBase & self.bigmask
                        self.addLibraryBase(dllname, dllbase, always=True)
                        ldr_entry = ldte.InLoadOrderLinks.Flink & self.bigmask

                    try:
                        self.addBreakpoint(KeBugCheckBreak('nt.KeBugCheck'))
                    except Exception, e:
                        print 'Error Seting KeBugCheck Bp: %s' % e

                    try:
                        self.addBreakpoint(KeBugCheckBreak('nt.KeBugCheckEx'))
                    except Exception, e:
                        print 'Error Seting KeBugCheck Bp: %s' % e

                else:
                    # FIXME enumerate non-windows OSs!
                    self.fireNotifiers(vtrace.NOTIFY_ATTACH)

            else: # FIXME 64bit vmware!

                idtr = self._getVmwareIdtr()
                self.setVariable('idtr', idtr)

                win_kpcr = 0x07fffffde000

                fields = [-1,]
                try:
                    fields = self.readMemoryFormat(win_kpcr, '<7Q')
                except Exception, e:
                    print 'Exception:',e

                # FIXME other heuristics for linux/bsd/etc...
                if fields[-1] == win_kpcr:
                    self._initWin64(win_kpcr)
                else:
                    self.fireNotifiers(vtrace.NOTIFY_ATTACH)

                #fsbase = self._getVmwareReg('fs')
                #self.setVariable('fsbase', fsbase)

                #fs_fields = self.readMemoryFormat(fsbase, '<8I')

                #nt = self._getNtOsKrnl(idtr)
                #if nt != None:
                    # We are 64bit windows!
                    #import vstruct.defs.windows.win_6_1_amd64.ntoskrnl as vs_w_ntoskrnl
                    #self.vsbuilder.addVStructNamespace('nt', vs_w_ntoskrnl)
                    #self.setMeta('GdbTargetPlatform', 'Windows')
                    #self.setVariable('KernelBase', nt)
                    #self.platformParseBinary = self.platformParseBinaryPe
                    #self.fireNotifiers(vtrace.NOTIFY_ATTACH)
                    #self.addLibraryBase('nt', nt, always=True)

                #else:

        elif vercmd.lower().find('open on-chip debugger') != -1:

            self.setMeta('GdbPlatform', 'OpenOCD')
            self.fireNotifiers(vtrace.NOTIFY_ATTACH)

        else:
            print 'Unidentified gdbstub: %s' % vercmd
            self.fireNotifiers(vtrace.NOTIFY_ATTACH)


    # FIXME implement getRegister(idx) and steal get/set for regs which are not part of the whole...
    def _initWin64(self, kpcr):

        import vstrct.defs.windows.win_6_1_amd64.ntoskrnl as vs_w_ntoskrnl
        self.vsbuilder.addVStructNamespace('nt', vs_w_ntoskrnl)
        self._initWinBase()
                #nt = self._getNtOsKrnl(idtr)
                #if nt != None:
                    # We are 64bit windows!
                    #import vstruct.defs.windows.win_6_1_amd64.ntoskrnl as vs_w_ntoskrnl
                    #self.vsbuilder.addVStructNamespace('nt', vs_w_ntoskrnl)
                    #self.setMeta('GdbTargetPlatform', 'Windows')
                    #self.setVariable('KernelBase', nt)
                    #self.platformParseBinary = self.platformParseBinaryPe
                    #self.fireNotifiers(vtrace.NOTIFY_ATTACH)
                    #self.addLibraryBase('nt', nt, always=True)

    def _initWinBase(self, kpcr):
        self.setMeta('GdbTargetPlatform', 'Windows')
        self.casesens = False

        kpcr = self.getStruct('nt.KPCR', kpcr)
        kver = self.getStruct('nt.DBGKD_GET_VERSION64', kpcr.KdVersionBlock)

        kernbase = kver.KernBase & self.bigmask
        modlist = kver.PsLoadedModuleList & self.bigmask

        self.setVariable('PsLoadedModuleList', modlist)
        self.setVariable('KernelBase', kernbase)

        self.platformParseBinary = self.platformParseBinaryPe

        self.fireNotifiers(vtrace.NOTIFY_ATTACH)

        self.addLibraryBase('nt', kernbase, always=True)
        ldr_entry = self.readMemoryFormat(modlist, '<P')[0]
        while ldr_entry != modlist:
            ldte = self.getStruct('nt.LDR_DATA_TABLE_ENTRY', ldr_entry)
            dllname = self.readMemory(ldte.FullDllName.Buffer, ldte.FullDllName.Length).decode('utf-16le')
            dllbase = ldte.DllBase & self.bigmask
            self.addLibraryBase(dllname, dllbase, always=True)
            ldr_entry = ldte.InLoadOrderLinks.Flink & self.bigmask

        try:
            self.addBreakpoint(KeBugCheckBreak('nt.KeBugCheck'))
        except Exception, e:
            print 'Error Seting KeBugCheck Bp: %s' % e

        try:
            self.addBreakpoint(KeBugCheckBreak('nt.KeBugCheckEx'))
        except Exception, e:
            print 'Error Seting KeBugCheck Bp: %s' % e

    def platformProcessEvent(self, event):
        #print 'EVENT ->%s<-' % event

        if len(event) == 0:
            self.setMeta('ExitCode', 0xffffffff)
            self.fireNotifiers(vtrace.NOTIFY_EXIT)
            self.sock.shutdown(2)
            self.sock = None
            return

        atype = event[0]
        signo = int(event[1:3], 16)

        # Is this a thread specific signal?
        if atype == 'T':

            #print 'SIGNAL',sig

            dictbytes = event[3:]

            evdict = {}
            for kvstr in dictbytes.split(';'):
                if not kvstr: break
                #print 'KVSTR ->%s<-' % kvstr
                key, value = kvstr.split(':', 1)
                evdict[key.lower()] = value

            # Did we get a specific thread?
            tidstr = evdict.get('thread')
            if tidstr != None:
                tid = int(tidstr, 16)
                self.setMeta('ThreadId', tid)
            #else:
                #print "WE SHOULD ASK FOR THE CURRENT THREAD HERE!"

        elif atype == 'S':
            pass

        elif atype in exit_types:

            # Fire an exit event and GTFO!
            self._fireExit(signo)
            return

        else:
            print 'Unhandled Gdb Server Event: %s' % event

        #if self.attaching and signo in trap_sigs:
        if self.attaching:
            #if signo == 0:
                #We are attached, but he is still running! (no signal)
                #lets send a break, and process the event!
                #self.platformSendBreak()
                #evt = self.platformWait()
                #self.platformProcessEvent(evt)
                #return

            self.attaching = False
            self._enumGdbTarget()
            self.runAgain(False) # Clear this, if they want BREAK to run, it will
            self.fireNotifiers(vtrace.NOTIFY_BREAK)

        elif self.breaking and signo in trap_sigs:
            self.breaking = False
            self.fireNotifiers(vtrace.NOTIFY_BREAK)

        # Process the signal and decide what to do...
        elif signo == SIGTRAP:

            # Traps on posix systems are a little complicated
            if self.stepping:
                #FIXME try out was single step thing for intel
                self.stepping = False
                self.fireNotifiers(vtrace.NOTIFY_STEP)

            elif self.checkBreakpoints():
                return

            #elif self.checkWatchpoints():
                #return

            #elif self.checkBreakpoints():
                # It was either a known BP or a sendBreak()
                #return

            #elif self.execing:
                ##self.execing = False
                #self.handleAttach()

            else:
                self._fireSignal(signo)

        #elif signo == signal.SIGSTOP:
            #self.handleAttach()

        else:
            self._fireSignal(signo)

    def platformGetRegCtx(self, tid):
        '''
        Get an envi register context from the target stub.
        '''
        # FIXME tid!
        regbytes = self._cmdTransact('g').decode('hex')
        rvals = struct.unpack(self._arch_regfmt, regbytes[:self._arch_regsize])
        ctx = self.arch.archGetRegCtx()
        for myidx, enviidx in self._arch_reg_xlat:
            ctx.setRegister(enviidx, rvals[myidx])
        return ctx
        
    def platformSetRegCtx(self, tid, ctx):
        '''
        Set the target stub's register context from the envi register context
        '''
        # FIXME tid!
        regbytes = self._cmdTransact('g').decode('hex')
        regremain = regbytes[self._arch_regsize:]
        rvals = struct.unpack(self._arch_regfmt, regbytes[:self._arch_regsize])
        rvals = list(rvals) # So we can assign to them...
        for myidx, enviidx in self._arch_reg_xlat:
            rvals[myidx] = ctx.getRegister(enviidx)
        newbytes = struct.pack(self._arch_regfmt, rvals) + regremain
        return self._cmdTransact('G'+newbytes.encode('hex'))

    def _recvUntil(self, c):
        ret = ''
        while not ret.endswith(c):
            x = self.sock.recv(1)
            if len(x) == 0:
                raise Exception('socket closed prematurely!')
            ret += x
        return ret

    def _recvPkt(self):
        b = self.sock.recv(1)
        if len(b) == 0:
            raise GdbServerDisconnected()
        if b != '$':
            raise Exception('Invalid Pkt Beginning! ->%s<-' % b)

        bytes = self._recvUntil('#')
        bytes = bytes[:-1]

        isum = int(self.sock.recv(2), 16)
        ssum = csum(bytes)
        if isum != ssum:
            raise Exception('Invalid Checksum! his: 0x%.2x ours: 0x%.2x' % (isum, ssum))

        self.sock.sendall('+')

        #print 'RECV: ->%s<-' % bytes
        return bytes

    def _cmdTransact(self, cmd):
        self._sendPkt(cmd)
        return self._recvPkt()

    def _sendPkt(self, cmd):
        #print 'SEND: ->%s<-' % cmd
        self.sock.sendall(pkt(cmd))
        b = self.sock.recv(1)
        if b != '+':
            raise Exception('Retrans! ->%s<-' % b)

    def platformGetThreads(self):

        ret = {}

        self._sendPkt('qfThreadInfo')
        tbytes = self._recvPkt()

        while tbytes.startswith('m'):

            if tbytes.find(','):
                for bval in tbytes[1:].split(','):
                    ret[int(bval)] = 0
            else:
                ret[int(tbytes[1:])] = 0

            self._sendPkt('qsThreadInfo')
            tbytes = self._recvPkt()

        return ret

    def _raiseIfError(self, msg):
        if msg.startswith('E'):
            raise Exception('Error: %s' % msg)

    def platformReadMemory(self, addr, size):
        mbytes = ''
        offset = 0
        while len(mbytes) < size:
            # FIXME is this 256 problem just in the VMWare gdb stub?
            cmd = 'm%x,%x' % (addr + offset, min(256, size-offset))
            pkt = self._cmdTransact(cmd)
            self._raiseIfError(pkt)
            #print 'GOT SOME AT',pkt
            pbytes = pkt.decode('hex')
            offset += len(pbytes)
            mbytes += pbytes
        return mbytes

    def platformWriteMemory(self, addr, mbytes):
        cmd = 'M%x,%x:%s' % (addr, len(mbytes), mbytes.encode('hex'))
        pkt = self._cmdTransact(cmd)
        self._raiseIfError(pkt)

    def platformGetMaps(self):
        return []

    def _monitorCommand(self, cmd):
        resp = ''
        cmd = 'qRcmd,%s' % cmd.encode('hex')
        pkt = self._cmdTransact(cmd)
        while not pkt.startswith('OK'):
            self._raiseIfError(pkt)
            if not pkt.startswith('O'):
                return pkt.decode('hex')
            resp += pkt[1:].decode('hex')
            pkt = self._recvPkt()
        return resp

GDB_BP_SOFTWARE     = 0
GDB_BP_HARDWARE     = 1
GDB_BP_WATCH_WRITE  = 2
GDB_BP_WATCH_READ   = 3
GDB_BP_WATCH_ACCESS = 4

class GdbStubTrace(
        vtrace.Trace,
        GdbStubMixin,
        v_base.TracerBase):

    def __init__(self, archname):

        # First things first, lets steal ourself an arch!
        envi.stealArchMethods(self, archname)
        vtrace.Trace.__init__(self, archname=archname)
        v_base.TracerBase.__init__(self)
        GdbStubMixin.__init__(self)

    # FIXME this should have a cleaner abstraction to allow for stuff...
    # platformActivateBreak / Watch!
    # platformDeactivateBreak / Watch!

    # FIXME we also need cleaner abstraction for checkBreakpoints
    # (some platforms stop *on* break and some stop *after...)

    def _activateBreak(self, bp):
        # For now, we don't support watchpoints...
        if not bp.active:
            addr = bp.resolveAddress(self)
            self._cmdTransact('Z%d,%x,%x' % (GDB_BP_SOFTWARE,addr,1))

    def _cleanupBreakpoints(self, force=False):
        '''
        Cleanup any non-fastbreak breakpoints.  This routine doesn't even get
        called in the event of mode FastBreak=True.
        '''
        self.fb_bp_done = False
        for bp in self.breakpoints.itervalues():
            # No harm in calling deactivate on
            # an inactive bp
            if force or not bp.fastbreak:
                self._cmdTransact('z%d,%x,%x' % (GDB_BP_SOFTWARE,bp.getAddress(),1))
                bp.active = False
                #bp.deactivate(self)

    def checkBreakpoints(self):
        pc = self.getProgramCounter()
        bp = self.breakpoints.get(pc, None)

        if bp:
            self._fireBreakpoint(bp)
            return True

        if self.getMeta("ShouldBreak"):
            self.setMeta("ShouldBreak", False)
            self.fireNotifiers(vtrace.NOTIFY_BREAK)
            return True

        return False

    def _checkForBreak(self):
        """
        Check to see if we've landed on a breakpoint, and if so
        deactivate and step us past it.

        WARNING: Unfortunatly, cause this is used immidiatly before
        a call to run/wait, we must block briefly even for the GUI
        """
        # Steal a reference because the step should
        # clear curbp...
        bp = self.curbp
        if bp != None and bp.isEnabled():
            orig = self.getMode("FastStep")
            self.setMode("FastStep", True)
            self.stepi()
            self.setMode("FastStep", orig)
            self._activateBreak(bp)

    def buildNewTrace(self):
        arch = self.getMeta('Architecture')
        newt = GdbStubTrace(arch)
        newt.setMeta('GdbServerHost', self.getMeta('GdbServerHost'))
        newt.setMeta('GdbServerPort', self.getMeta('GdbServerPort'))
        return newt

