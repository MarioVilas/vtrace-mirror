
from PyQt4 import QtCore, QtGui, QtWebKit

#import vtrace

#import envi.cli as e_cli

#import vqwidget.cli as vq_cli
import vqwidget.main as vq_main
#import vqwidget.vqvtrace as vq_vtrace

vq_main.startup()

#trace = vtrace.getTrace()
#pid = vq_vtrace.getProcessPid()
#if pid != None:
     #trace.attach(pid)

#ecli = e_cli.EnviMutableCli(trace, symobj=trace)

#win = vq_cli.VQCli(ecli)

win = QtWebKit.QWebView()
#win.setHtml('<HTML>oh hai!</html>')
win.load(QtCore.QUrl('http://www.google.com'))
win.setZoomFactor(1)
win.show()

vq_main.main()

