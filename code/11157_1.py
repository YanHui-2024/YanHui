Traceback (most recent call last):
  File "examples/ein.py", line 4, in <module>
    @torch.jit.trace(torch.ones(2, 3), torch.ones(2, 3))
  File "/Users/npradhan/miniconda2/envs/pytorch-master/lib/python3.6/site-packages/torch/jit/__init__.py", line 290, in wrapper
    module._create_method_from_trace('forward', func, tuple(args))
  File "examples/ein.py", line 6, in fn
    return torch.einsum('ab,ab->b', [x, y])
  File "/Users/npradhan/miniconda2/envs/pytorch-master/lib/python3.6/site-packages/torch/functional.py", line 239, in einsum
    return torch._C._VariableFunctions.einsum(equation, operands)
RuntimeError: Found an unsupported argument type in the JIT tracer. File a bug report.