"""
A package for any of the vivisect workspace renderers.
"""
import envi

from vivisect.const import *

import vstruct.primitives as vs_prims
import envi.cli as e_cli
import envi.memcanvas as e_canvas

location_tags = {
    LOC_PAD:"pad",
    LOC_OP:"code",
    LOC_STRING:"string",
    LOC_UNI:"string",
}

def cmpoffset(x,y):
    return cmp(x[0], y[0])

class WorkspaceRenderer(e_canvas.MemoryRenderer):
    def __init__(self, vw):
        self.vw = vw

        # Some tweakables...
        self._show_segment = True
        self._show_address = True
        self._show_opbytes = True

    def render(self, mcanv, va):

        loc = self.vw.getLocation(va)
        if loc == None:
            loc = (va, 1, LOC_UNDEF, None)

        lva, lsize, ltype, tinfo = loc

        extra = None
        name = self.vw.getName(va)
        cmnt = self.vw.getComment(va)
        func = self.vw.isFunction(va)

        if ltype == LOC_OP:
            extra = self.vw.parseOpcode(lva)

        elif ltype == LOC_STRUCT:
            extra = self.vw.getStructure(lva, tinfo)

        self.renderLocation(mcanv, loc, name, func, cmnt, extra)
        return lsize

    def renderLocation(self, mcanv, loc, name, isfunc, cmnt, extra):
        """
        Actually render a given VA to the given text buffer.

        If there is *any* function to optimize, this is it... it renders EVERYTHING...
        """
        lva,lsize,ltype,tinfo = loc

        vatag = mcanv.getVaTag(lva)
        if cmnt != None:
            cmnttag = mcanv.getTag("comment")

        seg = self.vw.getSegment(lva)
        if seg == None:
            segname = "map"
        else:
            segname = seg[SEG_NAME]

        vastr = self.vw.arch.pointerString(lva)
        linepre = "%s:%s  " % (segname, vastr)

        xrefs = self.vw.getXrefsTo(lva)

        xrcount = len(xrefs)

        if seg != None and self._show_segment:
            segva, segsize, segname, segfname = seg
            if segva == lva:
                mcanv.addText(linepre, tag=vatag)
                mcanv.addText("Segment: %s (%d bytes) FIXME PERMS\n" % (segname, segsize))

        if isfunc:
            mcanv.addText(linepre, tag=vatag)
            mcanv.addText('\n')

            mcanv.addText(linepre, tag=vatag)
            mcanv.addText("FUNC: ")
            cconv = self.vw.getFunctionMeta(lva, 'CallingConvention', default='__unknown')
            mcanv.addNameText(cconv)
            mcanv.addText(' ')
            mcanv.addText(name, tag=vatag)


            # Render whatever we know about the function args.
            mcanv.addText("( ")
            for i,(atype,aname) in enumerate(self.vw.getFunctionArgs(lva)):
                mcanv.addNameText(atype.__name__)
                mcanv.addText(" ")
                mcanv.addNameText("%s_%d" % (aname,i))
                mcanv.addText(", ")
            mcanv.addText(")")

            # FIXME color code and get args parsing goin on
            mcanv.addText(" ")
            xrtag = mcanv.getTag("xrefs")
            mcanv.addText("[%d XREFS]\n" % xrcount, tag=xrtag)

            mcanv.addText(linepre, tag=vatag)
            mcanv.addText('\n')

            mcanv.addText(linepre, tag=vatag)
            mcanv.addText('Local Variables:\n')
            locals = self.vw.getFunctionLocals(lva)
            locals.sort(cmp=cmpoffset)
            lnames = [ '%s_%d' % (x[2],x[0]) for x in locals ]
            for i in xrange(len(locals)):
                offset, local_type, local_name = locals[i]
                local_name = lnames[i]
                mcanv.addText(linepre, tag=vatag)
                mcanv.addText('        ')
                mcanv.addNameText(local_name)
                #mcanv.addText(' ')
                #mcanv.addNameText(repr(local_type))
                mcanv.addText('\n')

            mcanv.addText(linepre, tag=vatag)
            mcanv.addText('\n')

        elif xrcount > 0 or name != None:
            mcanv.addText(linepre, tag=vatag)
            if name == None:
                name = "loc_%.8x" % lva # FIXME 64bit.
            mcanv.addText(name, tag=vatag)
            mcanv.addText(": ")
            xrtag = mcanv.getTag("xrefs")
            mcanv.addText("[%d XREFS]\n" % xrcount, tag=xrtag)

        if ltype == LOC_OP:

            mcanv.addText(linepre, tag=vatag)
            opbytes = mcanv.mem.readMemory(lva, lsize)
            mcanv.addText(opbytes[:8].encode('hex').ljust(17))

            # extra is the opcode object
            try:
                extra.render(mcanv)
            except Exception, e:
                import traceback
                traceback.print_exc()
                mcanv.addText("Opcode Render Failed: %s\n" % repr(extra))

            if cmnt != None:
                mcanv.addText("    ;%s" % cmnt, tag=cmnttag)

            mcanv.addText("\n")

        elif ltype == LOC_STRUCT:

            for soff, sind, sname, sobj in extra.vsGetPrintInfo():

                sva = lva + soff

                if soff != 0:
                    vastr = self.vw.arch.pointerString(sva)
                    linepre = "%s:%s  " % (segname, vastr)
                    vatag = mcanv.getVaTag(sva)

                mcanv.addText(linepre, tag=vatag)

                totag = None
                if isinstance(sobj, vs_prims.v_ptr):
                    stova = long(sobj)
                    stoname = self.vw.getName(stova)
                    if stoname == None:
                        stoname = repr(sobj)
                    if self.vw.isValidPointer(stova):
                        totag = mcanv.getVaTag(stova)

                # Insert the field name (and indent)
                mcanv.addText("  "*sind)
                mcanv.addNameText(sname)
                mcanv.addText(": ")

                # Insert the sobj info (if it's a primitive)
                if isinstance(sobj, vs_prims.v_prim):
                    if totag != None:
                        mcanv.addText(stoname, tag=totag)
                    else:
                        mcanv.addText(repr(sobj))

                if soff != 0:
                    xrefs = self.vw.getXrefsTo(sva)
                    if len(xrefs):
                        xrtag = mcanv.getTag("xrefs")
                        mcanv.addText("[%d XREFS]" % len(xrefs), tag=xrtag)

                # Handle the comment if present
                comment = self.vw.getComment(sva)
                if comment != None:
                    cmnttag = mcanv.getTag("comment")
                    mcanv.addText(comment, tag=cmnttag)

                mcanv.addText("\n")

        elif ltype == LOC_POINTER:

            fromva, tova, rtype, rflags = self.vw.getXrefsFrom(lva)[0] #FIXME hardcoded one
        
            pstr = self.vw.arch.pointerString(tova)

            mcanv.addText(linepre, tag=vatag)
            mcanv.addNameText("ptr: ")

            totag = mcanv.getVaTag(tova)
            pstr = self.vw.arch.pointerString(tova)

            mcanv.addText(pstr, tag=totag)

            name = self.vw.getName(tova)
            if name == None:
                name = "loc_%.8x" % tova #FIXME 64bit

            mcanv.addText(" (")
            mcanv.addText(name, tag=totag)
            mcanv.addText(")")
            if cmnt != None:
                cmnttag = mcanv.getTag("comment")
                mcanv.addText("    ;%s" % cmnt, tag=cmnttag)
            mcanv.addText("\n")

        elif ltype == LOC_UNDEF:

            mcanv.addText(linepre, vatag)
            offset,bytes = self.vw.getByteDef(lva)
            b = bytes[offset].encode('hex')
            mcanv.addNameText(b, typename="undefined")
            if cmnt != None:
                cmnttag = mcanv.getTag("comment")
                mcanv.addText(cmnt, tag=cmnttag)
            mcanv.addText("\n")

        elif ltype == LOC_IMPORT:

            mcanv.addText(linepre, vatag)
            tva = self.vw.vaByName(tinfo)
            mcanv.addText('IMPORT: ')
            if tva != None:
                mcanv.addVaText(tinfo, tva)
            else:
                mcanv.addText(tinfo)

            if cmnt != None:
                cmnttag = mcanv.getTag("comment")
                mcanv.addText(cmnt, tag=cmnttag)

            mcanv.addText("\n")

        else:
            tagname = location_tags.get(ltype, None)
            if tagname == None:
                tagname = "location"

            ltag = mcanv.getTag(tagname)
            cdone = False
            for line in self.vw.reprLocation(loc).split("\n"):
                mcanv.addText(linepre, tag=vatag)
                mcanv.addText(line, ltag)
                if not cdone:
                    cdone = True
                    if cmnt != None:
                        cmnttag = mcanv.getTag("comment")
                        mcanv.addText("    ;%s" % cmnt, tag=cmnttag)
                mcanv.addText("\n")

