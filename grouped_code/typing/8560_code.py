import torch
@torch.jit.script
def func1(x, y):
    return x + y.type_as(x)
x = torch.tensor(0.1)
y = torch.tensor(1)
func1(x, y)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-7-36d19baf43bf> in <module>()
      5 x = torch.tensor(0.1)
      6 y = torch.tensor(1)
----> 7 func1(x, y)

RuntimeError: torch/csrc/jit/fusion_compiler.cpp:450: operator(): Assertion `nDim <= uncompressedDim` failed.