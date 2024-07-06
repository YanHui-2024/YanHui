RuntimeError: 

aten::grad(Tensor[] outputs, Tensor[] inputs, Tensor?[]? grad_outputs=None, bool? keep_graph=None, bool create_graph=False, bool allow_unused=False) -> (Tensor[]):
Keyword argument retain_graph unknown.
:
at test.py:5:11
@torch.jit.script
def f(x):
    return torch.autograd.grad([x.sum()], [x], retain_graph=True)
           ~~~~~~~~~~~~~~~~~~~ <--- HERE