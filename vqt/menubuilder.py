
from PyQt4 import QtCore, QtGui

class FieldAdder:
    def __init__(self, menu, splitchar='.'):
        self.splitchar = splitchar
        self.menu = menu
        self.menu.idx = 0
        self.menu.kids = {}

    def addField(self, pathstr, callback=None, args=(), tip=None):
        parent = self.menu
        kid = self.menu
        plist = pathstr.split(self.splitchar)

        for p in plist[:-1]:
            kid = parent.kids.get(p)
            if kid == None:
                kid = VQMenu(p, parent=parent)
                action = parent.addMenu(kid)
                parent.kids[p] = kid
                parent.idx += 1
            parent = kid

        action = VQAction(plist[-1], kid, callback, args)

        if tip: action.setStatusTip(tip)

        kid.addAction(action)

        return kid

class VQMenuBar(FieldAdder, QtGui.QMenuBar):
    def __init__(self, parent=None):
        QtGui.QMenuBar.__init__(self, parent=parent)
        FieldAdder.__init__(self, self)

class VQAction(QtGui.QAction):

    def __init__(self, aname, parent=None, callback=None, args=()):
        QtGui.QAction.__init__(self, aname, parent)
        self._a_callback = callback
        self._a_args = args

        self.connect(self, QtCore.SIGNAL('triggered()'), self._a_triggered)

    def _a_triggered(self):
        if self._a_callback:
            args = self._a_args
            self._a_callback(*args)

class VQMenu(FieldAdder, QtGui.QMenu):

    def __init__(self, name, parent=None):
        QtGui.QMenu.__init__(self, name, parent=parent)
        FieldAdder.__init__(self, self)
        self.idx = 0
        self.kids = {}

        self._menu_cbargs = ()
        self._menu_callback = None

