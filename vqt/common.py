
# Some common GUI helpers

class ACT:
    def __init__(self, meth, *args, **kwargs):
        self.meth = meth
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.meth( *self.args, **self.kwargs )

