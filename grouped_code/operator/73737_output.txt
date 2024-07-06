Traceback (most recent call last):
  File "test_trace.py", line 13, in <module>
    torch.jit.trace(m, torch.randn(1))
  File "/home/haozhe/rebase/frameworks.ai.pytorch.private-cpu/torch/jit/_trace.py", line 741, in trace
    return trace_module(
  File "/home/haozhe/rebase/frameworks.ai.pytorch.private-cpu/torch/jit/_trace.py", line 942, in trace_module
    module = make_module(mod, _module_class, _compilation_unit)
  File "/home/haozhe/rebase/frameworks.ai.pytorch.private-cpu/torch/jit/_trace.py", line 568, in make_module
    return _module_class(mod, _compilation_unit=_compilation_unit)
  File "/home/haozhe/rebase/frameworks.ai.pytorch.private-cpu/torch/jit/_trace.py", line 1067, in __init__
    tmp_module._modules[name] = make_module(
  File "/home/haozhe/rebase/frameworks.ai.pytorch.private-cpu/torch/jit/_trace.py", line 556, in make_module
    elif torch._jit_internal.module_has_exports(mod):
  File "/home/haozhe/rebase/frameworks.ai.pytorch.private-cpu/torch/_jit_internal.py", line 675, in module_has_exports
    if hasattr(mod, name):
TypeError: hasattr(): attribute name must be string