import torch
import torch.nn as nn

        
@torch.jit.interface
class OperatorIf(nn.Module):
    def forward(self, inp: torch.Tensor) -> torch.Tensor:
        pass


class Operator(nn.Module):
    def __init__(self, a):
        super().__init__()
        self.a = a
        
    def forward(self, inp: torch.Tensor) -> torch.Tensor:
        return self.a * (inp + self.a)
        

class Inner(nn.Module):
    op: OperatorIf
    def __init__(self, op):
        super().__init__()
        self.op = op
        
    def forward(self, inp):
        return self.op(inp)


class Outer(nn.Module):
    def __init__(self):
        super().__init__()
        self.inner_a = Inner(Operator(1))
        self.inner_b = Inner(Operator(3.0))


if __name__ == "__main__":
    s = torch.jit.script(Outer())
    torch.jit.save(s, "/tmp/s.pt")