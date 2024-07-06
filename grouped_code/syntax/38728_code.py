class X(object):
    def __init__(self):
        pass

@torch.jit.script
def foo():
    return X()
    pass