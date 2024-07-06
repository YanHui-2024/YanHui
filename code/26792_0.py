Traceback (most recent call last):
  File "bug.py", line 15, in <module>
    torch.jit.script(bug)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/__init__.py", line 1162, in script
    return _convert_to_script_module(obj)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/__init__.py", line 1812, in _convert_to_script_module
    return WeakScriptModuleProxy(mod, stubs)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/__init__.py", line 1386, in init_then_register
    original_init(self, *args, **kwargs)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/__init__.py", line 1736, in __init__
    _create_methods_from_stubs(self, stubs)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/__init__.py", line 1347, in _create_methods_from_stubs
    self._c._create_methods(self, defs, rcbs, defaults)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/__init__.py", line 1058, in _compile_and_register_class
    ast = get_jit_class_def(obj, obj.__name__)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/frontend.py", line 143, in get_jit_class_def
    self_name=self_name) for method in methods]
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/frontend.py", line 143, in <listcomp>
    self_name=self_name) for method in methods]
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/frontend.py", line 166, in get_jit_def
    return build_def(ctx, py_ast.body[0], type_line, self_name)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/frontend.py", line 195, in build_def
    param_list = build_param_list(ctx, py_def.args, self_name)
  File "/home/d00413986/.local/share/virtualenvs/Code-ekJV9_xh/lib/python3.6/site-packages/torch/jit/frontend.py", line 215, in build_param_list
    raise ValueError(_vararg_kwarg_err)
ValueError: Compiled functions can't take variable number of arguments or use keyword-only arguments with defaults