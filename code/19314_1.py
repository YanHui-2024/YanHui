tensor([[1.8719, 1.6158, 1.0286, 1.0959, 1.1366],
        [1.5421, 0.4732, 1.1207, 1.4857, 3.2413],
        [2.4948, 2.7028, 2.1719, 2.7762, 3.3651],
        [1.9806, 2.5796, 1.4602, 1.5482, 1.9668]])
Traceback (most recent call last):
  File "iter_test.py", line 13, in <module>
    @torch.jit.script
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 745, in script
    _jit_script_compile(mod, ast, _rcb, get_default_args(obj))
RuntimeError: 
Tensor cannot be used as a tuple:
@torch.jit.script
def foo(x):
    rv = x[0]
    for x_i in x:
    ~~~~~~~~~~~~~...  <--- HERE
        rv += x_i
    return rv