'''
Gui objects for things in the envi package.
'''

from PyQt4 import QtCore, QtGui

import envi.memory as e_mem

import vqt.tree as vq_tree

class MemoryMapModel(vq_tree.VQTreeModel):
    columns = ('Address','Size','Perms','Filename')

class VQMemoryMapView(vq_tree.VQTreeView):
    def __init__(self, mem, parent=None):
        vq_tree.VQTreeView.__init__(self, parent=parent)
        self.mem = mem
        self.setModel(MemoryMapModel(parent=self))
        self.vqLoad()
        self.setWindowTitle('Memory Maps')

    def vqLoad(self):
        model = MemoryMapModel(parent=self)
        for mva, msize, mperm, mfile in self.mem.getMemoryMaps():
            pstr = e_mem.reprPerms(mperm)
            model.append(('0x%.8x' % mva, msize, pstr, mfile))
        self.setModel(model)

