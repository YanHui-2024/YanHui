import torch

def pass_through(a: int, b: int):
    return (a, b)

class JitClass:
    def __init__(self, a: int, b: int):
        self.a, self.b = pass_through(a, b)

    def get(self):
        return self.a + self.b

@torch.jit.script
def fn(a: int, b: int):
    o = JitClass(a, b)
    return o.get()