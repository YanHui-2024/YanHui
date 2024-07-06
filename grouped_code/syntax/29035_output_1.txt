Traceback (most recent call last):
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/_utils_internal.py", line 46, in get_source_lines_and_file
    sourcelines, file_lineno = inspect.getsourcelines(obj)
  File "/opt/anaconda/envs/test/lib/python3.7/inspect.py", line 955, in getsourcelines
    lines, lnum = findsource(object)
  File "/opt/anaconda/envs/test/lib/python3.7/inspect.py", line 786, in findsource
    raise OSError('could not get source code')
OSError: could not get source code

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c.py", line 10, in <module>
    torch.jit.script(M())
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/__init__.py", line 1203, in script
    return torch.jit.torch.jit._recursive.recursive_script(obj)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/_recursive.py", line 173, in recursive_script
    return copy_to_script_module(mod, overload_stubs + stubs)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/_recursive.py", line 95, in copy_to_script_module
    torch.jit._create_methods_from_stubs(script_module, stubs)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/__init__.py", line 1423, in _create_methods_from_stubs
    self._c._create_methods(self, defs, rcbs, defaults)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/__init__.py", line 1075, in _compile_and_register_class
    ast = get_jit_class_def(obj, obj.__name__)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/frontend.py", line 148, in get_jit_class_def
    self_name=self_name) for method in methods]
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/frontend.py", line 148, in <listcomp>
    self_name=self_name) for method in methods]
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/frontend.py", line 160, in get_jit_def
    sourcelines, file_lineno, filename = get_source_lines_and_file(fn)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/_utils_internal.py", line 50, in get_source_lines_and_file
    "Make sure original .py files are available. Original error: {}").format(filename, e))
OSError: Can't get source for None. TorchScript requires source access in order to carry out compilation. Make sure original .py files are available. Original error: could not get source code