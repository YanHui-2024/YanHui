RuntimeError: The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
  File "<ipython-input-11-c4a594a6d126>", line 3, in f
@torch.jit.script
def f(x):  # ? x 6
    return x.t()[[0, 1, 5]]  # 3 x ?
           ~~~~~~~~~~~~~~ <--- HERE
RuntimeError: select() cannot be applied to a 0-dim tensor.