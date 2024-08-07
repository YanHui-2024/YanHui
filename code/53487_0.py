In [1]: import torch

In [2]: x, y = torch.randn(3, 4), torch.randn(4, 3)

In [3]: torch.tensordot(x, y, dims=((1,), (0,)))
Out[3]: 
tensor([[-0.2011,  0.1324,  0.7855],
        [ 0.4894, -2.1793, -0.4989],
        [ 2.4699,  0.4472, -0.5411]])

In [5]: @torch.jit.script
   ...: def f(x, y):
   ...:     return torch.tensordot(x, y, dims=((1,), (0,)))
   ...: 
---------------------------------------------------------------------------
RuntimeError: 
Arguments for call are not valid.
The following variants are available:
  
  aten::tensordot(Tensor self, Tensor other, int[] dims_self, int[] dims_other) -> (Tensor):
  Argument dims_self not provided.
  
  aten::tensordot.out(Tensor self, Tensor other, int[] dims_self, int[] dims_other, *, Tensor(a!) out) -> (Tensor(a!)):
  Argument dims_self not provided.

The original call is:
  File "<ipython-input-5-61613126bcad>", line 3
@torch.jit.script
def f(x, y):
    return torch.tensordot(x, y, dims=((1,), (0,)))
           ~~~~~~~~~~~~~~~ <--- HERE


In [6]: @torch.jit.script
   ...: def f(x, y):
   ...:     return torch.tensordot(x, y, dims_self=[1], dims_other=[0])

In [7]: torch.tensordot(x, y, dims_self=[1], dims_other=[0])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-be1bfc130a4a> in <module>
----> 1 torch.tensordot(x, y, dims_self=[1], dims_other=[0])

TypeError: tensordot() got an unexpected keyword argument 'dims_self'