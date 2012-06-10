
import os
import sys
import time
import cobra
import struct
import socket
import optparse
import threading
import subprocess

import vivisect

import cobra.dcode

viv_port = 0x4074

viv_s_ip = '224.56.56.56'
viv_s_port = 26998

class VivServer:

    def __init__(self, dirname=""):
        self.path = os.path.abspath(dirname)
        self.wdict = {}
        self.wsports = {}
        self.wsstatus = {}

    def setWorkspaceStatus(self, wsname, status):
        print 'Workspace Status: %s %s' % (wsname, status)
        self.wsstatus[wsname] = status

    def setWorkspacePort(self, wsname, port):
        self.wsports[wsname] = port

    def listWorkspaces(self):
        '''
        Get a list of the workspaces this server is willing to share.
        '''
        ret = []
        for fname in os.listdir(self.path):
            wsname = os.path.basename(fname)
            if not wsname.endswith('.viv'):
                continue
            wsstat = self.wsstatus.get(wsname, 'Shutdown')
            wsport = self.wsports.get(wsname)
            ret.append( (wsname, wsport, wsstat) )
        return ret

    def startWorkspace(self, wsname):
        print 'Client requesting: %s' % wsname
        wsport = self.wsports.get(wsname)
        if wsport != None:
            return wsport

        print 'Starting: %s' % wsname
        wspath = os.path.join(self.path, wsname)
        p = subprocess.Popen([sys.executable, "-m", "vivisect.server", "-w", wspath])

        port = self.wsports.get(wsname, None)
        while port == None:
            time.sleep(.5)
            if self.wsstatus.get(wsname, '').startswith('Error:'):
                raise Exception('Workspace %s' % self.wsstatus.get(wsname, ''))
            port = self.wsports.get(wsname, None)

        print 'Workspace Running: %s (port %d)' % (wsname, port)

        return port

def connectToServer(hostname):
    return cobra.CobraProxy("cobra://%s:%d/VivServer" %  (hostname,viv_port))

def connectToWorkspace(hostname, port):
    return cobra.CobraProxy("cobra://%s:%d/VivWorkspace" %  (hostname,port))

def runMainServer(dirname=''):
    print 'vivisect server starting... (port %d)' % viv_port
    s = VivServer(dirname=dirname)
    daemon = cobra.CobraDaemon(port=viv_port)
    daemon.shareObject(s, "VivServer")
    daemon.serve_forever()

def shareWorkspace(vw, doref=False):

    daemon = cobra.CobraDaemon('',0)
    daemon.fireThread()
    daemon.shareObject(vw, 'VivWorkspace', doref=doref)

    # Also, we are a dcode server...
    dfindr = cobra.dcode.DcodeFinder()
    daemon.shareObject(dfindr,'DcodeServer')
    
    return daemon

def waitForWorkspace(daemon):
    """
    Wait for the ref-count on the workspace to go away.
    """
    while daemon.getSharedObject('VivWorkspace') != None:
        time.sleep(1)

def runWorkspaceServer(workspace):

    svr = connectToServer('localhost')
    wsbase = os.path.basename(options.workspace)
    try:

        svr.setWorkspaceStatus(wsbase, 'Loading')
        vw = vivisect.VivWorkspace()
        vw.loadWorkspace(options.workspace)

        svr.setWorkspaceStatus(wsbase, 'Sharing')
        daemon = shareWorkspace(vw, doref=True)
        svr.setWorkspacePort(wsbase, daemon.port)
        svr.setWorkspaceStatus(wsbase, 'Running')

        waitForWorkspace(daemon)
        svr.setWorkspacePort(wsbase, None)
        svr.setWorkspaceStatus(wsbase, 'Shutdown')

    except Exception, e:
        svr.setWorkspacePort(wsbase, None)
        svr.setWorkspaceStatus(wsbase, 'Error: %s' % e)

    sys.exit(0)

def usage():
    print 'Usage: python -m vivisect.server <vivdir>'
    print ''
    print 'NOTE: vivdir is simply a directory full of viv files to share'
    sys.exit(0)

if __name__ == '__main__':
    
    parser = optparse.OptionParser(usage='python -m vivisect.server <vivdir>')
    parser.add_option('-w', '--workspace', dest='workspace', default=None, help='special case used by server')
    options, argv = parser.parse_args()

    # We are the server's child, firing a workspace.
    if options.workspace:
        runWorkspaceServer(options.workspace)

    if len(argv) != 1:
        usage()

    vivdir = os.path.abspath(sys.argv[1])
    if not os.path.isdir(vivdir):
        usage()

    runMainServer(vivdir)

