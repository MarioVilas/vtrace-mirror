
from PyQt4 import QtCore, QtGui

import vqwidget.main as vq_main
import re

class VQSyntaxHighlighter(QtGui.QSyntaxHighlighter):

    def __init__(self, textedit):
        QtGui.QSyntaxHighlighter.__init__(self, textedit)
        self.highword = 'omg hai!'
        self.deffmt = QtGui.QTextCharFormat()
        self.deffmt.setForeground(QtGui.QBrush(QtGui.QColor('#000000')))
        self.deffmt.setBackground(QtGui.QBrush(QtGui.QColor('#00ff00')))
        self.fmtcur = QtGui.QTextCursor(self.document())

    def dostuff(self, s):
        self.highword = '\\b%s\\b' % s
        self.rehighlight()

    def highlightBlock(self, text):
        # FIXME pre-compile regex's?

        block = self.currentBlock()
        blockoff = block.position()
        for match in re.finditer(self.highword, text):
            off = match.start()
            self.fmtcur.setPosition(blockoff + off )
            x = self.fmtcur.charFormat()
            #fg = x.foreground().color()
            #bg = x.background().color()
            x.setBackground(QtGui.QBrush(QtGui.QColor('#000000')))
            x.setForeground(QtGui.QBrush(QtGui.QColor('#00ff00')))
            print 'MATCH',text[match.start():match.end()]

            self.setFormat(off, match.end()-off, x)

class MyTest(QtGui.QTextEdit):
    def __init__(self):
        QtGui.QTextEdit.__init__(self, parent=None)
        self.cursorPositionChanged.connect(self.cursorChanged)
        c = self.textCursor()
        cfmt = c.charFormat()
        #self.deffmt.setForeground(QtGui.QBrush(QtGui.QColor('#000000')))
        #self.deffmt.setBackground(QtGui.QBrush(QtGui.QColor('#00ff00')))
        cfmt.setBackground(QtGui.QBrush(QtGui.QColor('#000000')))
        cfmt.setForeground(QtGui.QBrush(QtGui.QColor('#00ff00')))
        c.setCharFormat(cfmt)
        self.setReadOnly(True)
        self.setText('Hi this this is kewl!')

        self.shighlight = VQSyntaxHighlighter(self)

    def cursorChanged(self):
        c = self.textCursor()
        #b = c.block()
        ##print 'BLOCK',str(b.text())
        c.select(c.WordUnderCursor)
        #cfmt = c.charFormat()
        ##print cfmt
        ##cfmt.setFontStrikeOut(not cfmt.fontStrikeOut())
        ##c.setCharFormat(cfmt)

            ##x = self.fmtcur.charFormat()
        #fg = cfmt.foreground().color()
        #bg = cfmt.background().color()
        #cfmt.setBackground(QtGui.QBrush(fg))
        #cfmt.setForeground(QtGui.QBrush(bg))

        ##self.setFormat(off, match.end()-off, x)
        #c.setCharFormat(cfmt)

        x = c.selectedText()
        self.shighlight.dostuff(x)
        #print 'CURSOR SELECTED',x

if __name__ == '__main__':

    #model = treeModel()
    #dialog = QtGui.QDialog()

    #dialog.setMinimumSize(300,150)
    #layout = QtGui.QVBoxLayout(dialog)

    #tv = QtGui.QTreeView(dialog)
    #tv.setModel(model)
    #tv.setAlternatingRowColors(True)
    #layout.addWidget(tv)
    
    #label = QtGui.QLabel("Search for the following person")
    #layout.addWidget(label)

    #dialog.exec_()

    #app.closeAllWindows()
    vq_main.startup()
    #app = QtGui.QApplication([])

    #db = vdb.Vdb()
    #w = VdbWindow(db)
    #t = vdb.VdbTrace(db)
    #w.show()
    win = MyTest()
    win.show()

    vq_main.main()
