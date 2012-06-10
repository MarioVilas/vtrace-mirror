
'''
Some glue code to do workspace related things based on visgraph
'''

import envi
import vivisect

import visgraph.pathcore as vg_pathcore
import visgraph.graphcore as vg_graphcore

xrskip = envi.BR_PROC | envi.BR_DEREF

def _nodeedge(tnode):
    nid = vg_pathcore.getNodeProp(tnode, 'nid')
    eid = vg_pathcore.getNodeProp(tnode, 'eid')
    return nid,eid

def getCodePaths(fgraph, loopcnt=0):
    '''
    Return a list of all the paths through the hierarchical graph.  Each
    "root" node is traced to all terminating points.  Specify a loopcnt
    to allow loop paths to be generated with the given "loop iteration count"

    Example:
        for path in g.getAllPaths():
            for node,edge in path:
                ...etc...
    '''
    for root in fgraph.getRootNodes():
        proot = vg_pathcore.newPathNode(nid=root, eid=None)
        todo = [(root,proot), ]

        while todo:

            nodeid,cpath = todo.pop()

            for eid, fromid, toid, einfo in fgraph.getRefsFrom(nodeid):
                # Skip loops if they are "deeper" than we are allowed
                if vg_pathcore.getPathLoopCount(cpath, 'nid', toid) > loopcnt:
                    continue
                npath = vg_pathcore.newPathNode(parent=cpath, nid=toid, eid=eid)
                todo.append((toid,npath))

        # Now we have a complete tree from root
        for path in vg_pathcore.getAllPaths(proot):
            yield [ _nodeedge(n) for n in path ]

def getLoopPaths(fgraph):
    '''
    Similar to getCodePaths(), however, getLoopPaths() will return path lists
    which loop.  The last element in the (node,edge) list will be the first
    "looped" block.
    '''
    loops = []
    for root in graph.getRootNodes():
        proot = vg_pathcore.newPathNode(nid=root, eid=None)
        todo = [ (root,proot), ]

        while todo:
            nodeid,cpath = todo.pop()

            for eid, fromid, toid, einfo in fgraph.getRefsFrom(nodeid):
                loopcnt = vg_pathcore.getPathLoopCount(cpath, 'nid', toid)
                if loopcnt > 1:
                    continue
                npath = vg_pathcore.newPathNode(parent=cpath, nid=toid, eid=eid)
                if loopcnt == 1:
                    loops.append(npath)
                else:
                    todo.append((toid,npath))

    for lnode in loops:
        yield [ _nodeedge(n) for n in vg_pathcore.getPathToNode(lnode) ]

def buildFunctionGraph(vw, fva, revloop=False):
    '''
    Build a visgraph HierarchicalGraph for the specified function.
    '''

    g = vg_graphcore.HierarchicalGraph()
    g.setMeta('fva', fva)

    colors = vw.getFunctionMeta(fva, 'BlockColors', default={})
    fcb = vw.getCodeBlock(fva)
    if fcb == None:
        t = (fva, vw.isFunction(fva))
        raise Exception('Invalid initial code block for 0x%.8x isfunc: %s' % t)

    todo = [ (fcb, []), ]

    fcbva, fcbsize, fcbfunc = fcb

    # Add the root node...
    bcolor = colors.get(fva, '#0f0')
    g.addNode(nodeid=fva, rootnode=True, cbva=fva, cbsize=fcbsize, color=bcolor)

    while todo:

        (cbva,cbsize,cbfunc),path = todo.pop()

        path.append(cbva)

        # If the code block va doesn't have a node yet, make one
        if not g.hasNode(cbva):
            bcolor = colors.get(cbva, '#0f0')
            g.addNode(nodeid=cbva, cbva=cbva, cbsize=cbsize, color=bcolor)

        # Grab the location for the last instruction in the block
        lva, lsize, ltype, linfo = vw.getLocation(cbva+cbsize-1)

        for xrfrom, xrto, xrtype, xrflags in vw.getXrefsFrom(lva, vivisect.REF_CODE):

            # For now, the graph doesn't cross function boundaries
            # or indirects.
            if xrflags & xrskip:
                continue

            if not g.hasNode(xrto):
                cblock = vw.getCodeBlock(xrto)
                if cblock == None:
                    print 'CB == None in graph building?!?!'
                    print '(fva: 0x%.8x cbva: 0x%.8x)' % (fva, xrto)
                    continue

                tova, tosize, tofunc = cblock
                if tova != xrto:
                    print 'CBVA != XREFTO in graph building!?'
                    print '(cbva: 0x%.8x xrto: 0x%.8x)' % (tova, xrto)
                    continue

                # Since we haven't seen this node, lets add it to todo
                # and build a new node for it.
                todo.append( ((tova,tosize,tofunc), list(path)) )
                bcolor = colors.get(tova, '#0f0')
                g.addNode(nodeid=tova, cbva=tova, cbsize=tosize, color=bcolor)

            # If they want it, reverse "loop" edges (graph layout...)
            if revloop and xrto in path:
                g.addEdge(xrto, cbva, reverse=True)
            else:
                g.addEdge(cbva, xrto)
                
        if linfo & envi.IF_NOFALL:
            continue

        # If this codeblock can fall through into another, add it to
        # todo!
        fallva = lva + lsize
        if not g.hasNode(fallva):
            fallblock = vw.getCodeBlock(fallva)
            if fallblock == None:
                print 'FB == None in graph building!??!'
                print '(fva: 0x%.8x  fallva: 0x%.8x' % (fva, fallva)
            elif fallva != fallblock[0]:
                print 'FALLVA != CBVA in graph building!??!'
                print '(fallva: 0x%.8x CBVA: 0x%.8x' % (fallva, fallblock[0])
            else:
                fbva, fbsize, fbfunc = fallblock
                if fbfunc != fva:
                    continue

                todo.append( ((fbva,fbsize,fbfunc), list(path)) )
                bcolor = colors.get(fallva, '#0f0')
                g.addNode(nodeid=fallva, cbva=fallva, cbsize=fbsize, color=bcolor)

        # If we ended up with a destination node, make the edge
        if g.hasNode(fallva):
            # If they want it, reverse "loop" edges (graph layout...)
            if revloop and fallva in path:
                g.addEdge(fallva, cbva, reverse=True)
            else:
                g.addEdge(cbva, fallva)

    return g

