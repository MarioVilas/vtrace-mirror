
import emulator as sym_emulator
import vivisect.tools.graphutil as viv_graph

def NOTgetSymbolikGraph(vw, fva, xlate):
    '''
    Instantiate a standard vivisect function graph (visgraph
    hierarchical graph) and translate all the opcodes in each block
    to un-applied symbolik effects.  The list of effects for each node
    is stored in 'symbolik_effects' list in the node properties.
    '''
    g = viv_graph.buildFunctionGraph(vw, fva)

    for nodeva,ninfo in g.getNodes():

        cbva = ninfo.get('cbva')
        cbsize = ninfo.get('cbsize')

        cbmax = cbva + cbsize
        oplist = []
        while cbva < cbmax:
            op = vw.parseOpcode(cbva)
            oplist.append(op)
            cbva += len(op)

        for op in oplist:
            xlate.translateOpcode(op)

        efflist = xlate.getEffects() # we needn't copy
        conlist = xlate.getConstraints()
        xlate.clearEffects()

        # Put them into a dictionary lookup by target address
        con_lookup = {}
        for coneff in conlist:
            addrva = coneff.addrsym.solve()
            clist = con_lookup.get(addrva)
            if clist == None:
                clist = []
                con_lookup[addrva] = clist
            clist.append(coneff)

        # Save these off in node info for later
        ninfo['opcodes'] = oplist
        ninfo['symbolik_effects'] = efflist

        # Add the constraints to the edges
        for eid,fromid,toid,einfo in g.getRefsFrom(nodeva):
            clist = con_lookup.pop(toid, None)
            if clist == None:
                continue
            einfo['symbolik_constraints'] = clist

        #if len(con_lookup):
            #raise Exception('FIXME: We ditched a constraint! %s' % repr(con_lookup))

    return g

def NOTgetSymbolikPaths(vw, graph):
    '''
    For each path through the function, run all symbolik
    effects in an emulator instance and yield
    graph, emulator, effectlist tuple.
    '''
    fva = graph.getMeta('fva')  # put in place by buildFunctionGraph...
    for path in viv_graph.getCodePaths(graph):

        emu = sym_emulator.SymbolikEmulator(vw)

        patheffects = []
        for node,edge in path:
            # This is the edge that *got us here* so it has to
            # be processed first!
            if edge != None:
                constraints = graph.getEdgeInfo(edge, 'symbolik_constraints', ())
                print 'EDGE GOT CONSTRAINTS',constraints
                constraints = emu.applyEffects(constraints)
                patheffects.extend(constraints)

            effects = graph.getNodeInfo(node, 'symbolik_effects', ())
            effects = emu.applyEffects(effects)
            patheffects.extend(effects)


        yield emu, patheffects

def getSymbolikLoops(vw, graph):
    '''
    For each loop path through the graph, 
    '''

