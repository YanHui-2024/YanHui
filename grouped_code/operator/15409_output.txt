Traceback (most recent call last):
  File "fail.py", line 4, in <module>
    @torch.jit.script
  File "/home/apaszke/pytorch/torch/jit/__init__.py", line 693, in script
    _jit_script_compile(mod, ast, _rcb, get_default_args(fn))
  File "/home/apaszke/pytorch/torch/jit/annotations.py", line 67, in get_num_params
    raise RuntimeError("expected a single top-level function")
RuntimeError: expected a single top-level function