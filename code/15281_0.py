Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.7/dist-packages/torch/__init__.py", line 263, in <module>
    from .functional import *
  File "/usr/local/lib/python3.7/dist-packages/torch/functional.py", line 2, in <module>
    import torch.nn.functional as F
  File "/usr/local/lib/python3.7/dist-packages/torch/nn/__init__.py", line 1, in <module>
    from .modules import *
  File "/usr/local/lib/python3.7/dist-packages/torch/nn/modules/__init__.py", line 2, in <module>
    from .linear import Linear, Bilinear
  File "/usr/local/lib/python3.7/dist-packages/torch/nn/modules/linear.py", line 5, in <module>
    from .. import functional as F
  File "/usr/local/lib/python3.7/dist-packages/torch/nn/functional.py", line 369, in <module>
    if_false=_fractional_max_pool2d)
  File "/usr/local/lib/python3.7/dist-packages/torch/_jit_internal.py", line 141, in boolean_dispatch
    raise RuntimeError("only one function can have a docstring")
RuntimeError: only one function can have a docstring