"""
Attempt to find locations that are likely vftable arrays
by finding lists of function pointers in memory.

This should be a *late* pass after all code that is possible
is defined.
"""
import vivisect

def analyze(vw):

    psize = vw.arch.getPointerSize()

    for lva,lsize,ltype,tinfo in vw.getLocations(vivisect.LOC_POINTER):

        if not vw.isFunction(vw.getXrefsFrom(lva)[0][vivisect.XR_TO]):
            continue

        count = 1
        va = lva+lsize
        while True:

            if vw.getLocation(va) != None:
                break
                
            ptrva = vw.castPointer(va)
            #FIXME this might make us miss stuff
            if not vw.isFunction(ptrva):
                #print "SKIPPING:",hex(ptrva)
                break

            count += 1
            va += psize

        if count >= 4:
            print "VFTABLE? 0x%.8x" % ptrva
