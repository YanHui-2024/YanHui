Traceback (most recent call last):
  File "final.py", line 14, in <module>
    torch.jit.script(M())
  File "/home/gaoxiang/.local/lib/python3.8/site-packages/torch/jit/__init__.py", line 1304, in script
    return torch.jit._recursive.create_script_module(obj, torch.jit._recursive.infer_methods_to_compile)
  File "/home/gaoxiang/.local/lib/python3.8/site-packages/torch/jit/_recursive.py", line 305, in create_script_module
    concrete_type = concrete_type_store.get_or_create_concrete_type(nn_module)
  File "/home/gaoxiang/.local/lib/python3.8/site-packages/torch/jit/_recursive.py", line 264, in get_or_create_concrete_type
    concrete_type_builder = infer_concrete_type_builder(nn_module)
  File "/home/gaoxiang/.local/lib/python3.8/site-packages/torch/jit/_recursive.py", line 226, in infer_concrete_type_builder
    attr_type = infer_type(name, value)
  File "/home/gaoxiang/.local/lib/python3.8/site-packages/torch/jit/_recursive.py", line 94, in infer_type
    attr_type = torch.jit.annotations.ann_to_type(class_annotations[name], _jit_internal.fake_range())
  File "/home/gaoxiang/.local/lib/python3.8/site-packages/torch/jit/annotations.py", line 302, in ann_to_type
    raise ValueError("Unknown type annotation: '{}'".format(ann))
ValueError: Unknown type annotation: 'typing.Final[float]'