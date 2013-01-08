"""
Code for generating implib profiles for vivisect workspaces.
"""

import sys

import vivisect.impemu.impmagic as v_impmagic
import vivisect.impemu.emufunc as v_emufunc

import inspect

def printEmuFunc(tofile, classname, callconv, names, args):
    tofile.write("#EMUFUNC:%s\n" % classname)
    tofile.write("class %s(emufunc.EmuFunc):\n" % classname)
    tofile.write("    __callconv__ = '%s'\n" % callconv)
    tofile.write("    __argn__ = %s\n" % repr(names))
    tofile.write("    __argt__ = [")
    for t in args:
        mname = t.__module__.split(".")[-1]
        if mname == "impmagic":
            tofile.write("%s, " % t.__name__)
        else:
            tofile.write("%s.%s, " % (mname, t.__name__))
    tofile.write("]\n")
    tofile.write("#EMUFUNCDONE\n\n")

def genProfile(vw, tofile=None):

    if tofile == None:
        tofile = file("output.py","w")

    magicbase = "vivisect.impemu.impmagic."
    iemubase = "%s." % vw.getMeta("ImportEmulation")

    deltas = {}

    for eva,etype,ename,efname in vw.getExports():

        if not vw.isFunction(eva):
            continue

        funcva = eva

        callconv = vw.getFunctionMeta(funcva, "CallingConvention", None)
        if callconv == None:
            continue

        alist = vw.getFunctionArgs(funcva)
        argn = [y for x,y in alist]
        argt = [x for x,y in alist]
        argc = len(argt)

        # Merge what we have with existing import emu stuff by precedence
        impfunc = vw.getImpEmuFunc("%s.%s" % (efname, ename))

        if not isinstance(impfunc, v_emufunc.WrapperFunc):

            changes = False

            newargc = len(alist)
            final_args = [v_impmagic.Unknown for i in range(newargc)]
            final_names = [None for i in range(newargc)]

            # Fill in the defaults (from the old emu func)
            for i in range(min(newargc, impfunc.argc)):
                final_names[i] = impfunc.argn[i]
                final_args[i] = impfunc.argt[i]

            # Fill in emulation derived over-rides
            for i in range(min(newargc,argc)):

                # Allow a new name to only over-ride a none.
                if final_names[i] == None:
                    final_names[i] = argn[i]

                # Allow precendent over-ride
                if final_args[i].__precedence__ < argt[i].__precedence__:
                    final_args[i] = argt[i]

            if final_names != impfunc.argn:
                print "OLD NAMES: %s" % repr(impfunc.argn)
                print "NEW NAMES: %s" % repr(final_names)
                changes = True

            if final_args != impfunc.argt:
                print "OLD ARGS: %s" % repr([x.__name__ for x in impfunc.argt])
                print "NEW ARGS: %s" % repr([x.__name__ for x in final_args])
                changes = True

            if changes:

                printEmuFunc(sys.stdout, ename, callconv, final_names, final_args)
                print "Merge? (y/n)"
                if sys.stdin.readline() == "y\n":
                    deltas[ename] = (callconv, final_names, final_args)
                else:
                    print "Skipped..."

            else:
                print "#Unchanged %s" % ename

        else:
            deltas[ename] = (callconv, [y for x,y in alist], [x for x,y in alist])
            printEmuFunc(sys.stdout, ename, *deltas.get(ename))

            #print "#Adding..."
            #print "class %s(impmagic.EmuFunc):" % ename
            #print "    __callconv__ = '%s'" % callconv
            #print "    __argn__ = %s" % repr([y for x,y in alist])
            #print "    __argt__ = [",
            #for x,y in alist:
                #FIXME not everything will be a submod of magic...
                #mr = x.__module__.split(".")
                #m = mr[-1]
                #print "%s.%s," % (m,x.__name__),
            #print "]"


    modname = "%s%s" % (iemubase, efname)
    try:
        __import__(modname)
    except Exception, e:
        print e
    mod = sys.modules.get(modname, None)
    print "MOD",modname,mod
    if mod != None:
        eat = False
        for line in inspect.getsource(mod).split("\n"):

            if line.startswith("#EMUFUNCDONE"):
                if eat:
                    eat = False
                    continue

            elif line.startswith("#EMUFUNC:"):
                tag,classname = line.split(":")
                classname = classname.strip()

                d = deltas.pop(classname, None)
                if d != None:
                    eat = True
                    printEmuFunc(tofile, classname, *d)

            if eat: continue

            tofile.write(line+"\n")

    cnames = deltas.keys()
    cnames.sort()

    for classname in cnames:
        printEmuFunc(tofile, classname, *deltas.pop(classname))
       
