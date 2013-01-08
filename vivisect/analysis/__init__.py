
"""
The analysis package.  Modules in this directory are responsible
for different phases of analysis on different platforms.
"""


def addAnalysisModules(vw):

    import vivisect.analysis.i386 as viv_analysis_i386

    arch = vw.getMeta('Architecture')
    fmt  = vw.getMeta('Format')
    plat = vw.getMeta('Platform')

    if fmt == 'pe':

        vw.addAnalysisModule("vivisect.analysis.pe")
        vw.impmod = vw.loadModule('vivisect.impemu.windows') # FIXME this shouldn't be here!

        if arch == 'i386':

            #import vivisect.impapi.windows.i386 as api_windows_i386
            #vw._loadImportApi( api_windows_i386.api )

            viv_analysis_i386.addEntrySigs(vw)
            vw.addAnalysisModule("vivisect.analysis.i386.importcalls")
            vw.addStructureModule('ntdll', 'vstruct.defs.windows.win_5_1_i386.ntdll')

        elif arch == 'amd64':

            #import vivisect.impapi.windows.amd64 as api_windows_amd64
            #vw._loadImportApi( api_windows_amd64.api )

            vw.addStructureModule('ntdll', 'vstruct.defs.windows.win_6_1_amd64.ntdll')

        vw.addConstModule('vstruct.constants.ntstatus')

        vw.addAnalysisModule("vivisect.analysis.generic.funcentries")
        vw.addAnalysisModule("vivisect.analysis.generic.relocations")
        vw.addAnalysisModule("vivisect.analysis.generic.pointertables")

        vw.addAnalysisModule("vivisect.analysis.ms.vftables")

        vw.addAnalysisModule("vivisect.analysis.generic.emucode")

        vw.addFuncAnalysisModule("vivisect.analysis.generic.codeblocks")
        vw.addFuncAnalysisModule("vivisect.analysis.ms.hotpatch")
        vw.addFuncAnalysisModule("vivisect.analysis.ms.msvc")

        # Snap in an architecture specific emulation pass
        if arch == 'i386':
            vw.addFuncAnalysisModule("vivisect.analysis.i386.calling")

        elif arch == 'amd64':
            vw.addFuncAnalysisModule("vivisect.analysis.amd64.emulation")

        # See if we got lucky and got arg/local hints from symbols
        vw.addAnalysisModule('vivisect.analysis.ms.localhints')
        # Find import thunks
        vw.addFuncAnalysisModule("vivisect.analysis.generic.thunks")

    elif fmt == 'elf': # ELF ########################################################

        vw.addAnalysisModule("vivisect.analysis.elf")
        vw.impmod = vw.loadModule('vivisect.impemu.posix') # FIXME this should not be here

        if arch == 'i386':
            viv_analysis_i386.addEntrySigs(vw)
            vw.addAnalysisModule("vivisect.analysis.i386.importcalls")

        vw.addAnalysisModule("vivisect.analysis.generic.funcentries")
        vw.addAnalysisModule("vivisect.analysis.generic.relocations")
        vw.addAnalysisModule("vivisect.analysis.generic.pointertables")
        vw.addAnalysisModule("vivisect.analysis.generic.emucode")

        # Get PLTs taken care of early
        vw.addFuncAnalysisModule("vivisect.analysis.elf.elfplt")
        # Generic code block analysis
        vw.addFuncAnalysisModule("vivisect.analysis.generic.codeblocks")

        # Add our emulation modules
        if arch == 'i386':
            vw.addFuncAnalysisModule("vivisect.analysis.i386.calling")
        elif arch == 'amd64':
            vw.addFuncAnalysisModule("vivisect.analysis.amd64.emulation")

        # Find import thunks
        vw.addFuncAnalysisModule("vivisect.analysis.generic.thunks")

    elif fmt == 'macho': # MACH-O ###################################################

        if arch == 'i386':
            viv_analysis_i386.addEntrySigs(vw)
            vw.addAnalysisModule("vivisect.analysis.i386.importcalls")

        # Add the one that brute force finds function entry signatures
        vw.addAnalysisModule("vivisect.analysis.generic.funcentries")
        vw.addAnalysisModule("vivisect.analysis.generic.relocations")
        vw.addAnalysisModule("vivisect.analysis.generic.pointertables")
        vw.addAnalysisModule("vivisect.analysis.generic.emucode")

        vw.addFuncAnalysisModule("vivisect.analysis.generic.codeblocks")

        if arch == 'i386':
            vw.addFuncAnalysisModule("vivisect.analysis.i386.calling")

        elif arch == 'amd64':
            vw.addFuncAnalysisModule("vivisect.analysis.amd64.emulation")

        vw.addFuncAnalysisModule("vivisect.analysis.generic.thunks")

    elif fmt == 'blob': # BLOB ######################################################

        vw.addAnalysisModule("vivisect.analysis.generic.funcentries")
        vw.addAnalysisModule("vivisect.analysis.generic.relocations")
        vw.addAnalysisModule("vivisect.analysis.generic.pointertables")
        vw.addAnalysisModule("vivisect.analysis.generic.emucode")

        vw.addFuncAnalysisModule("vivisect.analysis.generic.codeblocks")
        vw.addFuncAnalysisModule("vivisect.analysis.generic.thunks")

    else:

        raise Exception('Analysis modules unknown for format: %s' % fmt)

