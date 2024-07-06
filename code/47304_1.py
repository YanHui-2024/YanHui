Traceback (most recent call last):
  File "error.py", line 14, in <module>
    _ = torch.autograd.grad(out, x)
  File "/home/ignacio/anaconda3/envs/torchani/lib/python3.7/site-packages/torch/autograd/__init__.py", line 204, in grad
    inputs, allow_unused)
RuntimeError: CUDA driver error: a PTX JIT compilation failed