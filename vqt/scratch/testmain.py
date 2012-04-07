# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testmain.ui'
#
# Created: Mon Oct 11 22:25:44 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 431, 361))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuBlah = QtGui.QMenu(self.menubar)
        self.menuBlah.setObjectName(_fromUtf8("menuBlah"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFoo = QtGui.QAction(MainWindow)
        self.actionFoo.setObjectName(_fromUtf8("actionFoo"))
        self.menuBlah.addAction(self.actionFoo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuBlah.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBlah.setTitle(QtGui.QApplication.translate("MainWindow", "blah", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFoo.setText(QtGui.QApplication.translate("MainWindow", "foo", None, QtGui.QApplication.UnicodeUTF8))

