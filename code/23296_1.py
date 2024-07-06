Traceback (most recent call last):
  File "/private/home/suo/scratch/test.py", line 176, in <module>
    ScriptRoot = torch.jit.script(Root)
  File "/scratch/suo/pytorch/torch/jit/__init__.py", line 1065, in script
    _compile_and_register_class(obj, _rcb, qualified_name)
  File "/scratch/suo/pytorch/torch/jit/__init__.py", line 1045, in _compile_and_register_class
    ast = get_jit_class_def(obj, obj.__name__)
  File "/scratch/suo/pytorch/torch/jit/frontend.py", line 143, in get_jit_class_def
    self_name=self_name) for method in methods]
  File "/scratch/suo/pytorch/torch/jit/frontend.py", line 143, in <listcomp>
    self_name=self_name) for method in methods]
  File "/scratch/suo/pytorch/torch/jit/frontend.py", line 166, in get_jit_def
    return build_def(ctx, py_ast.body[0], type_line, self_name)
  File "/scratch/suo/pytorch/torch/jit/frontend.py", line 195, in build_def
    param_list = build_param_list(ctx, py_def.args, self_name)
  File "/scratch/suo/pytorch/torch/jit/frontend.py", line 215, in build_param_list
    raise ValueError(_vararg_kwarg_err)
ValueError: Compiled functions can't take variable number of arguments or use keyword-only arguments with defaults