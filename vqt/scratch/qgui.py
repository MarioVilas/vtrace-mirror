
from PyQt4 import QtCore, QtGui

import vdb
import vtrace

import vqwidget.cli as vq_cli
import vqwidget.main as vq_main
import vqwidget.vqenvi as vq_envi
import vqwidget.memory as vq_memory
import vqwidget.vqpython as vq_python
import vqwidget.vqvtrace as vq_vtrace
import vqwidget.menubuilder as vq_menu

class VQSavableWidget:

    def vqSaveState(self):
        pass

    def vqRestoreState(self):
        pass

class VdbMemoryWindow(vq_memory.VQMemoryWindow, vtrace.Notifier):

    def __init__(self, db, parent=None):
        t = vdb.VdbTrace(db)
        vq_memory.VQMemoryWindow.__init__(self, t, syms=t, parent=parent)
        vtrace.Notifier.__init__(self)
        self._db = db
        self._db.registerNotifier(vtrace.NOTIFY_ALL, self)
        for rname in db.canvas.getRendererNames():
            self.mem_canvas.addRenderer(rname, db.canvas.getRenderer(rname))

        self.loadRendSelect()

        if not t.isAttached():
            self.setEnabled(False)
        elif t.isRunning():
            self.setEnabled(False)
        else:
            self._renderMemory()

    @vq_main.idlethreadsync
    def notify(self, event, trace):
        if event in [vtrace.NOTIFY_CONTINUE, vtrace.NOTIFY_DETACH, vtrace.NOTIFY_EXIT]:
            self.setEnabled(False)

        else:
            # If the trace is just going to run again, skip the update.
            if not trace.shouldRunAgain():
                self.setEnabled(True)
                self._renderMemory()

class VQDockWidget(QtGui.QDockWidget):

    def __init__(self, parent):
        QtGui.QDockWidget.__init__(self, parent)

    def vqSaveState(self):
        wid = self.widget()
        ret = None
        if isinstance(wid, VQSavableWidget):
            ret = wid.vqSaveState()
            return wid.vqSaveState()

    def setWidget(self, widget):
        # If he sets his window title, we want to...
        self.setWindowTitle(widget.windowTitle())
        widget.setWindowTitle = self.setWindowTitle
        QtGui.QDockWidget.setWidget(self, widget)

    def vqRestoreState(self):
        pass

    def closeEvent(self, event):
        self.parentWidget().vqRemoveDockWidget(self)
        return QtGui.QDockWidget.closeEvent(self, event)

class VdbWindow(QtGui.QMainWindow, vtrace.Notifier):

    def __init__(self, db):
        QtGui.QMainWindow.__init__(self)
        vtrace.Notifier.__init__(self)
        self._db = db
        self._db_t = vdb.VdbTrace(db)
        self._db.registerNotifier(vtrace.NOTIFY_ALL, self)


        self._q_settings = QtCore.QSettings('invisigoth', application='vdb', parent=self)
        self._dock_widgets = []
        self._dock_classes = {}

        self.addDockWidgetClass(VdbMemoryWindow, args=(db, self))
        self.addDockWidgetClass(vq_vtrace.VQMemoryMapView, args=(self._db_t, self))
        self.addDockWidgetClass(vq_vtrace.VQFileDescView, args=(self._db_t, self))
        self.addDockWidgetClass(vq_python.VQPythonView, args=(self._db.getExpressionLocals(),))

        geom = self._q_settings.value('Vdb/Geometry')
        if not geom.isNull():
            self.restoreGeometry(geom.toByteArray())

        if not self.restoreDockWidgets():
            print 'FAIL'

        self.setStyleSheet('''

/*
QWidget {
    background: #000000;
    color: #00ff00;
    font: 12pt courier;
}
*/

QLineEdit {
    border-color: green black black green
}

QPushButton:hover {
    background: purple;
    color: red;
}
''')

        self._vq_cli = vq_cli.VQCli(db)

        tbar = vq_vtrace.VQTraceToolBar(self._db_t, parent=self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, tbar)

        mbar = vq_menu.VQMenuBar()
        self.setMenuBar(mbar)

        mbar.addField('&File.&Quit', self.menuFileQuit)
        mbar.addField('&View.&Memory', self.menuViewMemory)
        mbar.addField('&View.&Memory Maps', self.menuViewMemMaps)
        mbar.addField('&View.&File Descriptors', self.menuViewFileDesc)
        mbar.addField('&View.&Layouts.&Load', self.menuViewLayoutsLoad)
        mbar.addField('&View.&Layouts.&Save', self.menuViewLayoutsSave)
        mbar.addField('&Tools.&Python', self.menuToolsPython)

        # AnimatedDocks, AllowNestedDocks, AllowTabbedDocks, ForceTabbedDocks, VerticalTabs
        self.setDockOptions(self.AnimatedDocks | self.AllowTabbedDocks)

        self.setCentralWidget(self._vq_cli)

    def addDockWidgetClass(self, cls, args=()):
        self._dock_classes[cls.__name__] = (cls,args)

    def buildDockWidgetInstance(self, clsname):
        res = self._dock_classes.get(clsname)
        if res == None:
            print 'buildDockWidgetInstance Failed For: %s' % clsname
            return
        cls, args = res
        obj = cls(*args)
        return self.vqDockWidget(obj, QtCore.Qt.TopDockWidgetArea, floating=True)

    def restoreDockWidgets(self):
        dwcls = self._q_settings.value('Vdb/DockClasses')
        if dwcls.isNull():
            return False

        for i,clsname in enumerate(dwcls.toStringList()):
            d = self.buildDockWidgetInstance(str(clsname))
            if d != None:
                d.setObjectName('VQDockWidget%d' % i)

        state = self._q_settings.value('Vdb/State')
        self.restoreState(state.toByteArray())
        return True

    def closeEvent(self, event):
        print 'closed!'
        dock_classes = []

        for i in xrange(len(self._dock_widgets)):
            w = self._dock_widgets[i]
            print 'CLASSNAME',w.widget().__class__.__name__
            #FIXME If register'd class....
            dock_classes.append(w.widget().__class__.__name__)
            name = 'VQDockWidget%d' % i
            w.setObjectName(name)
            s = w.vqSaveState()
            self._q_settings.setValue('Vdb/%s' % name, s)

        self._q_settings.setValue('Vdb/DockClasses', dock_classes)
        self._q_settings.setValue('Vdb/Geometry', self.saveGeometry())
        self._q_settings.setValue('Vdb/State', self.saveState())

        QtGui.QMainWindow.closeEvent(self, event)

    def menuToolsPython(self):
        self.buildDockWidgetInstance('VQPythonView')

    def menuViewFileDesc(self):
        self.buildDockWidgetInstance('VQFileDescView')

    def menuViewMemMaps(self):
        self.buildDockWidgetInstance('VQMemoryMapView')

    def menuViewMemory(self):
        self.buildDockWidgetInstance('VdbMemoryWindow')

    def menuViewLayoutsLoad(self):
        # FIXME file selector!
        state = file('winstate.bin','rb').read()
        print 'STATE: %s' % str(state).encode('hex')
        self.restoreState(state)

    def menuViewLayoutsSave(self):
        state = self.saveState()
        print 'STATE: %s' % str(state).encode('hex')
        file('winstate.bin','wb').write(state)

    def menuFileQuit(self, *args, **kwargs):
        print 'woot',args,kwargs

    def vqRemoveDockWidget(self, widget):
        self._dock_widgets.remove(widget)

    def vqDockWidget(self, widget, pos, floating=False):
        d = VQDockWidget(self)
        # We could enforce things...
        d.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        d.setWidget(widget)
        self.addDockWidget(pos, d)
        if floating:
            d.setFloating(True)
        self._dock_widgets.append(d)
        d.show()
        return d

    def notify(self, event, trace):
        pass

    #@vq_main.idlethreadsync
    #def notify(self, event, trace):

        #if event in [vtrace.NOTIFY_CONTINUE, vtrace.NOTIFY_DETACH, vtrace.NOTIFY_EXIT]:
            #self.setTraceWindowsActive(False)

        #else:
            # If the trace is just going to run again, skip the update.
            #if not trace.shouldRunAgain():
                #self.setTraceWindowsActive(True)

vq_main.startup()

db = vdb.Vdb()
w = VdbWindow(db)

t = vdb.VdbTrace(db)

w.show()
vq_main.main()

