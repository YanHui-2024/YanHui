torch.jit.frontend.NotSupportedError: ellipsis is not supported:
  File "/home/conda/jit.py", line 3
def foo(x: torch.Tensor) -> int:
    return x[-3]
           ~ <--- HERE