======================================================================
ERROR: test_python_submodule_script (jit.test_data_parallel.TestDataParallel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/pytorch/pytorch/test/jit/test_data_parallel.py", line 89, in test_python_submodule_script
    replicas = dp.replicate(module, {0, 1})
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 91, in replicate
    param_copies = _broadcast_coalesced_reshape(params, devices, detach)
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 71, in _broadcast_coalesced_reshape
    tensor_copies = Broadcast.apply(devices, *tensors)
  File "/opt/pytorch/pytorch/torch/autograd/function.py", line 506, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/opt/pytorch/pytorch/torch/nn/parallel/_functions.py", line 23, in forward
    outputs = comm.broadcast_coalesced(inputs, ctx.target_gpus)
  File "/opt/pytorch/pytorch/torch/nn/parallel/comm.py", line 58, in broadcast_coalesced
    return torch._C._broadcast_coalesced(tensors, devices, buffer_size)
RuntimeError: All tensors must be on devices[0]: 0

======================================================================
ERROR: test_shared_module (jit.test_data_parallel.TestDataParallel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/pytorch/pytorch/test/jit/test_data_parallel.py", line 97, in test_shared_module
    replicas = dp.replicate(module, {0, 1})
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 91, in replicate
    param_copies = _broadcast_coalesced_reshape(params, devices, detach)
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 71, in _broadcast_coalesced_reshape
    tensor_copies = Broadcast.apply(devices, *tensors)
  File "/opt/pytorch/pytorch/torch/autograd/function.py", line 506, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/opt/pytorch/pytorch/torch/nn/parallel/_functions.py", line 23, in forward
    outputs = comm.broadcast_coalesced(inputs, ctx.target_gpus)
  File "/opt/pytorch/pytorch/torch/nn/parallel/comm.py", line 58, in broadcast_coalesced
    return torch._C._broadcast_coalesced(tensors, devices, buffer_size)
RuntimeError: All tensors must be on devices[0]: 0

======================================================================
ERROR: test_tensor_sharing (jit.test_data_parallel.TestDataParallel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/pytorch/pytorch/test/jit/test_data_parallel.py", line 109, in test_tensor_sharing
    replica = dp.replicate(module, {0, 1})
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 91, in replicate
    param_copies = _broadcast_coalesced_reshape(params, devices, detach)
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 71, in _broadcast_coalesced_reshape
    tensor_copies = Broadcast.apply(devices, *tensors)
  File "/opt/pytorch/pytorch/torch/autograd/function.py", line 506, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/opt/pytorch/pytorch/torch/nn/parallel/_functions.py", line 23, in forward
    outputs = comm.broadcast_coalesced(inputs, ctx.target_gpus)
  File "/opt/pytorch/pytorch/torch/nn/parallel/comm.py", line 58, in broadcast_coalesced
    return torch._C._broadcast_coalesced(tensors, devices, buffer_size)
RuntimeError: All tensors must be on devices[0]: 0

======================================================================
ERROR: test_tensor_sharing_with_forward (jit.test_data_parallel.TestDataParallel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/pytorch/pytorch/test/jit/test_data_parallel.py", line 134, in test_tensor_sharing_with_forward
    replica = dp.replicate(module, {0, 1})
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 91, in replicate
    param_copies = _broadcast_coalesced_reshape(params, devices, detach)
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 71, in _broadcast_coalesced_reshape
    tensor_copies = Broadcast.apply(devices, *tensors)
  File "/opt/pytorch/pytorch/torch/autograd/function.py", line 506, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/opt/pytorch/pytorch/torch/nn/parallel/_functions.py", line 23, in forward
    outputs = comm.broadcast_coalesced(inputs, ctx.target_gpus)
  File "/opt/pytorch/pytorch/torch/nn/parallel/comm.py", line 58, in broadcast_coalesced
    return torch._C._broadcast_coalesced(tensors, devices, buffer_size)
RuntimeError: All tensors must be on devices[0]: 0

======================================================================
ERROR: test_traced_module (jit.test_data_parallel.TestDataParallel)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/pytorch/pytorch/test/jit/test_data_parallel.py", line 103, in test_traced_module
    replicas = dp.replicate(module, {0, 1})
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 91, in replicate
    param_copies = _broadcast_coalesced_reshape(params, devices, detach)
  File "/opt/pytorch/pytorch/torch/nn/parallel/replicate.py", line 71, in _broadcast_coalesced_reshape
    tensor_copies = Broadcast.apply(devices, *tensors)
  File "/opt/pytorch/pytorch/torch/autograd/function.py", line 506, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/opt/pytorch/pytorch/torch/nn/parallel/_functions.py", line 23, in forward
    outputs = comm.broadcast_coalesced(inputs, ctx.target_gpus)
  File "/opt/pytorch/pytorch/torch/nn/parallel/comm.py", line 58, in broadcast_coalesced
    return torch._C._broadcast_coalesced(tensors, devices, buffer_size)
RuntimeError: All tensors must be on devices[0]: 0

======================================================================
FAIL: test_streams_and_events (jit.test_cuda.TestCUDA)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/pytorch/pytorch/torch/testing/_internal/common_utils.py", line 1075, in wrapper
    fn(*args, **kwargs)
  File "/opt/pytorch/pytorch/test/jit/test_cuda.py", line 220, in test_streams_and_events
    self.assertTrue(is_device_d0)
AssertionError: False is not true

======================================================================
FAIL: test_script_get_device_cuda (__main__.TestScript)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/pytorch/pytorch/test/test_jit.py", line 9824, in test_script_get_device_cuda
    self.assertEqual(foo(v), 0)
  File "/opt/pytorch/pytorch/torch/testing/_internal/common_utils.py", line 2979, in assertEqual
    raise error_metas[0].to_error(
AssertionError: Scalars are not equal!

Absolute difference: 1
Relative difference: inf

----------------------------------------------------------------------
Ran 2676 tests in 159.745s

FAILED (failures=2, errors=5, skipped=67, expected failures=10)