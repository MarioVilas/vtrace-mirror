from PyQt4 import QtCore, QtGui, QtWebKit

class NodeColumn(QtGui.QGraphicsItem):

    def __init__(self, vg, nodes, scene, left=None, right=None):
        QtGui.QGraphicsItem.__init__(self, scene=scene)
        self.setZValue( -100 ) # Get behind click events...

        self._v_vg = vg
        self._v_lines = []
        self._v_nodes = nodes

        # Remember if we srarted with something on our right or left
        self._v_goleft = (left == None)
        self._v_goright = (right == None)

        self._v_left = left
        self._v_right = right

        offset = 0
        for nid,nprops in nodes:
            txt = QGraphNode(vg, self, nid, nprops, scene=scene)
            txt.setY( offset )
            offset += txt.boundingRect().height()

    def takeOverView(self):
        self._removeLeft()
        self._removeRight()
        self.setX(0)
        self.setY(0)
        self._v_goleft = True
        self._v_goright = True

    def _removeLeft(self):
        left = self._v_left
        while left:
            nextleft = left._v_left
            left.removeColumn()
            left = nextleft

    def _removeRight(self):
        right = self._v_right
        while right:
            nextright = right._v_right
            right.removeColumn()
            right = nextright

    def removeColumn(self):
        scene = self.scene()
        for item in self._v_lines:
            scene.removeItem( item )
        scene.removeItem( self )

    def boundingRect(self):
        return self.childrenBoundingRect()

    def paint(self, x, y, z): pass

    def getRightBoundary(self):
        rect = self.boundingRect()
        return self.x() + rect.width()

    def getLeftBoundary(self):
        return self.x()

    def getYMid(self):
        return self.y() + (self.boundingRect().height() / 2)

    def drawLinesTo(self, colnode):
        '''
        Draw lines to our nodes from the specified one
        (used when we are on the right...)
        '''
        scene = self.scene()
        colpos = colnode.scenePos()
        colrect = colnode.boundingRect()

        ecolor = self._v_vg.getMeta('edgecolor', '#000')
        pen = QtGui.QPen( QtGui.QColor( ecolor ) )

        for item in self.childItems():
            itpos = item.scenePos()
            itrect = item.boundingRect()

            x1 = colpos.x() + colrect.width()
            y1 = colpos.y() + (colrect.height() / 2 )

            x2 = itpos.x()
            y2 = itpos.y() + ( itrect.height() / 2)

            lineitem = scene.addLine(x1, y1, x2, y2, pen=pen)
            self._v_lines.append( lineitem )
            #lineitem.setParentItem(self)

    def drawLinesFrom(self, colnode):
        '''
        Draw lines from our nodes to the specified one
        (used when we are on the left...)
        '''
        scene = self.scene()
        colpos = colnode.scenePos()
        colrect = colnode.boundingRect()

        ecolor = self._v_vg.getMeta('edgecolor', '#000')
        pen = QtGui.QPen( QtGui.QColor( ecolor ) )

        for item in self.childItems():
            itpos = item.scenePos()
            itrect = item.boundingRect()

            x1 = itpos.x() + itrect.width()
            y1 = itpos.y() + ( itrect.height() / 2 )

            x2 = colpos.x()
            y2 = colpos.y() + ( colrect.height() / 2)

            lineitem = scene.addLine(x1, y1, x2, y2, pen=pen)
            self._v_lines.append( lineitem )
            #lineitem.setParentItem(self)

    def expandNode(self, colnode):

        mymid = colnode.scenePos().y()

        if self._v_goleft:

            self._removeLeft()

            nodes = [ (n1, self._v_vg.getNodeProps(n1)) for (eid, n1, n2, einfo) in self._v_vg.getRefsTo( colnode._v_nid ) ]

            col = NodeColumn( self._v_vg, nodes, self.scene(), right=self )
            hiswidth = col.boundingRect().width()
            col.setX( self.getLeftBoundary() - hiswidth - 20 )

            # Check if we want to scoot it down...
            hismid = col.getYMid()
            if hismid < mymid:
                col.setY( col.y() + (mymid - hismid) )

            col.drawLinesFrom( colnode )

            self._v_left = col

        if self._v_goright:

            self._removeRight()

            nodes = [ (n2, self._v_vg.getNodeProps(n2)) for (eid, n1, n2, einfo) in self._v_vg.getRefsFrom( colnode._v_nid ) ]

            col = NodeColumn( self._v_vg, nodes, self.scene(), left=self )
            col.setX( self.getRightBoundary() + 20 )

            # Check if we want to scoot it down...
            hismid = col.getYMid()
            if hismid < mymid:
                col.setY( col.y() + (mymid - hismid) )

            col.drawLinesTo( colnode )
            self._v_right = col

class QGraphNode(QtGui.QGraphicsSimpleTextItem):

    def __init__(self, vg, column, nid, nprops, scene=None):

        QtGui.QGraphicsSimpleTextItem.__init__(self, nprops.get('repr', 'node:%d' % nid), scene=scene, parent=column)

        self._v_vg = vg
        self._v_nid = nid
        self._v_nprops = nprops

        color = vg.getMeta('nodecolor', 'green')
        color = nprops.get('color', color)

        brush = QtGui.QBrush( QtGui.QColor( color ) )
        self.setBrush( brush )

    # TODO mouseDoubleClickEvent to take over center of view.

    def mousePressEvent(self, event):
        self.parentItem().expandNode( self )
        # Our scene's parent is a QGraphTreeView...
        self.scene().parent()._sig_NodeSelected.emit(self._v_nid, self._v_nprops)

    def contextMenuEvent(self, event):
        pos = self.scene().parent().mapFromGlobal(QtGui.QCursor.pos()) # FIXME cheating
        self.scene().parent()._sig_NodeContextMenu.emit(pos, self._v_nid, self._v_nprops)

class QGraphTreeView(QtGui.QGraphicsView):

    _sig_NodeSelected = QtCore.pyqtSignal(int, dict)
    _sig_NodeContextMenu = QtCore.pyqtSignal( object, int, dict ) # pos, nid, nprops

    def __init__(self, vg, nodes, parent=None):
        QtGui.QGraphicsView.__init__(self, parent=parent)
        scene = QtGui.QGraphicsScene(parent=self)

        self.setScene( scene )
        self._v_nodecol = NodeColumn(vg, nodes, scene)
        self._v_vg = vg

    def loadNewGraph(self, vg, nodes):

        # setup default meta colors
        color = vg.getMeta('bgcolor', '#000000')
        self.scene().setBackgroundBrush( QtGui.QBrush( QtGui.QColor( color ) ) )

        self._v_nodecol._removeLeft()
        self._v_nodecol._removeRight()
        self._v_nodecol.removeColumn()

        self._v_nodecol = NodeColumn(vg, nodes, self.scene() )
        self._v_vg = vg

if __name__ == '__main__':

    import sys
    import visgraph.graphcore as vg_graphcore

    app = QtGui.QApplication(sys.argv)
    app.setFont( QtGui.QFont('Courier') )

    initnodes = [ (i, {'repr':'node%d' % i}) for i in xrange( 30 ) ]

    # Build up a fake graph
    vg = vg_graphcore.Graph()
    for nid,nprops in initnodes:
        vg.addNode(nodeid=nid, repr='node %d' % nid)

    for nid,nprops in initnodes:
        for knid,knprops in initnodes:
            if nid == knid:
                continue
            vg.addEdge(nid, knid)

    win = QGraphTreeView( vg, initnodes, parent=None )

    win.show()
    app.exec_()

