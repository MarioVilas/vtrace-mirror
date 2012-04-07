
from PyQt4 import QtCore, QtGui

import visgraph.pathcore as vg_path

class TreeItem(object):
    '''
    a python object used to return row/column data, and keep note of
    it's parents and/or children
    '''
    def __init__(self, person, parentItem):
        self.person = person
        self.parentItem = parentItem
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return 2
    
    def data(self, column):
        return 'col %d' % column
        #if self.person == None:
            #if column == 0:
                #return QtCore.QVariant(self.header)
            #if column == 1:
                #return QtCore.QVariant("")                
        #else:
            #if column == 0:
                #return QtCore.QVariant(self.person.sname)
            #if column == 1:
                #return QtCore.QVariant(self.person.fname)
        #return QtCore.QVariant()

    def parent(self):
        return self.parentItem
    
    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0

class treeModel(QtCore.QAbstractItemModel):
    '''
    '''

    columns = ( 'A first column!', 'The Second Column!')

    def __init__(self, parent=None):
        QtCore.QAbstractItemModel.__init__(self, parent=parent)
        self.rootnode = vg_path.newPathNode()
        for i in xrange(20):
            n = self.vwAddRow(('asdf %d' % i, 'qwer %d' % i))
            for j in xrange(3):
                self.vwAddRow([ 'WOOT_%d_%d' % (i,j), 'foobar...' ], parent=n)

    def vwAddRow(self, rowdata, parent=None):
        if parent == None:
            parent = self.rootnode
        if len(rowdata) != len(self.columns):
            x = (len(rowdata), len(self.columns))
            raise Exception('Invalid Row (len %d should be %d)' % x)
        node = vg_path.newPathNode(parent=parent, QColumns=list(rowdata))
        return node

    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()

        node = index.internalPointer()
        if role == QtCore.Qt.DisplayRole:

            columns = vg_path.getNodeProp(node, 'QColumns')
            if columns == None:
                return QtCore.QVariant()

            col = index.column()
            if col >= len(columns):
                return QtCore.QVariant()

            return columns[col]

        if role == QtCore.Qt.UserRole:
            return node

        return QtCore.QVariant()

    def headerData(self, column, orientation, role):
        if ( orientation == QtCore.Qt.Horizontal and
             role == QtCore.Qt.DisplayRole):

            return self.columns[column]

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            node = self.rootnode
        else:
            node = parent.internalPointer()

        knode = vg_path.getNodeKids(node)[row]
        return self.createIndex(row, column, knode)

    def parent(self, index):

        if not index.isValid():
            return QtCore.QModelIndex()

        node = index.internalPointer()
        pnode = vg_path.getNodeParent(node)
        if pnode == self.rootnode:
            return QtCore.QModelIndex()

        return self.createIndex(index.row(), 0, pnode)

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.column() > 0:
            return 0
        node = parent.internalPointer()
        if not parent.isValid():
            node = self.rootnode
        return len(vg_path.getNodeKids(node))
    
if __name__ == '__main__':

    app = QtGui.QApplication([])
    
    model = treeModel()
    dialog = QtGui.QDialog()

    dialog.setMinimumSize(300,150)
    layout = QtGui.QVBoxLayout(dialog)

    tv = QtGui.QTreeView(dialog)
    tv.setModel(model)
    tv.setAlternatingRowColors(True)
    layout.addWidget(tv)
    
    label = QtGui.QLabel("Search for the following person")
    layout.addWidget(label)

    dialog.exec_()

    app.closeAllWindows()
