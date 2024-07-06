FAIL [0.063s]: test_nvfuser_correctness_nn_functional_conv_transpose3d_cuda_float16 (__main__.TestCudaFuserOpInfoCUDA)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1780, in wrapper
    method(*args, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1780, in wrapper
    method(*args, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_device_type.py", line 376, in instantiated_test
    result = test(self, **param_kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_device_type.py", line 780, in test_wrapper
    return test(*args, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1087, in wrapper
    fn(*args, **kwargs)
  File "/var/lib/jenkins/workspace/test/test_jit_cuda_fuser.py", line 4457, in test_nvfuser_correctness
    val = trace(*clone_inputs((sample.input, *sample.args)), **sample.kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/jit_metaprogramming_utils.py", line 368, in traced_fn
    self.assertExportImport(traced.graph, inputs_tensors)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_jit.py", line 148, in assertExportImport
    self.assertExportImportModule(m, inputs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_jit.py", line 154, in assertExportImportModule
    self.assertEqual(a, b, "Results of original model and "
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 2150, in assertEqual
    assert_equal(
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_comparison.py", line 1084, in assert_equal
    raise error_metas[0].to_error()
AssertionError: Results of original model and exported/imported version of model differed

======================================================================
FAIL [0.161s]: test_nvfuser_correctness_nn_functional_conv_transpose3d_cuda_float32 (__main__.TestCudaFuserOpInfoCUDA)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1780, in wrapper
    method(*args, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1780, in wrapper
    method(*args, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_device_type.py", line 376, in instantiated_test
    result = test(self, **param_kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_device_type.py", line 780, in test_wrapper
    return test(*args, **kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1087, in wrapper
    fn(*args, **kwargs)
  File "/var/lib/jenkins/workspace/test/test_jit_cuda_fuser.py", line 4455, in test_nvfuser_correctness
    trace(*clone_inputs((sample.input, *sample.args)), **sample.kwargs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/jit_metaprogramming_utils.py", line 368, in traced_fn
    self.assertExportImport(traced.graph, inputs_tensors)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_jit.py", line 148, in assertExportImport
    self.assertExportImportModule(m, inputs)
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_jit.py", line 154, in assertExportImportModule
    self.assertEqual(a, b, "Results of original model and "
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 2150, in assertEqual
    assert_equal(
  File "/opt/conda/lib/python3.9/site-packages/torch/testing/_comparison.py", line 1084, in assert_equal
    raise error_metas[0].to_error()
AssertionError: Results of original model and exported/imported version of model differed

----------------------------------------------------------------------
Ran 4571 tests in 2673.458s

FAILED (failures=2, skipped=206, expected failures=6)