
"""
A function analysis module that will find code blocks in
functions by flow and xrefs.  This is basically a mandatory
module which should be snapped in *very* early by parsers.

"""

#FIXME this belongs in the core disassembler loop!

import envi
import vivisect

from vivisect.const import *

def analyzeFunction(vw, funcva):

    done = {}
    todo = [funcva,]

    brefs = []

    while len(todo):

        start = todo.pop()

        # If we've hit code we've already done, keep going.
        if done.get(start):
            continue

        done[start] = True

        brefs.append( (start, True) )

        va = start

        # Walk forward through instructions until a branch edge
        while True:

            loc = vw.getLocation(va)

            # If it's not a location, terminate
            if loc == None:
                if vw.verbose:
                    vw.vprint("CodeBlock Analysis: hit 0x%.8x (non location) from inside 0x%.8x" % (va,funcva))
                brefs.append( (va, False) )
                break

            lva,lsize,ltype,linfo = loc

            # If it's not an op, terminate
            if ltype != LOC_OP:
                if vw.verbose:
                    vw.vprint("CodeBlock Analysis: hit 0x%.8x %s (non-opcode location) from inside 0x%.8x" % (va, vw.reprLocation(loc),funcva))
                brefs.append( (va, False) )
                break

            nextva = va+lsize

            # For each of our code xrefs, create a new target.
            branch = False
            xrefs = vw.getXrefsFrom(va, REF_CODE)
            for fromva, tova, rtype, rflags in xrefs:

                # We don't handle procedural branches here...
                if rflags & envi.BR_PROC:
                    continue

                # For now, we'll skip jmp [import] thunks...
                if rflags & envi.BR_DEREF:
                    continue

                # Add the branch to todo (let him add to brefs after done check)
                branch = True
                todo.append( tova )

            # If it doesn't fall through, terminate (at nextva)
            if linfo & envi.IF_NOFALL:
                brefs.append( (nextva, False) )
                break

            # If we hit a branch, we are the end of a block...
            if branch:
                todo.append( nextva )
                break

            va = nextva

    # we now have an ordered list of block references!
    brefs.sort()
    brefs.reverse()

    while len(brefs):
        bva, isbegin = brefs.pop()
        if not isbegin:
            continue

        if len(brefs) == 0:
            vw.vprint('OMG: code block start with no end: 0x%.8x' % bva)
            break

        nextva, nextbegin = brefs[-1]
        bsize = nextva - bva
        vw.addCodeBlock(bva, bsize, funcva)

    vw.setFunctionMeta(funcva, "InstructionCount", len(done.keys()))

