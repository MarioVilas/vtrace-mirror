
import envi.memcanvas.renderers.intel as e_rend_intel

def vdbExtension(vdb, trace):
    vdb.config.set("Aliases","db","mem -F bytes")
    vdb.config.set("Aliases","dw","mem -F u_int_16")
    vdb.config.set("Aliases","dd","mem -F u_int_32")
    vdb.config.set("Aliases","dq","mem -F u_int_64")
    vdb.canvas.addRenderer("i386", e_rend_intel.IntelOpcodeRenderer())

