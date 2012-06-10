import sys
from PyQt4 import QtCore, QtGui

from testmain import Ui_MainWindow

# Create a class for our main window
#class Main(QtGui.QMainWindow):
def sigClicked():
    return QtCore.SIGNAL('clicked()')

class SigSlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('signal & slot')

        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.connect(slider,  QtCore.SIGNAL('valueChanged(int)'), lcd, 
		QtCore.SLOT('display(int)') )

        self.resize(250, 150)

class TreeWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)

        tree = QtGui.QTreeView()
        model = MyModel(parent=self)
        tree.setModel(model)
        but  = QtGui.QPushButton('Whee!')
        self.connect(but, sigClicked(), self.wheeclicked)

        vbox.addWidget(tree)
        vbox.addWidget(but)

        self.setLayout(vbox)

    def wheeclicked(self):
        print 'WHEE CLICK'

class Grid(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit(self)
        authorEdit = QtGui.QLineEdit(self)
        reviewEdit = QtGui.QTextEdit(self)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        # NOTICE THIS SPANS GRID STUFFZ!
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)
        self.resize(350, 300)

        self.connect(titleEdit, QtCore.SIGNAL('textChanged(QString)'), self.onChanged)

    def onChanged(self, text):
        print 'Author Is Now: %s' % text

class FrameSplit(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)

        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)
 
        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle('QSplitter')


import time
import threading
def addrows(obj):
    time.sleep(5)
    for i in xrange(10):
        obj.rows.append(['Add %d' % i, i])
        obj.insertRow(obj.rowCount(None))
        time.sleep(1)

class MyTableModel(QtCore.QAbstractTableModel):

    columns = (
            ('Woot', None),
            ('Baz',  'setBaz'),
   )

    def __init__(self, parent=None):

        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self.rows = []

        self.rows.append(['Hehe!', 30])
        self.rows.append(['bazfaz', 40])

        #t = threading.Thread(target=addrows, args=(self,))
        #t.setDaemon(True)
        #t.start()

    def flags(self, index):
        #Qt.NoItemFlags	0	It does not have any properties set.
        #Qt.ItemIsSelectable	1	It can be selected.
        #Qt.ItemIsEditable	2	It can be edited.
        #Qt.ItemIsDragEnabled	4	It can be dragged.
        #Qt.ItemIsDropEnabled	8	It can be used as a drop target.
        #Qt.ItemIsUserCheckable	16	It can be checked or unchecked by the user.
        #Qt.ItemIsEnabled	32	The user can interact with the item.
        #Qt.ItemIsTristate	64	The item is checkable with three separate states.
        if not index.isValid():
            return 0
        flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        if self.columns[index.column()][1] != None:
            flags |= QtCore.Qt.ItemIsEditable
        return flags
        #return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def headerData(self, col, orient, role):
        #print 'headerData(%d, %d, %d)' % (col,orient,role)
        #print 'horiz',QtCore.Qt.Horizontal
        #print 'display',QtCore.Qt.DisplayRole
        #for name in dir(QtCore.Qt):
            #if name.lower().find('role') != -1:
                #print name,getattr(QtCore.Qt, name, None)
        if orient == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.columns[col][0]
        return None

    def data(self, index, role): 
        #print 'Index',index
        #print 'Role',role
        if not index.isValid(): 
            return None

        elif role != QtCore.Qt.DisplayRole: 
            return None

        #if index.row() == 0 and index.column() == 0:
            #return self._label

        # index.row() index.column()
        return self.rows[index.row()][index.column()]
        #return QtCore.QVariant(self.mydata[index.column()]) 

    def setData(self, qidx, value, role):
        #intval, isint = value.toInt()
        #print 'Row %d Col %d Value: %s' % (qidx.row(), qidx.column(), value.toInt())
        cbname = self.columns[qidx.column()][1]
        callback = getattr(self, cbname, None)
        if callback == None:
            raise Exception('Named table-set handler invalid: %s' % cbname)
        return callback(qidx, value)

    def setBaz(self, index, value):
        realval, isreal = value.toInt()
        if isreal:
            self.rows[index.row()][index.column()] = realval
        return isreal

    def columnCount(self, qidx):
        return len(self.columns)

    def rowCount(self, qidx):
        return len(self.rows)

class MyModel(QtCore.QAbstractItemModel):
    def __init__(self, parent=None):
        QtCore.QAbstractItemModel.__init__(self, parent=parent)
        self.mydata = [ 'asdf', 3 ]
        #self._label = QtGui.QLabel('woot', parent=parent)

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return 'Column%d' % col
            #return QtCore.QVariant(self.headerdata[col])
        return QtCore.QVariant()

    def hasChildren(self, index):
        print 'HAS CHILDREN',index
        return True
        #return False
    
    def data(self, index, role): 
        print 'Index',index
        print 'Role',role
        if not index.isValid(): 
            return QtCore.QVariant() 
        elif role != QtCore.Qt.DisplayRole: 
            return QtCore.QVariant() 
        #if index.row() == 0 and index.column() == 0:
            #return self._label
        # index.row() index.column()
        return QtCore.QVariant(self.mydata[index.column()]) 

    def index(self, row, col, object=None):
        print 'INDEX',row,col,object
        x = self.createIndex(row, col)
        print 'RETURNING',x
        return x

    #def flags(self, index):
#Qt.NoItemFlags	0	It does not have any properties set.
#Qt.ItemIsSelectable	1	It can be selected.
#Qt.ItemIsEditable	2	It can be edited.
#Qt.ItemIsDragEnabled	4	It can be dragged.
#Qt.ItemIsDropEnabled	8	It can be used as a drop target.
#Qt.ItemIsUserCheckable	16	It can be checked or unchecked by the user.
#Qt.ItemIsEnabled	32	The user can interact with the item.
#Qt.ItemIsTristate	64	The item is checkable with three separate states.
        #if not index.isValid():
            #return 0
        #return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def setData(self, qidx, value, role):
        intval, isint = value.toInt()
        print 'Row %d Col %d Value: %s' % (qidx.row(), qidx.column(), value.toInt())
        return True

    def columnCount(self, qidx):
        return 2

    def rowCount(self, qidx):
        return 2

    #def sort(self, Ncol, order):
        #"""Sort table by given column number.
        #"""
        #self.emit(SIGNAL("layoutAboutToBeChanged()"))
        #self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        #if order == Qt.DescendingOrder:
            #self.arraydata.reverse()
        #self.emit(SIGNAL("layoutChanged()"))
    
def addrows(obj):
    time.sleep(5)
    for i in xrange(10):
        print 'DOING ONE'
        time.sleep(1)
        x = obj.rowCount()
        obj.insertRow(x)
        obj.setItem(x, 0, QtGui.QTableWidgetItem('haha%d' % i))
        obj.setItem(x, 1, QtGui.QTableWidgetItem(i*300))

class MyTableWidget(QtGui.QTableWidget):
    def __init__(self, parent=None):
        QtGui.QTableWidget.__init__(self, parent=parent)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['asdf','qwer'])
        #t = threading.Thread(target=addrows, args=(self,))
        #t.setDaemon(True)
        #t.start()
        for i in xrange(10):
            #print 'DOING ONE'
            self.insertRow(i)
            self.setItem(i, 0, QtGui.QTableWidgetItem('haha%d' % i))
            self.setItem(i, 1, QtGui.QTableWidgetItem(str(i*300)))
        self.connect(self, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.itemDoubleClicked)

    def itemDoubleClicked(self, row, col):
        print 'DOUBLE CLICK'
        self.selectColumn(col)

class MainWin(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        #self.setStyleSheet('''
#QWidget {
    #background-color: #000000;
    #color: #00ff00;
#}
#
#QMenu{
    #background-color: black;
    #color: #00ff00;
#}
#
#QMainWindow::separator {
     #background: green;
     #width: 10px; /* when vertical */
     #height: 10px; /* when horizontal */
 #}
#
 #QMainWindow::separator:hover {
     #background: red;
 #}''')

        #a = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        a = QtGui.QAction('Stuff', self)
        #a.setShortcut('Ctrl+Q')
        a.setStatusTip('Do Stuff!')
        self.connect(a, QtCore.SIGNAL('triggered()'), self.stuff_clicked)

        m = self.menuBar()
        f = m.addMenu('&File')
        w = f.addMenu('&Woot')
        w.addAction(a)


        #for name in dir(QtCore.Qt):
            #if name.find('Dock') != -1:
                #print name

        #QtCore.Qt.AllDockWidgetAreas
        #QtCore.Qt.BottomDockWidgetArea
        #QtCore.Qt.DockWidgetArea
        #QtCore.Qt.DockWidgetArea_Mask
        #QtCore.Qt.DockWidgetAreas
        #QtCore.Qt.LeftDockWidgetArea
        #QtCore.Qt.NoDockWidgetArea
        #QtCore.Qt.RightDockWidgetArea
        #QtCore.Qt.TopDockWidgetArea

        # AnimatedDocks, AllowNestedDocks, AllowTabbedDocks, ForceTabbedDocks, VerticalTabs
        self.setDockOptions(self.AnimatedDocks)

        d = QtGui.QDockWidget(self)
        d.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        x = Grid(parent=self)
        d.setWidget(x)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, d)
        #self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, x)


        d1 = QtGui.QDockWidget(self)
        d1.setObjectName('DrawText')
        d1.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)

        tab = QtGui.QTabWidget(parent=self)
        tab.setMovable(True)
        tab.setTabsClosable(True)
        sa = QtGui.QScrollArea(parent=self)
        y = DrawText(parent=sa)
        sa.setWidget(y)
        tab.addTab(sa, 'Draw Text!')
        tab.addTab(ComboExample(parent=self), 'Combo Example!')

        d1.setWidget(tab)

        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, d1)

        d2 = QtGui.QDockWidget(self)
        d2.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        z = QtGui.QTableView()
        z.setModel(MyTableModel(parent=self))
        #z = MyTableWidget(parent=self)

        d2.setWidget(z)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, d2)

        #dd = DragDrop(parent=self)
        #self.setCentralWidget(dd)

        self.setGeometry(300, 300, 250, 150)
    def stuff_clicked(self):
        # Saves geometry/dock in for for the MainWindow
        print str(self.saveState()).encode('hex')

class TextBrowser(QtGui.QTextBrowser):

    def __init__(self, parent=None):
        QtGui.QTextBrowser.__init__(self, parent=parent)

        #self.setOpenLinks(False)
        #self.setMouseTracking(True)
        self.setStyleSheet('QWidget { background-color: black; color: #00ff00; }')
        self.document().setDefaultStyleSheet('''
b {
    background-color: #00ff00;
    color: black;
}
''')
        self.insertHtml('''
Some Text!<br>
<b>Some Bold Text!</b>
<a href="#NotAnAnchor">Anchor Link...</a>
''')

        self.connect(self, QtCore.SIGNAL("anchorClicked(QUrl)"), self.anchorClicked)
        
    def anchorClicked(self, url):
        print 'CLICK: ',url.toString()

class TextWindow(QtGui.QTextEdit):
    def __init__(self, parent=None):
        QtGui.QTextEdit.__init__(self, parent=parent)
        self.setReadOnly(True)
        self.insertPlainText('Woot woot!')
        self.setMouseTracking(True)

        self.setStyleSheet('''
QWidget {
    background-color: black;
    color: #00ff00;
}
''')

        self.document().setDefaultStyleSheet('''
b {
    background-color: #00ff00;
    color: black;
    font-weight: bold;
}

reg {
    background-color: red;
    color: blue;
}

reg.ahem {
    background-color: green;
    color: blue;
}

a {
    background-color: yellow;
    color: black;
}

a:hover {
    background-color: black;
    color: yellow;
}

b:hover {
    background-color: black;
    color: #00ff00;
}
''')

        self.insertHtml('''
<b>WOOT</b>
<script type=javascript>alert(0);</script>
<a name=0xf0f0f0f0>0xf0f0f0f0</a>
<reg class='ahem'>ahem</neato>
<reg class='wootreg'>wootreg</neato>
%s
Also, just some text
<a href="#0xf0f0f0f0">text</a>
''' % ('<hr>' * 200))

        #for f in self.document().rootFrame().begin():
        #print dir(self.document().rootFrame().begin().currentFrame())
        #print self.style()
        print type(self.styleSheet())
        for name in dir(self):
            if name.lower().find('cursor') != -1:
                print name

    def mouseDoubleClickEvent(self, mevent):
        #print dir(mevent)
        #print mevent.pos()
        a = self.anchorAt(mevent.pos())
        if a != None:
            self.scrollToAnchor(a)
            #cur = QtGui.QTextCursor(self.document())
            #cur = self.cursorForPosition(mevent.pos())
            #cur.beginEditBlock()
            cur = self.textCursor()
            cur.select(cur.LineUnderCursor)
            cur.removeSelectedText()
            cur.insertHtml('<reg>new text!</reg>')
            #cur.endEditBlock()
        #mevent.accept()
        QtGui.QTextEdit.mouseDoubleClickEvent(self, mevent)

    def mouseMoveEvent(self, mevent):
        #print 'moved',mevent.pos()
        QtGui.QTextEdit.mouseMoveEvent(self, mevent)

    def mouseReleaseEvent(self, mevent):
        print 'Click Release'
        QtGui.QTextEdit.mouseReleaseEvent(self, mevent)

class TestWindow(QtGui.QWidget):
    def __init__(self):
        #QtGui.QMainWindow.__init__(self)
        QtGui.QWidget.__init__(self)

        for name in  dir(self):
            if name.find('Event') != -1:
                print name

        self.setWindowTitle('Oh Hai!')

        #self.statusBar().showMessage('STATUS BAR READY!')
        
        self.setGeometry(300, 300, 250, 150)

        self.center()

        self.dbutton = QtGui.QPushButton("dialog")
        cancel = QtGui.QPushButton("Cancel")

        self.connect(self.dbutton, sigClicked(), self.dialog_clicked)
        self.connect(cancel, sigClicked(), self.stuffmenuitem)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.dbutton)
        vbox.addWidget(cancel)


        self.cb = QtGui.QCheckBox('Show title', self)
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus) # To make the checkbox not accept tabbed focus...
        self.cb.toggle()
        self.connect(self.cb, QtCore.SIGNAL('stateChanged(int)'), self.checkChange)

        vbox.addWidget(self.cb)

        pixmap = QtGui.QPixmap("129162873558291557.jpg")
        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        vbox.addWidget(label)

        self.setLayout(vbox)

    def checkChange(self, value):
        if self.cb.isChecked():
            self.setWindowTitle('Checkbox')
        else:
            self.setWindowTitle('')

        
    def dialog_clicked(self):

        #text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        #if ok:
            #print text

        # OMG YOU CAN USE CSS FOR COLORATION
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.dbutton.setStyleSheet("QWidget { background-color: %s }"
                % col.name())

        #font, ok = QtGui.QFontDialog.getFont()
        #if ok:
            #self.dbutton.setFont(font)
            #self.setFont(font)

        #filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    #'/home')
        #print 'FILENAME',filename
            
        
    def stuffmenuitem(self, event):
        print 'STUFF',event

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def resizeEvent(self, event):
        pass
        #print dir(event)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
         

         # This is always the same
         #self.ui=Ui_MainWindow()
         #self.ui.setupUi(self)
         #self.connect(self.ui.wootbutton, QtCore.SIGNAL('clicked()'), self.wootbutton_cb)

     #def wootbutton_cb(self, *args, **kwargs):
        #print 'WOOT:',args,kwargs

class ComboExample(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()


    def initUI(self):

        self.label = QtGui.QLabel("Ubuntu", self)

        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.label.move(50, 150)

        self.connect(combo, QtCore.SIGNAL('activated(QString)'), self.onActivated)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle('QComboBox')

    def onActivated(self, text):
        self.label.setText(text)
        self.label.adjustSize()

class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        QtGui.QPushButton.__init__(self, title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore() 

    def dropEvent(self, event):
        self.setText(event.mimeData().text()) 


class DragDrop(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.resize(280, 150)
        self.setWindowTitle('Simple Drag & Drop')

        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(170, 65)

        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)

class DrawText(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        but = QtGui.QPushButton('Woot Button', self)
        but.move(20,20)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Draw Text')

    def paintEvent(self, event):
        #print 'AHEM'
        paint = QtGui.QPainter()
        #print dir(paint)
        paint.begin(self)
        paint.setPen(QtGui.QColor(168, 34, 3))
        paint.setFont(QtGui.QFont('Decorative', 10))
        paint.drawText(event.rect(), QtCore.Qt.AlignCenter, 'Woot Woot!')

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#0f0')
        paint.setPen(color)
        #paint.setBrush(color)
        #paint.setBrush(None)
        paint.drawRect(10, 15, 90, 60)

        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        paint.setPen(pen)
        paint.drawLine(20, 40, 250, 40)

        pen.setStyle(QtCore.Qt.DashLine)
        paint.setPen(pen)
        paint.drawLine(20, 80, 250, 80)

        pen.setStyle(QtCore.Qt.DashDotLine)
        paint.setPen(pen)
        paint.drawLine(20, 120, 250, 120)

        pen.setStyle(QtCore.Qt.DotLine)
        paint.setPen(pen)
        paint.drawLine(20, 160, 250, 160)

        pen.setStyle(QtCore.Qt.DashDotDotLine)
        paint.setPen(pen)
        paint.drawLine(20, 200, 250, 200)

        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        paint.setPen(pen)
        paint.drawLine(20, 240, 250, 240)

        # Brush examples...

        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense1Pattern)
        paint.setBrush(brush)
        paint.drawRect(130, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense2Pattern)
        paint.setBrush(brush)
        paint.drawRect(250, 15, 90, 60)

        brush.setStyle(QtCore.Qt.Dense3Pattern)
        paint.setBrush(brush)
        paint.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.DiagCrossPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense5Pattern)
        paint.setBrush(brush)
        paint.drawRect(130, 105, 90, 60)

        brush.setStyle(QtCore.Qt.Dense6Pattern)
        paint.setBrush(brush)
        paint.drawRect(250, 105, 90, 60)

        brush.setStyle(QtCore.Qt.HorPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 195, 90, 60)

        brush.setStyle(QtCore.Qt.VerPattern)
        paint.setBrush(brush)
        paint.drawRect(130, 195, 90, 60)

        brush.setStyle(QtCore.Qt.BDiagPattern)
        paint.setBrush(brush)
        paint.drawRect(250, 195, 90, 60)
        

        paint.end()



def main():
     # Again, this is boilerplate, it's going to be the same on
     # almost every app you write
     app = QtGui.QApplication(sys.argv)
     window = MainWin()

     #window = TextWindow()
     #window = TextBrowser()
     #window  = TreeWindow()

     #window = TestWindow()
     #window = Grid()
     #window = SigSlot()
     #window = FrameSplit()
     #window = ComboExample()
     #window = DragDrop()
     #window = DrawText()

     window.show()
     # It's exec_ because exec is a reserved word in Python
     sys.exit(app.exec_())


if __name__ == "__main__":
     main()


