'''
'''
import gtk

import vwidget.main as vw_main
import vwidget.memview as vw_memview

import visgraph.layouts.dynadag as vg_dynadag
import visgraph.renderers.gtkrend as vg_rend_gtk

import vwidget.menubuilder as vw_menu

import vivisect.gui as viv_gui
import vivisect.base as viv_base
import vivisect.renderers as viv_rend
import vivisect.tools.graphutil as viv_graphutil

class VivGraphMemView(viv_gui.VivMemoryView, viv_base.VivEventCore):

    def __init__(self, vw, gui, memwin):
        viv_gui.VivMemoryView.__init__(self, vw, gui, memwin)
        viv_base.VivEventCore.__init__(self, vw)
        gui.addEventCore(self)

    def renderMemory(self, va, size, rend=None):
        self.beginva = va
        vw_memview.MemoryView.renderMemory(self, va, size, rend=rend)

    def vwGetPopup(self, textview, menu, vwfaddr=None):
        va = self.selectva
        vwmenu = vw_menu.FieldAdder(menu, splitchar='/')
        vwmenu.addField('Graph/Color Node', self.popColorGraphNode, (self.beginva,), stockid=gtk.STOCK_SELECT_COLOR)
        viv_gui.VivMemoryView.vwGetPopup(self, textview, menu, vwfaddr=vwmenu)

    def VWE_SETFUNCMETA(self, vw, event, einfo):
        fva, key, val = einfo
        if key == 'BlockColors':
            colorstr = val.get(self.beginva, '#0F0')
            color = gtk.gdk.color_parse(colorstr)
            self._hack_frame.modify_bg(gtk.STATE_NORMAL, color)

    def popColorGraphNode(self, item, cbva):
        dialog = gtk.ColorSelectionDialog("Select Color")  
        if dialog.run() == gtk.RESPONSE_OK:  
            col = dialog.colorsel.get_current_color()
            fva = self.vw.getFunction(cbva)
            cols = self.vw.getFunctionMeta(fva, 'BlockColors', default={})
            cols[self.beginva] = str(col)
            self.vw.setFunctionMeta(fva, 'BlockColors', cols)
        dialog.destroy()  

    def goto(self, va, size=None, rend=None):
        print 'GOTO 0x%.8x' % va

def addWidgets(vw, fva, graph):

    rend = viv_rend.WorkspaceRenderer(vw)

    colors = vw.getFunctionMeta(fva, 'BlockColors', default={})

    tagtable = None
    for nid,ninfo in graph.getNodes():

        if ninfo.get('ghost'):
            widget = gtk.Label()
            print 'LABEL SIZE',widget.size_request()

        else:

            memview = VivGraphMemView(vw, vw._viv_gui, None)
            if tagtable == None:
                tagtable = memview.vwGetTagTable()
                tagselect = memview.vaTagSelector

            memview.vaTagSelector = tagselect # HACK
            memview.vwSetTagTable(tagtable)

            memview.set_policy(gtk.POLICY_NEVER, gtk.POLICY_NEVER)
            memview.addRenderer('Viv', rend)
            memview.renderMemory(ninfo['cbva'],ninfo['cbsize'])

            color = gtk.gdk.color_parse(colors.get(ninfo['cbva'], '#0f0'))

            widget = gtk.Frame()
            widget.modify_bg(gtk.STATE_NORMAL, color)
            widget.set_shadow_type(gtk.SHADOW_ETCHED_OUT)

            memview._hack_frame = widget

            widget.add(memview)
            widget.show_all()

        ninfo['widget'] = widget

def destwin(widget, win):
    win.destroy()

@vw_main.idlethread
def makeFuncGraphWindow(vw, fva):

    graph = viv_graphutil.buildFunctionGraph(vw, fva, revloop=True)
    addWidgets(vw, fva, graph)

    rend = vg_rend_gtk.GtkVisGraphRenderer(graph)

    layout = vg_dynadag.DynadagLayout(graph)
    layout.renderGraph(rend)

    s = gtk.ScrolledWindow()
    s.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    s.add(rend)

    oview = vg_rend_gtk.GtkVisGraphOverview(graph, layout, scrollwin=s)
    w1 = gtk.Window()
    w1.set_title('Overview')
    w1.add(oview)
    w1.show_all()
    w1.resize(100,100)
    oview.connect('destroy', destwin, w1)

    w = gtk.Window()
    w.set_title('Function Graph: 0x%.8x (%s)' % (fva, vw.getName(fva)))

    w.add(s)
    w.show_all()

    w.resize(800, 800)


    #def button_press_event(self, widget, item, event):
        #print event.x
        #print event.y
        #print event.button

    #w.connect('button_press_event', button_press_event)

