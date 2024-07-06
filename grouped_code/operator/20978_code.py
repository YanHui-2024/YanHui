import torch
from torch.nn import LayerNorm
from torch.jit import ScriptModule


class Test(ScriptModule):
    def __init__(self, dim):
        super().__init__()
        self.layer_norm = LayerNorm(dim)


if __name__ == '__main__':
    m = Test(100)
    print(m)