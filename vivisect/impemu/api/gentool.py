import sys
import vivisect

'''
A very simple tool for generating import API definitions from a viv
workspace...
'''

import vivisect.impemu.api.windows.i386 as viv_api_win_i386

if __name__ == '__main__':

    vw = vivisect.VivWorkspace()
    vw.loadWorkspace(sys.argv[1])

    print 'from vstruct.primitives import *'
    print 'api_defs = {'

    fnames = {}

    for fva, etype, ename, fname in vw.getExports():

        enamekey = ename
        fnamekey = fname

        fnames[fname] = True

        # Skip past forwarders
        if not vw.isFunction(fva):
            continue

        if vw.getMeta('Platform') == 'Windows':
            enamekey = ename.lower()
            fnamekey = fname.lower()

        #argv = vw.getFunctionArgNames(fva)
        argv = [ (None, name) for t,name in vw.getFunctionArgs(fva) ]
        ccname = vw.getFunctionMeta(fva, 'CallingConvention')
        
        print "    '%s.%s':( '%s.%s', %s, %s )," % (fnamekey,enamekey,fname,ename,repr(ccname),repr(tuple(argv)))

    for fwdfname in fnames.keys():
        for rva, name, fwdname in vw.getFileMeta(fwdfname, 'forwarders', ()):
            # FIXME i386 specific....
            fwdapi = viv_api_win_i386.getImportApi(fwdname)
            if fwdapi == None:
                print '    # FIXME unresolved %s -> %s' % (name,fwdname)
            else:
                print "    '%s.%s':%s," % (fwdfname.lower(), name.lower(), repr(fwdapi))

    print '}'
    


