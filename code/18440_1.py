Traceback (most recent call last):
  File "param.py", line 3, in <module>
    @torch.jit.script
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 739, in script
    _jit_script_compile(mod, ast, _rcb, get_default_args(obj))
RuntimeError:
range() expects 1 argument but got 2:
@torch.jit.script
def foo(x):
    for i in range(1, 10):
    ~~~~~~~~~~~~~~~~~~~~~~...  <--- HERE
        x += float(i)
    return x