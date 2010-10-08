
import envi.archs.amd64 as e_amd64
import envi.archs.i386.renderer as e_i386_rend

class Amd64OpcodeRenderer(e_i386_rend.i386OpcodeRenderer):
    def __init__(self):
        e_i386_rend.i386OpcodeRenderer.__init__(self)
        self.arch = e_amd64.Amd64Module()
        self.rctx = e_amd64.Amd64RegisterContext()
