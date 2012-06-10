
"""
Functions for exporting/importing a vivisect workspace
"""

import cPickle as pickle

import vivisect
from vivisect.const import *

FORMAT_VERSION=1

def vivexport(vw):
    raise Exception('vivisect.export.vivexport() SHOULD NO LONGER BE USED!, use vw.exportWorkspace()')

# Keeping this code around to import old style workspaces...
def vivimport(vw, edict):

    ver = edict.get("ver")

    amods = edict.get("amods")
    if amods != None:
        for name in amods:
            vw._fireEvent(VWE_ADDMODULE, name)

    frefs = edict.get("frefs")
    if frefs != None:
        for fref in frefs:
            vw._fireEvent(VWE_ADDFREF, fref)

    fmods = edict.get("fmods")
    if fmods != None:
        for name in fmods:
            vw._fireEvent(VWE_ADDFMODULE, name)

    cmaps = edict.get("colormaps")
    if cmaps != None:
        for coltup in cmaps:
            vw._fireEvent(VWE_ADDCOLOR, coltup)

    vasetlist = edict.get("vasetlist")
    if vasetlist != None:
        for row in vasetlist:
            vw._fireEvent(VWE_ADDVASET,row)

    # Gotta import meta first to get things like arch all set
    meta = edict.get("meta")
    if meta != None:
        for key,val in meta.items():
            #FIXME possibly make storage format tuples...
            vw._fireEvent(VWE_SETMETA,(key,val))

    files = edict.get("files")
    if files != None:
        for ftup in files:
            vw._fireEvent(VWE_ADDFILE,ftup)

    maps = edict.get("memmaps")
    if maps != None:
        for maptup in maps:
            vw._fireEvent(VWE_ADDMMAP,maptup)

    segs = edict.get("segments")
    if segs != None:
        for row in segs:
            vw._fireEvent(VWE_ADDSEGMENT,row)

    exps = edict.get("exports")
    if exps != None:
        for e in exps:
            vw._fireEvent(VWE_ADDEXPORT,e)

    relocs = edict.get("relocations")
    if relocs != None:
        for rtup in relocs:
            vw._fireEvent(VWE_ADDRELOC,rtup)

    funcs = edict.get("functions")
    if funcs != None:
        for ftup in funcs:
            vw._fireEvent(VWE_ADDFUNCTION,ftup)

    blocks = edict.get("codeblocks")
    if blocks != None:
        for btup in blocks:
            vw._fireEvent(VWE_ADDCODEBLOCK,btup)

    names = edict.get("names")
    if names != None:
        for ntup in names:
            vw._fireEvent(VWE_SETNAME,ntup)

    # FIXME LEGACY ( these are now in function meta!
    fargset = edict.get("fargs")
    if fargset != None:
        for fva,alist in fargset.iteritems():
            args = []
            for mname,cname,aname in alist:
                try:
                    m = __import__(mname,0,0,1)
                    c = getattr(m,cname)
                    args.append((c,aname))
                except Exception,e:
                    print e
                    args.append((None, aname))
            vw.setFunctionArgs(fva, args)

    locs = edict.get("locations")
    if locs != None:
        for ltup in locs:
            vw._fireEvent(VWE_ADDLOCATION,ltup)

    xrefs = edict.get("xrefs")
    if xrefs != None:
        for xtup in xrefs:
            vw._fireEvent(VWE_ADDXREF,xtup)

    comments = edict.get("comments")
    if comments != None:
        for ctup in comments:
            vw._fireEvent(VWE_COMMENT,ctup)

    siglist = edict.get("siglist")
    if siglist != None:
        for bytes, mask in siglist:
            vw.addFunctionSignatureBytes(bytes, mask)

    # Pull in any stored symbol hints
    for row in edict.get('symhints', []):
        vw._fireEvent(VWE_SYMHINT,row)


