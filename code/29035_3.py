Traceback (most recent call last):
  File "b.py", line 10, in <module>
    torch.jit.script(M())
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/__init__.py", line 1203, in script
    return torch.jit.torch.jit._recursive.recursive_script(obj)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/_recursive.py", line 173, in recursive_script
    return copy_to_script_module(mod, overload_stubs + stubs)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/_recursive.py", line 95, in copy_to_script_module
    torch.jit._create_methods_from_stubs(script_module, stubs)
  File "/opt/anaconda/envs/test/lib/python3.7/site-packages/torch/jit/__init__.py", line 1423, in _create_methods_from_stubs
    self._c._create_methods(self, defs, rcbs, defaults)
RuntimeError: 
Unknown type name 'a.Type':
at b.py:7:25
    def forward(self) -> a.Type:
                         ~~~~~~ <--- HERE
        return a.Type(1)