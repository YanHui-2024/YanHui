Traceback (most recent call last):
  File "method_casts.py", line 3, in <module>
    @torch.jit.script
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 351, in script
    graph = _jit_script_compile(ast, rcb)
RuntimeError: 
unknown builtin op:
@torch.jit.script
def cast_to_int(x):
    return x.int()
           ~~~~~ <--- HERE

