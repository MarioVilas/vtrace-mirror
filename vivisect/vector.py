
"""
A module full of utils for vectored input tracking and code
flow analysis. (when a scalpel finds something you need to be
able to figgure out how to get to it right?)
"""

import vivisect.exc as viv_exc
import vivisect.impemu as viv_imp
import vivisect.impemu.impmagic as viv_magic
import vivisect.impemu.emufunc as viv_emufunc

import visgraph.pathcore as vg_path

from vivisect.const import *

import envi

class InputMonitor(viv_imp.EmulationMonitor):

    def __init__(self):
        viv_imp.EmulationMonitor.__init__(self)
        self.res = []

    def impcall(self, emu, impfunc):
        try:
            sp = emu.getStackCounter()
            args = impfunc.getArgs(emu)
            callpc = emu.readMemoryFormat(sp, '<P')[0]
            self.res.append((callpc, [ (val, emu.getMagic(val)) for val in args]))
        except Exception, e:
            import traceback
            traceback.print_exc()

def getEmuAtVa(vw, va):
    """
    Build and run an emulator to the given virtual address
    from the function entry point.

    (most useful for state analysis.  kinda heavy though...)
    """
    fva = vw.getFunction(va)
    if fva == None:
        raise viv_exc.InvalidLocation(va, "No Function found!")

    emu = vw.getEmulator()
    emu.runFunction(fva, stopva=va)
    return emu

def trackImportInputs(vw, iname):
    """
    Works just like trackFunctionInputs but finds calls to
    imports by name instead...
    """
    ef = vw.getImpEmuFunc(iname)
    if ef == None:
        raise Exception('no imp emu func for %s!' % iname)

    mon = InputMonitor()
    for va in vw.getImportCallers(iname):
        vw.vprint('IMPORT CALLERS %s 0x%.8x' % (iname, va))
        emu = getEmuAtVa(vw, va)
        # Set an emulation monitor and step over the call
        emu.setEmulationMonitor(mon)
        emu.stepi()

    return mon.res

def trackFunctionInputs(vw, fva):
    """
    Find all the callers to the given function and return a list
    of (callva, [ (argval, magic), ...]) tuples.
    """
    mon = InputMonitor()
    for va in vw.getCallers(fva):

        if not vw.getFunction(va):
            vw.vprint('code at 0x%.8x is not part of a function!' % va)
            continue

        emu = getEmuAtVa(vw, va)
        # Set an emulation monitor and step over the call
        emu.setEmulationMonitor(mon)
        emu.stepi()

    return mon.res

def trackArgOrigin(vw, fva, argidx):
    """
    Return an input tree (visgraph path tree) of the trackable inputs
    to the specified function.

    Each node in the list will be a leaf node for a path leading
    down toward a call to the target function.  Each node will have
    the following path node properties:

    fva    - The function
    argidx - The index of the argument input with this call
    cva    - The address of the call (to our next) (None on root node)
    argv   - A list of (<val>,<magic>) tuples for the call args (None on root node)
    """

    rootpath = vg_path.newPathNode(fva=fva, cva=None, trackidx=argidx, argidx=None, argv=None)

    todo = [rootpath, ]

    while len(todo):

        path = todo.pop()

        fva = vg_path.getNodeProp(path, 'fva')
        trackidx = vg_path.getNodeProp(path, 'trackidx')

        # Get all of our callers and their arguments to us
        for callva, argv in trackFunctionInputs(vw, fva):

            newfva = vw.getFunction(callva)
            pargs = dict(parent=path, fva=newfva, cva=callva, argidx=trackidx, argv=argv)
            newpath = vg_path.newPathNode(**pargs)

            aval, amagic = argv[trackidx]
            if isinstance(amagic, viv_magic.StackArg) and newfva:
                vg_path.setNodeProp(newpath, 'trackidx', amagic.index)
                todo.append(newpath)

    return vg_path.getLeafNodes(rootpath)

def getCodeFlow(vw, cbva):
    """
    Get a list of the code blocks which are known to flow
    into this one.  This *will* cross function boundaries.
    """
    ret = []
    # Get our actual xrefs
    for fromva, tova, xtype, xdata in vw.getXrefsTo(cbva, REF_CODE):
        xcb = vw.getCodeBlock(fromva)
        if xcb != None:
            ret.append(xcb)

    # Lets see if the instruction before this was a fallthrough
    ploc = vw.getPrevLocation(cbva)
    if ploc != None:
        pva, psize, ptype, pinfo = ploc
        # If it's an opcode with fallthrough, count this one too...
        if ptype == LOC_OP and not pinfo & envi.IF_NOFALL:
            pblock = vw.getCodeBlock(pva)
            if pblock != None:
                ret.append(pblock)

    return ret

def getCodePaths(vw, fromva, tova, trim=True):
    """
    Return a list of paths, where each path is a list
    of code blocks from fromva to tova.

    Usage: getCodePaths(vw, <fromva>, <tova>) -> [ [frblock, ..., toblock], ...]

    NOTE: "trim" causes an optimization which may not reveal *all* the paths,
          but is much faster to run.  It will never return no paths when there
          are some, but may not return all of them... (based on path overlap)
    """

    done = {}
    res = []

    frcb = vw.getCodeBlock(fromva)
    tocb = vw.getCodeBlock(tova)
    if frcb == None:
        raise viv_exc.InvalidLocation(fromva)
    if tocb == None:
        raise viv_exc.InvalidLocation(tova)

    frva = frcb[0] # For compare speed

    root = vg_path.newPathNode(cb=tocb, cbva=tocb[0])
    todo = [root, ]
    done[tova] = tocb

    cbcache = {}

    while len(todo):

        path = todo.pop()
        cbva = vg_path.getNodeProp(path, 'cbva')

        codeblocks = cbcache.get(cbva)
        if codeblocks == None:
            codeblocks = getCodeFlow(vw, cbva)
            cbcache[cbva] = codeblocks

        for cblock in codeblocks:

            bva,bsize,bfva = cblock

            # Don't follow loops...
            if vg_path.isPathLoop(path, 'cbva', bva):
                continue

            # If we have been here before and it's *not* the answer,
            # skip out...
            if trim and done.get(bva) != None: continue

            done[bva] = cblock

            newpath = vg_path.newPathNode(parent=path, cb=cblock, cbva=bva)

            # If this one is a match, we don't need to
            # track past it.  Also, put it in the results list
            # so we don't have to do it later....
            if bva == frva:
                res.append(newpath)
            else:
                todo.append(newpath)


    # Now...  if we have some results, lets build the block list.
    ret = []
    for cpath in res:
        fullpath = vg_path.getPathToNode(cpath)
        # We actually do it by inbound references, so reverse the result!
        fullpath.reverse()
        ret.append([vg_path.getNodeProp(path, 'cb') for path in fullpath])

    return ret

