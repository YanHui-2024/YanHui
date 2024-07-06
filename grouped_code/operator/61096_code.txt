>>> import torch
>>> torch.tensordot(torch.zeros(()), torch.zeros(()), 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/fobermey/opt/miniconda3/envs/pyro/lib/python3.7/site-packages/torch/functional.py", line 929, in tensordot
    raise RuntimeError(f"unsupported input to tensordot, got dims={dims}")
RuntimeError: unsupported input to tensordot, got dims=0