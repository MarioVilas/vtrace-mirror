
import cPickle as pickle
import vivisect

def saveWorkspaceChanges(vw, filename):
    elist = vw.exportWorkspaceChanges()
    if len(elist):
        f = file(filename, 'ab')
        pickle.dump(elist, f, protocol=2)
        f.close()

def saveWorkspace(vw, filename):
    f = file(filename, "wb")
    vwevents = vw.exportWorkspace()
    pickle.dump(vwevents, f, protocol=2)
    f.close()

def loadWorkspace(vw, filename):
    f = file(filename, "rb")

    #if vw.verbose: vw.vprint('Un-pickling Exported Workspace...')

    explist = []

    # Incremental changes are saved to the file by appending more pickled
    # lists of exported events

    e = None
    while True:
        try:
            import time
            begin = time.time()
            explist.append( pickle.load(f) )
        except EOFError, e:
            break
        except pickle.UnpicklingError, e:
            raise vivisect.InvalidWorkspace(filename, "invalid workspace file")

    f.close()

    for elist in explist:
        vw.importWorkspace(elist)

