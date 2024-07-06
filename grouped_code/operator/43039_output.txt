Traceback (most recent call last):
  File "pytorch.py", line 17, in <module>
    traced_script_module = torch.jit.trace(model, example)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/torch/jit/__init__.py", line 955, in trace
    check_tolerance, strict, _force_outplace, _module_class)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/torch/jit/__init__.py", line 1119, in trace_module
    check_tolerance, strict, _force_outplace, True, _module_class)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/torch/autograd/grad_mode.py", line 15, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/torch/jit/__init__.py", line 597, in _check_trace
    copied_dict[name] = _clone_inputs(data)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/torch/jit/__init__.py", line 450, in _clone_inputs
    clone_input, condition_msg="tensors")(args)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/torch/autograd/function.py", line 263, in _map
    return fn(obj)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/torch/jit/__init__.py", line 443, in clone_input
    v = a.detach().clone(memory_format=torch.preserve_format).requires_grad_(a.requires_grad)
RuntimeError: unsupported memory format option Preserve