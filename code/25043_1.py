Traceback (most recent call last):
  File "ought.py", line 9, in <module>
    torch.jit.script(Foo())
  File "/home/jamesreed/pytorch/torch/jit/__init__.py", line 1159, in script
    return torch.jit.torch.jit._recursive.recursive_script(obj)
  File "/home/jamesreed/pytorch/torch/jit/_recursive.py", line 166, in recursive_script
    stubs = list(map(make_stub, filtered_methods))
  File "/home/jamesreed/pytorch/torch/jit/_recursive.py", line 163, in make_stub
    return torch.jit.script_method(func, _jit_internal.createResolutionCallbackFromClosure(func))
  File "/home/jamesreed/pytorch/torch/jit/__init__.py", line 1224, in script_method
    ast = get_jit_def(fn, self_name="ScriptModule")
  File "/home/jamesreed/pytorch/torch/jit/frontend.py", line 164, in get_jit_def
    py_ast = ast.parse(dedent_src)
  File "/home/jamesreed/miniconda3/lib/python3.6/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    def forward(self, x):
    ^
IndentationError: unexpected indent