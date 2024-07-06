import torch

class A(torch.nn.Module):
    @torch.jit.export
    def test(self):
        s= {"hello": None}
        return {**s}
        
torch.jit.script(A())
