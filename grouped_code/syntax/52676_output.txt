Traceback (most recent call last):
  File "test/tinytest.py", line 22, in <module>
    scripted = torch.jit.script(M())
  File "/home/ansley/local/miniconda3/envs/pytorch/lib/python3.8/site-packages/torch/jit/_script.py", line 947, in script
    return torch.jit._recursive.create_script_module(
  File "/home/ansley/local/miniconda3/envs/pytorch/lib/python3.8/site-packages/torch/jit/_recursive.py", line 398, in create_script_module
    return create_script_module_impl(nn_module, concrete_type, stubs_fn)
  File "/home/ansley/local/miniconda3/envs/pytorch/lib/python3.8/site-packages/torch/jit/_recursive.py", line 459, in create_script_module_impl
    create_methods_and_properties_from_stubs(concrete_type, method_stubs, property_stubs)
  File "/home/ansley/local/miniconda3/envs/pytorch/lib/python3.8/site-packages/torch/jit/_recursive.py", line 341, in create_methods_and_properties_from_stubs
    concrete_type._create_methods_and_properties(property_defs, property_rcbs, method_defs, method_rcbs, method_defaults)
  File "/home/ansley/local/miniconda3/envs/pytorch/lib/python3.8/site-packages/torch/jit/annotations.py", line 351, in try_ann_to_type
    return torch._C._resolve_type_from_object(ann, loc, fake_rcb)
RuntimeError: 
Default values are currently not supported on NamedTuple fields in TorchScript. Fields with default values: [xy]:
  File "test/tinytest.py", line 17
    def forward(self, point: Point):
                             ~~~~~ <--- HERE
        return point