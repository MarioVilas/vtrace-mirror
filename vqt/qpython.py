'''
Home of some helpers for python interactive stuff.
'''
import traceback

from threading import Thread
from PyQt4 import QtCore, QtGui

from vqt.main import idlethread

@idlethread
def scripterr(msg, info):
    msgbox = QtGui.QMessageBox()
    msgbox.setText('Script Error: %s' % msg)
    msgbox.setInformativeText(info)
    msgbox.exec_()

class ScriptThread(Thread):

    def __init__(self, cobj, locals):
        Thread.__init__(self)
        self.setDaemon(True)
        self.cobj = cobj
        self.locals = locals

    def run(self):
        try:
            exec(self.cobj, self.locals)
        except Exception, e:
            scripterr(str(e), traceback.format_exc())

class VQPythonView(QtGui.QWidget):

    def __init__(self, locals=None, parent=None):
        if locals == None:
            locals = {}

        self._locals = locals

        QtGui.QWidget.__init__(self, parent=parent)

        self._textWidget = QtGui.QTextEdit(parent=self)
        self._botWidget = QtGui.QWidget(parent=self)
        self._run_button = QtGui.QPushButton('Run', parent=self._botWidget)
        self._run_button.clicked.connect(self._okClicked)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self._run_button)
        hbox.setMargin(2)
        hbox.setSpacing(4)

        self._botWidget.setLayout(hbox)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self._textWidget)
        vbox.addWidget(self._botWidget)
        vbox.setMargin(2)
        vbox.setSpacing(4)

        self.setLayout(vbox)

        self.setWindowTitle('Python Interactive')

    def _okClicked(self):
        pycode = str(self._textWidget.document().toPlainText())
        cobj = compile(pycode, "vqpython_exec.py", "exec")
        sthr = ScriptThread(cobj, self._locals)
        sthr.start()

