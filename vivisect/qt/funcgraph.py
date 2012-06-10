import envi.qt.memory as e_mem_qt
import envi.memcanvas as e_memcanvas
import envi.qt.memcanvas as e_qt_memcanvas

import visgraph.layouts.dynadag as vg_dynadag

import vivisect.base as viv_base
import vivisect.renderers as viv_rend
import vivisect.tools.graphutil as viv_graphutil
#import envi.qt.memory as e_mem_qt
#import envi.qt.memcanvas as e_mem_canvas

#import vstruct.qt as vs_qt

#import vqt.menubuilder as vqt_menu

#import vivisect.base as viv_base
#import vivisect.renderers as viv_rend
#
from PyQt4          import QtCore, QtGui, QtWebKit
from vqt.main       import idlethread, idlethreadsync, eatevents
#from envi.threads  import firethread
from vivisect.const import *

class VQVivFuncgraphCanvas(e_qt_memcanvas.VQMemoryCanvas):

    def __init__(self, *args, **kwargs):
        e_qt_memcanvas.VQMemoryCanvas.__init__(self, *args, **kwargs)
        self.vw = self.mem

    def renderMemory(self, va, size, rend=None):
        # For the funcgraph canvas, this will be called once per code block

        # Check if we have a codeblock element already...
        frame = self.page().mainFrame()
        canvelem = frame.findFirstElement('#memcanvas')

        elem = frame.findFirstElement('#codeblock_%.8x' % va)
        if elem.isNull():
            # Lets add a codeblock element for this
            canvelem.appendInside('<div class="codeblock" id="codeblock_%.8x"></div>' % va)

        self._canv_rendtagid = '#codeblock_%.8x' % va

        ret = e_memcanvas.MemoryCanvas.renderMemory(self, va, size, rend=rend)

        self._canv_rendtagid = '#memcanvas'

        return ret

    def _applyColorMap(self, cmap):

        frame = self.page().mainFrame()
        style = frame.findFirstElement('#cmapstyle')

        rows = []
        for va,color in cmap.items():
            rows.append('.va_0x%.8x { color: #000000; background-color: %s }' % (va, color))

        style.setInnerXml('\n'.join(rows))

funcgraph_js = '''
svgns = "http://www.w3.org/2000/svg";

function createSvgElement(ename, attrs) {
    var elem = document.createElementNS(svgns, ename);
    for (var aname in attrs) {
        elem.setAttribute(aname, attrs[aname]);
    }
    return elem
}

function svgwoot(parentid, svgid, width, height) {

    var elem = document.getElementById(parentid);

    var svgelem = createSvgElement("svg", { "height":height.toString(), "width":width.toString() })
    svgelem.setAttribute("id", svgid);

    elem.appendChild(svgelem);
}

function addSvgForeignObject(svgid, foid, width, height) {
    var foattrs = {
        "class":"node",
        "id":foid,
        "width":width,
        "height":height
    };

    var foelem = createSvgElement("foreignObject", foattrs);

    var svgelem = document.getElementById(svgid);
    svgelem.appendChild(foelem);
}

function addSvgForeignHtmlElement(foid, htmlid) {

    var foelem = document.getElementById(foid);
    var htmlelem = document.getElementById(htmlid);
    htmlelem.parentNode.removeChild(htmlelem);

    //foelem.appendChild(htmlid);

    var newbody = document.createElement("body");
    newbody.setAttribute("xmlns", "http://www.w3.org/1999/xhtml");
    //newbody.appendChild( htmlelem.cloneNode(true) );
    newbody.appendChild( htmlelem );

    foelem.appendChild(newbody);
}

function moveSvgElement(elemid, xpos, ypos) {
    var elem = document.getElementById(elemid);
    elem.setAttribute("x", xpos);
    elem.setAttribute("y", ypos);
}

function plineover(pline) {
    pline.setAttribute("style", "fill:none;stroke:yellow;stroke-width:2")
}

function plineout(pline) {
    pline.setAttribute("style", "fill:none;stroke:green;stroke-width:2")
}


function drawSvgLine(svgid, lineid, points) {
    var plineattrs = {
        "id":lineid,
        "points":points,
        "style":"fill:none;stroke:green;stroke-width:2",
        "onmouseover":"plineover(this)",
        "onmouseout":"plineout(this)"
    };

    var lelem = createSvgElement("polyline", plineattrs);
    var svgelem = document.getElementById(svgid);

    //var rule = "polyline." + lineclass + ":hover { stroke: red; }";
    //document.styleSheets[0].insertRule(rule, 0);

    svgelem.appendChild(lelem);
}
'''

class VQVivFuncgraphView(QtGui.QWidget, viv_base.VivEventCore):

    def __init__(self, vw, vwqgui):
        self.vw = vw
        self.fva = None
        self.vwqgui = vwqgui

        QtGui.QWidget.__init__(self, parent=vwqgui)
        viv_base.VivEventCore.__init__(self, vw)

        self.top_box = QtGui.QWidget(parent=self)
        hbox = QtGui.QHBoxLayout(self.top_box)
        hbox.setMargin(2)
        hbox.setSpacing(4)

        self.addr_entry  = QtGui.QLineEdit(parent=self.top_box)

        self.mem_canvas = VQVivFuncgraphCanvas(vw, syms=vw, parent=self)
        self.mem_canvas.setNavCallback(self._navGotoExpr)

        self.loadDefaultRenderers()

        self.addr_entry.returnPressed.connect(self._renderMemory)

        button_save = QtGui.QPushButton('Save', self)
        button_save.clicked.connect( self._buttonSaveAs )

        hbox.addWidget(self.addr_entry)
        hbox.addWidget(button_save)

        vbox = QtGui.QVBoxLayout(self)
        vbox.setMargin(4)
        vbox.setSpacing(4)
        vbox.addWidget(self.top_box)
        vbox.addWidget(self.mem_canvas, stretch=100)

        self.top_box.setLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle('FuncGraph: None')

        # Do these last so we are all setup...
        vwqgui.addEventCore(self)
        vwqgui.vivNavSignal.connect( self.vivMemNavSlot )
        vwqgui.vivMemColorSignal.connect( self.mem_canvas._applyColorMap )

    def _buttonSaveAs(self):
        frame = self.mem_canvas.page().mainFrame()
        elem = frame.findFirstElement('#mainhtml')
        h = elem.toOuterXml()
        #h = frame.toHtml()
        file('test.html','wb').write(str(h))

    def renderFunctionGraph(self, fva):

        self.fva = fva
        graph = viv_graphutil.buildFunctionGraph(self.vw, fva, revloop=True)

        # Go through each of the nodes and render them so we know sizes
        for nid, ninfo in graph.getNodes():
            cbva = ninfo.get('cbva')
            cbsize = ninfo.get('cbsize')
            self.mem_canvas.renderMemory(cbva, cbsize)

        # Let the renders complete...
        eatevents()

        frame = self.mem_canvas.page().mainFrame()
        frame.evaluateJavaScript(funcgraph_js)

        for nid, ninfo in graph.getNodes():
            cbva = ninfo.get('cbva')

            cbname = 'codeblock_%.8x' % cbva
            girth, ok = frame.evaluateJavaScript('document.getElementById("%s").offsetWidth;' % cbname).toInt()
            height, ok = frame.evaluateJavaScript('document.getElementById("%s").offsetHeight;' % cbname).toInt()
            graph.setNodeInfo(nid, "size", (girth, height))

        layout = vg_dynadag.DynadagLayout(graph)
        layout.layoutGraph()

        width, height = layout.getLayoutSize()

        svgid = 'funcgraph_%.8x' % fva
        frame.evaluateJavaScript('svgwoot("vbody", "%s", %d, %d);' % (svgid, width+10, height))

        for nid, ninfo in graph.getNodes():

            cbva = ninfo.get('cbva')
            if cbva == None:
                continue

            xpos, ypos = ninfo.get('position')
            girth, height = ninfo.get('size')

            foid = 'fo_cb_%.8x' % cbva
            cbid = 'codeblock_%.8x' % cbva

            frame.evaluateJavaScript('addSvgForeignObject("%s", "%s", %d, %d);' % (svgid, foid, girth+8, height))
            frame.evaluateJavaScript('addSvgForeignHtmlElement("%s", "%s");' % (foid, cbid))
            frame.evaluateJavaScript('moveSvgElement("%s", %d, %d);' % (foid, xpos, ypos))

        # Draw in some edge lines!
        for eid, n1, n2, einfo in graph.getEdges():
            points = einfo.get('edge_points')
            pointstr = ' '.join(['%d,%d' % (x,y) for (x,y) in points ])

            frame.evaluateJavaScript('drawSvgLine("%s", "edge_%.8x", "%s");' % (svgid, eid, pointstr))

    def closeEvent(self, event):
        # FIXME this doesn't actually do anything...
        print 'CLOSE AND REMOVE'
        self.parentWidget().delEventCore(self)
        return e_mem_qt.VQMemoryWindow.closeEvent(self, event)

    def _navGotoExpr(self, expr):
        parent = self.parentWidget()
        if parent.isFloating():
            self.addr_entry.setText(expr)
            self._renderMemory()
            return
        self.vwqgui.vivNavSignal.emit(expr)

    def vivMemNavSlot(self, expr, sizeexpr=None):
        parent = self.parentWidget()
        if parent.isFloating():
            return
        if parent.vqIsVisible():
            self.addr_entry.setText(expr)
            self._renderMemory()

    @idlethread
    def _renderMemory(self):

        expr = str(self.addr_entry.text())
        if not expr:
            return

        try:
            addr = self.vw.parseExpression(expr)
        except Exception, e:
            self.mem_canvas.addText('Invalid Address: %s (%s)' % (expr, e))
            return

        fva = self.vw.getFunction(addr)
        if fva == self.fva:
            self.mem_canvas.page().mainFrame().scrollToAnchor('viv:0x%.8x' % addr)
            return

        self.clearText()
        self.renderFunctionGraph(fva)
        self.setWindowTitle('FuncGraph: %s' % expr)

    def loadDefaultRenderers(self):
        vivrend = viv_rend.WorkspaceRenderer(self.vw)
        self.mem_canvas.addRenderer('Viv', vivrend)
        self.mem_canvas.setRenderer('Viv')

    def clearText(self):
        # Pop the svg and reset #memcanvas
        frame = self.mem_canvas.page().mainFrame()
        if self.fva:
            svgid = '#funcgraph_%.8x' % self.fva
            svgelem = frame.findFirstElement(svgid)
            svgelem.removeFromDocument()

        memelem = frame.findFirstElement('#memcanvas')
        memelem.setInnerXml(' ')

#@idlethread
#def showFunctionGraph(fva, vw, vwqgui):
    #view = VQVivFuncgraphView(fva, vw, vwqgui)
    #view.show()

