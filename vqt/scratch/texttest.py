import re
import sys

from PyQt4 import QtCore, QtGui

class VQHighlight(QtGui.QSyntaxHighlighter):

    highword = 'neato'

    deffmt = None # FIXME

    def highlightBlock(self, text):
        # FIXME pre-compile regex's?
        self.deffmt = QtGui.QTextCharFormat()
        self.deffmt.setForeground(QtGui.QBrush(QtGui.QColor('#000000')))
        self.deffmt.setBackground(QtGui.QBrush(QtGui.QColor('#00ff00')))

        block = self.currentBlock()
        blockoff = block.position()
        cur = QtGui.QTextCursor(self.document())
        for match in re.finditer(self.highword, text):
            #print dir(match)
            off = match.start()

            cur.setPosition(blockoff + off + 1)
            x = cur.charFormat()
            print hex(x.foreground().color().rgb())
            print hex(x.background().color().rgb())

            if x.foreground().color().rgb() == 0xff000000 and x.background().color().rgb() == 0xff000000:
                #newfmt.setForeground(QtGui.QBrush(QtGui.QColor('#000000')))
                #newfmt.setBackground(QtGui.QBrush(QtGui.QColor('#000000')))
                newfmt = self.deffmt
            else:
                newfmt = QtGui.QTextCharFormat(x)
                newfmt.setForeground(x.background())
                newfmt.setBackground(x.foreground())

            self.setFormat(off, match.end()-off, newfmt)
            #results.append(address+off)

def cursorchange():
    c = txt.textCursor()
    c.select(c.WordUnderCursor)
    x = c.selectedText()
    if x:
        syntax.highword = str(x)
        syntax.rehighlight()

def thing():
    #fmt.setForeground(QtGui.QBrush(QtGui.QColor('#ff0000')))
    print 'THING'
    #txt.setCurrentCharFormat(fmt)
    #syntax.highword = 'THING'
    txt.insertPlainText('THING TEXT')

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()

lyt = QtGui.QVBoxLayout()

but = QtGui.QPushButton('WOOT')
window.connect(but, QtCore.SIGNAL('clicked()'), thing)

#txt = QtGui.QTextEdit(parent=window)
txt = QtGui.QPlainTextEdit(parent=window)

fmt = QtGui.QTextCharFormat()
fmt.setFont(QtGui.QFont('Courier', 14))
fmt.setForeground(QtGui.QBrush(QtGui.QColor('#ff0000')))
fmt.setBackground(QtGui.QBrush(QtGui.QColor('#000000')))

#txt.setCurrentCharFormat(fmt)
txt.moveCursor(QtGui.QTextCursor.End)
#txt.mergeCurrentCharFormat(fmt)
oldfmt = txt.currentCharFormat()


#txt.document().setDefaultStyleSheet('''
#reg {
    #background-color: #000000;
    #color: #ff0000;
#}
#
#mnem {
    
#}
#
#a {
#}
#
#''')
#
#txt.setStyleSheet(
#'''
#QWidget {
    #background-color: black;
    #color: #00ff00;
    #font-family: Courier;
    #font-size: 14pt;
#}
#'''
#)


#txt.setCurrentCharFormat(fmt)
#txt.insertPlainText('some neato text!')
#txt.setCurrentCharFormat(oldfmt)
#txt.insertPlainText('some less neato text...')

#txt.insertHtml('this is some <reg>neat</reg> txt!<br>This is some less <reg>neat</reg> text...')
c = txt.textCursor()
b = c.blockFormat()
b.setNonBreakableLines(True)
b.setIndent(200)
c.setBlockFormat(b)
c.insertBlock()
#ffmt = QtGui.QTextFrameFormat()
#c.insertFrame(ffmt)
c.insertText('Block One ', fmt)
c.insertBlock()
#c.insertFrame(ffmt)
c.insertText('Block Two!')

#txt.cursorPositionChanged.connect(cursorchange)
#txt.setMouseTracking(True)

#syntax = VQHighlight(txt)

lyt.addWidget(but)
lyt.addWidget(txt)

window.setLayout(lyt)

window.show()

# It's exec_ because exec is a reserved word in Python
app.exec_()

