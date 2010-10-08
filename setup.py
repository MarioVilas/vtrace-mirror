import sys
from distutils.core import setup, Extension

# To gen docs:
# /opt/local/Library/Frameworks/Python.framework/Versions/2.4/bin/epydoc --html -o docs -c docs/epydoc.css vtrace

packages = [
    "cobra",
    "Elf",
    "envi",
    "envi.disassemblers",
    "envi.disassemblers.libdisassemble",
    "PE",
    "vdb",
    "vdb.extensions",
    "vdb.gui",
    "vdb.gui.extensions",
    "vstruct",
    "vtrace",
    "vtrace.archs",
    "vtrace.platforms",
    "vtrace.tools",
    "vwidget",
]

mods = []
pkgdata = {}

if sys.platform == "darwin":
    mods.append(Extension('mach', sources = ['mach/machmodule.c','mach/task.c', 'mach/thread.c', 'mach/utility.c']))

# Install the dbghelp library
pkgdata["vtrace"] = ["platforms/dbghelp.dll","platforms/symsrv.dll"]
pkgdata["vdb"] = ["configs/*","glade/*"]

setup  (name        = 'VDB',
        version     = '2.0',
        description = 'VDB',
        packages  = packages,
        package_data = pkgdata,
        scripts = ["vdbbin",],
        ext_modules = mods,
       )


