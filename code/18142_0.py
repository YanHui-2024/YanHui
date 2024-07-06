ERROR: test_trace_c10_ops (__main__.TestJit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test/test_jit.py", line 1431, in test_trace_c10_ops
    traced_model = torch.jit.trace(model, inputs)
  File "/data/users/zdevito/pytorch/torch/jit/__init__.py", line 668, in trace
    var_lookup_fn, _force_outplace)
  File "/data/users/zdevito/pytorch/torch/nn/modules/module.py", line 489, in __call__
    result = self._slow_forward(*input, **kwargs)
  File "/data/users/zdevito/pytorch/torch/nn/modules/module.py", line 479, in _slow_forward
    result = self.forward(*input, **kwargs)
  File "test/test_jit.py", line 1414, in forward
    a, b = torch.ops._caffe2.GenerateProposals(
  File "/data/users/zdevito/pytorch/torch/_ops.py", line 60, in __getattr__
    op = torch._C._jit_get_operation(qualified_op_name)
RuntimeError: No such operator _caffe2::GenerateProposals