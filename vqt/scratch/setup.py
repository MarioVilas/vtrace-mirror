import sys
import os
from distutils.core import setup, Extension

# To gen docs:
# /opt/local/Library/Frameworks/Python.framework/Versions/2.4/bin/epydoc --html -o docs -c docs/epydoc.css vtrace

try:
    import ctypes
except Exception, e:
    print "ERROR: you *need* a working ctypes install:",e
    sys.exit(0)

mods = []
pkgdata = {}

packages = [
    "cobra",
    "Elf",
    "envi",
    "envi.disassemblers",
    "envi.disassemblers.libdisassemble",
    "PE",
    "vivisect",
    "vivisect.analysis",
    "vivisect.analysis.elf",
    "vivisect.analysis.generic",
    "vivisect.analysis.i386",
    "vivisect.analysis.ms",
    "vivisect.contrib",
    "vivisect.gui",
    "vivisect.impemu",
    "vivisect.parsers",
    "vivisect.reports",
    "vivisect.storage",
    "vivisect.vamp",
    "vstruct",
    "vtrace",
    "vtrace.archs",
    "vtrace.platforms",
    "vtrace.tools",
    "vwidget",
]

pkgdata["vtrace"] = ["platforms/dbghelp.dll","platforms/symsrv.dll"]

setup  (name        = 'vivisect',
        version     = '1.0',
        description = 'Kenshoto Python Reversing API',
        packages  = packages,
        scripts   = ["vivbin",],
        pkg_data  = pkgdata,
       )

