"""
A module for GUI management of cobra.cluster clients
calling into a server.
"""

import gtk

import cobra
import cobra.cluster as c_cluster

import vwidget.main as vw_main
import vwidget.util as vw_util
import vwidget.views as vw_views

class ClusterServerView(vw_views.VTreeView,
                        c_cluster.ClusterCallback):
    """
    A cluster server status GUI.
    """
    __cols__ = (
        ("Id", 0, int),
        ("Client",1,str),
        ("Status",2,str),
        ("Percent",3,int)
    )

    def __init__(self, layout=None):
        vw_views.VTreeView.__init__(self, layout=layout)
        # Hook all the GUI callbacks in the server.
        #FIXME make this a callback object in the server
        self.id_iter = {}
        # Setup a progress bar renderer
        self.treeview.remove_column(self.treeview.get_column(3))
        col = vw_util.makeColumn("Percent", 3, cell=gtk.CellRendererProgress(), links={"value":3})
        self.treeview.append_column(col)

    # Mirror the server interfaces so it's easy to keep things straight
    def workGotten(self, server, work):
        vw_main.guilock.acquire()
        try:
            ip,port = cobra.getCallerInfo()
            #FIXME reverse lookup?
            iter = self.model.append((work.id, ip, "Starting", 0))
            self.id_iter[work.id] = iter
        finally:
            vw_main.guilock.release()

    def workDone(self, server, work):
        vw_main.guilock.acquire()
        try:
            iter = self.id_iter.pop(work.id, None)
            if iter != None:
                self.vwRemove(iter)
        finally:
            vw_main.guilock.release()

    def workTimeout(self, server, work):
        self.workDone(server, work)

    def workCanceled(self, server, work):
        self.workDone(server, work)

    def workFailed(self, server, work):
        self.workDone(server, work)

    def workStatus(self, server, workid, status):
        vw_main.guilock.acquire()
        try:
            iter = self.id_iter.get(workid)
            self.model.set_value(iter, 2, status)
        finally:
            vw_main.guilock.release()

    def workCompletion(self, server, workid, percent):
        vw_main.guilock.acquire()
        try:
            iter = self.id_iter.get(workid)
            self.model.set_value(iter, 3, percent)
        finally:
            vw_main.guilock.release()

