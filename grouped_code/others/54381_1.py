test_variant_consistency_jit_pinverse_cuda_float64 - TestCommonCUDA
test_ops.py
Traceback (most recent call last):
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_utils.py", line 955, in wrapper
    method(*args, **kwargs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_device_type.py", line 292, in instantiated_test
    raise rte
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_device_type.py", line 287, in instantiated_test
    result = test_fn(self, *args)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_device_type.py", line 584, in dep_fn
    return fn(slf, device, *args, **kwargs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_device_type.py", line 584, in dep_fn
    return fn(slf, device, *args, **kwargs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_device_type.py", line 584, in dep_fn
    return fn(slf, device, *args, **kwargs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_device_type.py", line 265, in test_wrapper
    return test(*args, **kwargs)
  File "test_ops.py", line 317, in test_variant_consistency_jit
    no_grad=not test_backward)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_jit.py", line 78, in check_against_reference
    outputs_test = output_func(self.runAndSaveRNG(func, recording_inputs, kwargs))
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_jit.py", line 130, in runAndSaveRNG
    results = func(*inputs, **kwargs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/jit_metaprogramming_utils.py", line 302, in script_fn
    self.assertExportImport(fn.graph, tensors)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_jit.py", line 118, in assertExportImport
    self.assertExportImportModule(m, inputs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_jit.py", line 122, in assertExportImportModule
    a = self.runAndSaveRNG(m, inputs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_jit.py", line 130, in runAndSaveRNG
    results = func(*inputs, **kwargs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_utils.py", line 131, in prof_func_call
    return prof_callable(func_call, *args, **kwargs)
  File "/opt/conda/lib/python3.6/site-packages/torch/testing/_internal/common_utils.py", line 128, in prof_callable
    return callable(*args, **kwargs)
RuntimeError: The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
  File "<string>", line 3, in forward

def the_method(i0):
    return torch.pinverse(i0)
           ~~~~~~~~~~~~~~ <--- HERE
RuntimeError: magma: The value of work_size(-9223372036854775808) is too large to fit into a magma_int_t (4 bytes)