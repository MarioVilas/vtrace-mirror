"""
Cobra RMI Framework

Cobra is a remote method invocation interface that is very "pythony".  It is
MUCH like its inspiration pyro, but slimmer and safer for things like threading
and object de-registration.  Essentially, cobra allows you to call methods from
and get/set attributes on objects that exist on a remote system.

"""
# Copyright (C) 2011 Invisigoth - See LICENSE file for details
import os
import sys
import time
import errno
import types
import socket
import struct
import urllib2
import traceback

import cPickle as pickle

from threading import currentThread,Thread,RLock
from SocketServer import ThreadingTCPServer, BaseRequestHandler

daemon = None
verbose = False
version = "Cobra2"
COBRA_PORT=5656
COBRASSL_PORT=5653
cobra_retrymax = None # Optional *global* retry max count

# Message Types
COBRA_HELLO     = 0
COBRA_CALL      = 1
COBRA_GETATTR   = 2
COBRA_SETATTR   = 3
COBRA_ERROR     = 4
COBRA_GOODBYE   = 5
COBRA_AUTH      = 6

SFLAG_MSGPACK   = 0x0001

class CobraException(Exception):
    """Base for Cobra exceptions"""
    pass

class CobraClosedException(CobraException):
    """Raised when a connection is unexpectedly closed."""
    pass

class CobraRetryException(CobraException):
    """Raised when the retrymax (if present) for a proxy object is exceeded."""
    pass

class CobraPickleException(CobraException):
    """Raised when pickling fails."""
    pass

class CobraAuthException(CobraException):
    '''Raised when specified auth data is rejected'''
    pass

class CobraErrorException(Exception):
    '''
    Raised when we receive a COBRA_ERROR message and the current options
    dont support serializing exception objects.
    '''

def connectSocket(host, port, timeout=None):
    """
    Make the long names go away....
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if timeout is not None:
        s.settimeout(timeout)

    s.connect((host, port))

    return s

def getCallerInfo():
    """
    This function may be used from *inside* a method being called
    by a remote caller.  It will return a tuple of host,port for the
    other side of the connection... use wisely ;)
    """
    return getattr(currentThread(),"_cobra_caller_info",None)

def getLocalInfo():
    """
    This function returns the local host,port combination being
    used in the socket servicing the current request
    """
    return getattr(currentThread(), "_cobra_local_info", None)

def getUserInfo():
    '''
    Get the cobra authenticated username of the current user
    ( or None if no user was authenticated )
    '''
    return getattr(currentThread(), "_cobra_authuser", None)

def setCallerInfo(callerinfo):
    """
    This is necissary because of crazy python method call
    name munging for thread attributes ;)
    """
    currentThread()._cobra_caller_info = callerinfo

def setUserInfo(authuser):
    currentThread()._cobra_authuser = authuser

def setLocalInfo(localinfo):
    currentThread()._cobra_local_info = localinfo

class CobraMethod:
    def __init__(self, proxy, methname):
        self.proxy = proxy
        self.methname = methname

    def __call__(self, *args, **kwargs):
        name = self.proxy._cobra_name
        if verbose: print "CALLING:",name,self.methname,repr(args)[:20],repr(kwargs)[:20]
        csock = self.proxy._cobra_getsock()
        mtype, name, data = csock.cobraTransaction(COBRA_CALL, name, (self.methname, args, kwargs))
        if mtype == COBRA_CALL:
            return data
        raise data

def pickledumps(o):
    return pickle.dumps( o, protocol=pickle.HIGHEST_PROTOCOL )

class CobraSocket:

    def __init__(self, socket, sflags=0):
        self.sflags = sflags
        self.socket = socket
        self.dumps = pickledumps
        self.loads = pickle.loads

        if sflags & SFLAG_MSGPACK:
            import msgpack
            self.dumps = msgpack.dumps
            self.loads = msgpack.loads

    def getSockName(self):
        return self.socket.getsockname()

    def getPeerName(self):
        return self.socket.getpeername()

    def sendMessage(self, mtype, objname, data):
        """
        Send message is responsable for transmission of cobra messages,
        and socket reconnection in the event that the send fails for network
        reasons.
        """

        #NOTE: for errors while using msgpack, we must send only the str
        if mtype == COBRA_ERROR and self.sflags & SFLAG_MSGPACK:
            data = str(data)

        try:
            buf = self.dumps(data)
        except Exception, e:
            raise CobraPickleException("The arguments/attributes must be serializable: %s" % e)

        self.sendExact(struct.pack("<III", mtype, len(objname), len(buf)) + objname + buf)

    def recvMessage(self):
        """
        Returns tuple of mtype, objname, and data
        This method is *NOT* responsable for re-connection, because there
        is not context on the server side for what to send on re-connect.
        Client side uses of the CobraSocket object should use cobraTransaction
        to ensure re-tranmission of the request on reception errors.
        """
        s = self.socket
        hdr = self.recvExact(12)
        mtype, nsize, dsize = struct.unpack("<III", hdr)
        name = self.recvExact(nsize)
        data = self.loads(self.recvExact(dsize))

        #NOTE: for errors while using msgpack, we must send only the str
        if mtype == COBRA_ERROR and self.sflags & SFLAG_MSGPACK:
            data = CobraErrorException(data)

        return (mtype, name, data)

    def recvExact(self, size):
        buf = ""
        s = self.socket
        while len(buf) != size:
            x = s.recv(size - len(buf))
            if len(x) == 0:
                raise CobraClosedException("Socket closed in recvExact...")
            buf += x
        return buf

    def sendExact(self, buf):
        self.socket.sendall(buf)

class SocketBuilder:
    '''
    For internal use by CobraClientSocket
    '''

    def __init__(self, scheme, host, port, timeout, kwargs):
        self.scheme = scheme
        self.host = host
        self.port = port
        self.timeout = timeout
        self.kwargs = kwargs

    def __call__(self):

        host = self.host
        port = self.port
        if verbose: print "CONNECTING TO:",self.host,self.port
        timeout = self.timeout

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.timeout is not None:
            sock.settimeout(self.timeout)

        if self.scheme == 'cobrassl':
            # A cobra SSL socket can take a few keywords in the
            # CobraProxy constructor...
            import ssl
            sslkwargs = {}
            sslca = self.kwargs.get('sslca')
            if sslca != None:
                sslkwargs['ca_certs'] = sslca
                sslkwargs['cert_reqs']=ssl.CERT_REQUIRED

            # Check for specified client certificate info
            sslkey = self.kwargs.get('sslkey')
            if sslkey:
                sslkwargs['keyfile'] = sslkey

            sslcrt = self.kwargs.get('sslcrt')
            if sslcrt:
                sslkwargs['certfile'] = sslcrt

            sock = ssl.wrap_socket(sock, **sslkwargs)

        sock.connect((self.host, self.port))
        if verbose:'CONNECTED!'
        return sock


class CobraClientSocket(CobraSocket):

    def __init__(self, sockctor, retrymax=cobra_retrymax, sflags=0):
        CobraSocket.__init__(self, sockctor(), sflags=sflags)
        self.sockctor = sockctor
        self.retries = 0
        self.trashed = False
        self.retrymax = retrymax

    def reConnect(self):
        """
        Handle the event where we need to reconnect
        """
        while self.retrymax is None or self.retries < self.retrymax:
            if verbose: sys.stderr.write("COBRA: Reconnection Attempt\n")
            try:
                self.socket = self.sockctor()
                return
            except Exception, e:
                time.sleep(2 ** self.retries)
                self.retries += 1
        self.trashed = True
        raise CobraRetryException()

    def cobraTransaction(self, mtype, objname, data):
        """
        This is an API for clients to use.  It will retransmit
        a sendMessage() automagically on recpt of an exception
        in recvMessage()
        """
        while True:
            try:
                self.sendMessage(mtype, objname, data)
                return self.recvMessage()
            except CobraClosedException, e:
                self.reConnect()
            except socket.error, e:
                self.reConnect()

class CobraDaemon(ThreadingTCPServer):

    def __init__(self, host="", port=COBRA_PORT, sslcrt=None, sslkey=None, sslca=None, msgpack=False):
        '''
        Construct a cobra daemon object.

        Parameters:
        host        - Optional hostname/ip to bind the service to (default: inaddr_any)
        port        - The port to bind (Default: COBRA_PORT)
        msgpack     - Use msgpack serialization

        # SSL Options
        sslcrt / sslkey     - Specify sslcrt and sslkey to enable SSL server side
        sslca               - Specify an SSL CA key to use validating client certs

        '''
        self.shared = {}
        self.host = host
        self.port = port
        self.reflock = RLock()
        self.refcnts = {}
        self.authmod = None
        self.sflags = 0

        if msgpack:
            self.sflags |= SFLAG_MSGPACK

        # SSL Options
        self.sslca = sslca
        self.sslcrt = sslcrt
        self.sslkey = sslkey

        if sslcrt and not os.path.isfile(sslcrt):
            raise Exception('CobraDaemon: sslcrt param must be a file!')

        if sslkey and not os.path.isfile(sslkey):
            raise Exception('CobraDaemon: sslkey param must be a file!')

        if sslca and not os.path.isfile(sslca):
            raise Exception('CobraDaemon: sslca param must be a file!')

        self.allow_reuse_address = True
        ThreadingTCPServer.__init__(self, (host, port), CobraRequestHandler)

        if port == 0:
            self.port = self.socket.getsockname()[1]

        self.daemon_threads = True
        self.recvtimeout = None

    def fireThread(self):
        thr = Thread(target=self.serve_forever)
        thr.setDaemon(True)
        thr.start()

    def setAuthModule(self, authmod):
        '''
        Enable an authentication module for this server
        ( all connections *must* be authenticated through the authmod )

        NOTE: See cobra.auth.* for various auth module implementations

        Example:
            import cobra.auth.shadow as c_a_shadow
            authmod = c_a_shadow.ShadowFileAuth('passwdfile.txt')
            cdaemon = CobraDaemon()
            cdaemon.setAuthModule()
        '''
        self.authmod = authmod

    def getSharedObject(self, name):
        return self.shared.get(name, None)

    def getSharedObjects(self):
        '''
        Return a list of (name, obj) for the currently shared objects.

        Example:
            for name,obj in daemon.getSharedObjects():
                print('%s: %r' % (name,obj))
        '''
        return self.shared.items()

    def getSharedName(self, obj):
        '''
        If this object is shared already, get the name...
        '''
        for name, sobj in self.shared.items():
            if sobj == obj:
                return name
        return None

    def getRandomName(self):
        ret = ""
        for byte in os.urandom(16):
            ret += "%.2x" % ord(byte)
        return ret

    def shareObject(self, obj, name=None, doref=False):
        """
        Share an object in this cobra server.  By specifying
        doref=True you will let CobraProxy objects decide that
        the object is done and should be un-shared.  Also, if
        name == None a random name is chosen.

        Returns: name (or the newly generated random one)
        """
        refcnt = None
        if doref:
            refcnt = 0
        if name == None:
            name = self.getRandomName()

        self.shared[name] = obj
        self.refcnts[name] = refcnt
        return name

    def getObjectRefCount(self, name):
        return self.refcnts.get(name)

    def decrefObject(self, name):
        """
        Decref this object and if it reaches 0, unshare it.
        """
        if verbose: print "DECREF:",name
        self.reflock.acquire()
        try:

            refcnt = self.refcnts.get(name, None)
            if refcnt != None:
                refcnt -= 1
                self.refcnts[name] = refcnt
                if refcnt == 0:
                    self.unshareObject(name)

        finally:
            self.reflock.release()

    def increfObject(self, name):
        if verbose: print "INCREF:",name
        self.reflock.acquire()
        try:
            refcnt = self.refcnts.get(name, None)
            if refcnt != None:
                refcnt += 1
                self.refcnts[name] = refcnt
        finally:
            self.reflock.release()

    def unshareObject(self, name):
        if verbose: print 'UNSHARE',name
        self.refcnts.pop(name, None)
        return self.shared.pop(name, None)

class CobraRequestHandler(BaseRequestHandler):

    def handle(self):
        c = CobraConnectionHandler(self.server, self.request)
        c.handleClient()

class CobraConnectionHandler:

    def __init__(self, daemon, socket):
        self.daemon = daemon
        self.socket = socket
        self.handlers = (
            self.handleHello,
            self.handleCall,
            self.handleGetAttr,
            self.handleSetAttr,
            self.handleError,
            self.handleGoodbye,
            self.handleError,
        )

    def handleClient(self):

        peer = self.socket.getpeername()
        me = self.socket.getsockname()
        if verbose: print "GOT A CONNECTIONN",peer

        sock = self.socket
        if self.daemon.sslkey:
            import ssl
            sslca = self.daemon.sslca
            keyfile = self.daemon.sslkey
            certfile = self.daemon.sslcrt
            sslreq = ssl.CERT_NONE
            # If they specify a CA key, require valid client certs
            if sslca:
                sslreq=ssl.CERT_REQUIRED

            sock = ssl.wrap_socket(sock,
                                     keyfile=keyfile, certfile=certfile,
                                     ca_certs=sslca, cert_reqs=sslreq,
                                     server_side=True)

        if self.daemon.recvtimeout:
            sock.settimeout( self.daemon.recvtimeout )

        authuser = None

        csock = CobraSocket(sock, sflags=self.daemon.sflags)

        setCallerInfo(peer)
        setLocalInfo(me)

        # If we have an authmod, they must send an auth message first
        if self.daemon.authmod:
            mtype,name,data = csock.recvMessage()
            if mtype != COBRA_AUTH:
                csock.sendMessage(COBRA_ERROR, '', CobraAuthException('Authentication Required!'))
                return

            authuser = self.daemon.authmod.authCobraUser( data )
            if not authuser:
                csock.sendMessage(COBRA_ERROR, '', CobraAuthException('Authentication Failed!'))
                return

            csock.sendMessage(COBRA_AUTH, '', authuser)
            setUserInfo( authuser )

        while True:

            try:
                mtype,name,data = csock.recvMessage()
            except CobraClosedException:
                break
            except socket.error:
                if verbose: traceback.print_exc()
                break

            if self.daemon.authmod and not self.daemon.authmod.checkUserAccess( authuser, name ):
                csock.sendMessage(COBRA_ERROR, name, Exception('Access Denied For User: %s' % authuser))
                continue

            obj = self.daemon.getSharedObject(name)
            if verbose: print "MSG FOR:",name,type(obj)

            if obj == None:
                try:
                    csock.sendMessage(COBRA_ERROR, name, Exception("Unknown object requested: %s" % name))
                except CobraClosedException:
                    pass
                if verbose: print "WARNING: Got request for unknown object",name
                continue

            try:
                handler = self.handlers[mtype]
            except:
                try:
                    csock.sendMessage(COBRA_ERROR, name, Exception("Invalid Message Type"))
                except CobraClosedException:
                    pass
                if verbose: print "WARNING: Got Invalid Message Type: %d for %s" % (mtype, data)
                continue

            try:
                handler(csock, name, obj, data)
            except Exception, e:
                if verbose: traceback.print_exc()
                try:
                    csock.sendMessage(COBRA_ERROR, name, e)
                except TypeError, typee:
                    # Probably about pickling...
                    csock.sendMessage(COBRA_ERROR, name, Exception(str(e)))
                except CobraClosedException:
                    pass

    def handleError(self, csock, oname, obj, data):
        print "THIS SHOULD NEVER HAPPEN"

    def handleHello(self, csock, oname, obj, data):
        """
        Hello messages are used to get the initial cache of
        method names for the newly connected object.
        """
        if verbose: print "GOT A HELLO"
        self.daemon.increfObject(oname)
        ret = {}
        for name in dir(obj):
            if type(getattr(obj,name)) in (types.MethodType, types.BuiltinMethodType):
                ret[name] = True
        try:
            csock.sendMessage(COBRA_HELLO, version, ret)
        except CobraClosedException:
            pass

    def handleCall(self, csock, oname, obj, data):
        if verbose: print "GOT A CALL",data
        methodname, args, kwargs = data
        meth = getattr(obj, methodname)
        try:
            csock.sendMessage(COBRA_CALL, "", meth(*args, **kwargs))
        except CobraClosedException:
            pass

    def handleGetAttr(self, csock, oname, obj, name):
        if verbose: print "GETTING ATTRIBUTE:",name
        try:
            csock.sendMessage(COBRA_GETATTR, "", getattr(obj, name))
        except CobraClosedException:
            pass

    def handleSetAttr(self, csock, oname, obj, data):
        if verbose: print "SETTING ATTRIBUTE:",data
        name,value = data
        setattr(obj, name, value)
        try:
            csock.sendMessage(COBRA_SETATTR, "", "")
        except CobraClosedException:
            pass

    def handleGoodbye(self, csock, oname, obj, data):
        if verbose: print 'GOODBYE!',oname,obj,data
        self.daemon.decrefObject(oname)
        try:
            csock.sendMessage(COBRA_GOODBYE, "", "")
        except CobraClosedException:
            pass

def isCobraUri(uri):
    try:
        x = urllib2.Request(uri)
        if x.get_type() not in ["cobra","cobrassl"]:
            return False
    except Exception, e:
        return False
    return True

def chopCobraUri(uri):

    req = urllib2.Request(uri)
    scheme = req.get_type()
    host = req.get_host()

    sel = req.get_selector()
    # URL options are parsed later
    selparts = sel.split('?', 1)
    name = selparts[0].strip("/")

    port = COBRA_PORT
    if host.find(':') != -1:
        host,portstr = host.split(":")
        port = int(portstr)

    # Do we have any URL options?
    urlparams = {}
    if len(selparts) > 1:

        for urlopt in selparts[1].split('&'):
            urlval = 1
            if urlopt.find('=') != -1:
                urlopt,urlval = urlopt.split('=',1)

            urlopt = urlopt.lower()
            urlparams[urlopt] = urlval

    return scheme,host,port,name,urlparams

class CobraProxy:
    """
    A proxy object for remote objects shared with Cobra

    A few optional keyword arguments are handled by all cobra protocols:
        retrymax    - Max transparent reconnect attempts
        timeout     - Socket timeout for a cobra socket
        authinfo    - A dict, probably like {'user':'username','passwd':'mypass'}
                      ( but it can be auth module specific )
        msgpack     - Use msgpack serialization

    Additional keyword arguments may depend on protocol.

    cobra://
        Only the standard args

    cobrassl://
        sslca           - File path to a CA certs file.  Causes server validation.
        sslcrt / sslkey - Client side cert info

    """
    def __init__(self, URI, retrymax=None, timeout=None, **kwargs):

        scheme, host, port, name, urlparams = chopCobraUri( URI )

        if verbose: print "HOST",host,"PORT",port,"OBJ",name

        self._cobra_uri = URI
        self._cobra_scheme = scheme
        self._cobra_host = host
        self._cobra_port = port
        self._cobra_slookup = (host,port)
        self._cobra_name = name
        self._cobra_retrymax = retrymax
        self._cobra_timeout = timeout
        self._cobra_kwargs = kwargs
        self._cobra_gothello = False
        self._cobra_sflags = 0

        if urlparams.get('msgpack'):
            self._cobra_sflags |= SFLAG_MSGPACK

        # If they asked for msgpack
        if kwargs.get('msgpack'):
            self._cobra_sflags |= SFLAG_MSGPACK

        if kwargs.get('sslkey') and not os.path.isfile(kwargs.get('sslkey')):
            raise Exception('CobraProxy: sslkey must be a file!')

        if kwargs.get('sslcrt') and not os.path.isfile(kwargs.get('sslcrt')):
            raise Exception('CobraProxy: sslcrt must be a file!')

        if kwargs.get('sslca') and not os.path.isfile(kwargs.get('sslca')):
            raise Exception('CobraProxy: sslca must be a file!')

        # If we got passed as user/passwd in our kwargs

        csock = self._cobra_getsock()
        mtype,rver,data = csock.cobraTransaction(COBRA_HELLO, name, "")

        if mtype == COBRA_ERROR:
            csock.trashed = True
            raise data

        if rver != version:
            csock.trashed = True
            raise Exception("Server Version Not Supported: %s" % rver)

        if mtype != COBRA_HELLO:
            csock.trashed = True
            raise Exception("Invalid Cobra Hello Response")

        self._cobra_gothello = True
        self._cobra_methods = data

    def _cobra_getsock(self):
        thr = currentThread()
        tsocks = getattr(thr, 'cobrasocks', None)
        if tsocks == None:
            tsocks = {}
            thr.cobrasocks = tsocks

        sock = tsocks.get(self._cobra_slookup)
        if not sock or sock.trashed:
            # Lets build a new socket... shall we?
            sock = self._cobra_newsock()

            # If we have authinfo lets authenticate
            authinfo = self._cobra_kwargs.get('authinfo')
            if authinfo != None:
                mtype,rver,data = sock.cobraTransaction(COBRA_AUTH, '', authinfo)
                if mtype != COBRA_AUTH:
                    raise CobraAuthException('Authentication Failed for %s: %s' % (repr(authinfo),str(data)))

            tsocks[self._cobra_slookup] = sock

        return sock

    def _cobra_newsock(self):
        """
        This is only used by *clients*
        """
        retrymax = self._cobra_retrymax
        builder = SocketBuilder(    self._cobra_scheme,
                                    self._cobra_host,
                                    self._cobra_port,
                                    self._cobra_timeout,
                                    self._cobra_kwargs)
        return CobraClientSocket(builder, retrymax=retrymax, sflags=self._cobra_sflags)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, sdict):
        self.__dict__.update(sdict)

    def __hash__(self):
        return hash(self._cobra_uri)

    def __nonzero__(self):
        return True

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<CobraProxy %s>" % self._cobra_uri

    def __eq__(self, obj):
        ouri = getattr(obj, '_cobra_uri', None)
        return self._cobra_uri == ouri

    def __ne__(self, obj):
        if self == obj:
            return False
        return True

    def __setattr__(self, name, value):
        if verbose: print "SETATTR %s %s" % (name, repr(value)[:20])

        if name.startswith('_cobra_'):
            self.__dict__[name] = value
            return

        csock = self._cobra_getsock()
        mtype,name,data = csock.cobraTransaction(COBRA_SETATTR, self._cobra_name, (name, value))
        if mtype == COBRA_ERROR:
            raise data
        elif mtype == COBRA_SETATTR:
            return
        else:
            raise Exception("Invalid Cobra Response")

    def __getattr__(self, name):
        if verbose: print "GETATTR",name

        if name == "__getinitargs__":
            raise AttributeError()

        # Handle methods
        if self._cobra_methods.get(name, False):
            return CobraMethod(self, name)

        csock = self._cobra_getsock()
        mtype,name,data = csock.cobraTransaction(COBRA_GETATTR, self._cobra_name, name)
        if mtype == COBRA_ERROR:
            raise data

        return data

    # For use with ref counted proxies
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        csock = self._cobra_getsock()
        csock.cobraTransaction(COBRA_GOODBYE, self._cobra_name, "")

def startCobraServer(host="", port=COBRA_PORT):
    global daemon
    if daemon == None:
        daemon = CobraDaemon(host,port)
        daemon.fireThread()
    return daemon

def runCobraServer(host='', port=COBRA_PORT):
    daemon = CobraDaemon(host,port)
    daemon.serve_forever()

def shareObject(obj, name=None, doref=False):
    """
    If shareObject is called before startCobraServer 
    or startCobraSslServer, it will call startCobraServer
    """
    global daemon
    if daemon == None:
        startCobraServer()
    return daemon.shareObject(obj, name, doref=doref)

def unshareObject(name):
    return daemon.unshareObject(name)

