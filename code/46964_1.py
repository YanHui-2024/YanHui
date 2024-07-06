Traceback (most recent call last):
  File "/a.py", line 24, in <module>
    b = torch.jit.script(b)
  File "/usr/local/lib/python3.6/site-packages/torch/jit/_script.py", line 898, in script
    obj, torch.jit._recursive.infer_methods_to_compile
  File "/usr/local/lib/python3.6/site-packages/torch/jit/_recursive.py", line 352, in create_script_module
    return create_script_module_impl(nn_module, concrete_type, stubs_fn)
  File "/usr/local/lib/python3.6/site-packages/torch/jit/_recursive.py", line 410, in create_script_module_impl
    create_methods_and_properties_from_stubs(concrete_type, method_stubs, property_stubs)
  File "/usr/local/lib/python3.6/site-packages/torch/jit/_recursive.py", line 304, in create_methods_and_properties_from_stubs
    concrete_type._create_methods_and_properties(property_defs, property_rcbs, method_defs, method_rcbs, method_defaults)
RuntimeError: 
Module 'A' has no attribute 'dim' :
  File "/a.py", line 21
    def forward(self, x):
        return self.a(x) + self.a.dim
                           ~~~~~~~~~~ <--- HERE