'''
The gui related elements used for code diffing.

GUI TODO:
  * symbol name transfer
  * block difference highlight
  * common list with clickthrough update both GUIs
  * Likely matches for each "unique"
  * Manual match selection

'''
import vivisect.gui as viv_gui
import vivisect.gui.viv_views as vg_views

import vivisect.codediff as viv_codediff

class VivCodeDiffView(vg_views.VivTreeView):
    pass


class ViviCodeDiffWindow(viv_gui.VivWindow):

    def __init__(self, vw):
        pass

