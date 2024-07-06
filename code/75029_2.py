2022-03-31T18:09:00.4229799Z FAIL [0.513s]: test_context_manager_test (__main__.TestPassManagerCudaFuser)
2022-03-31T18:09:00.4230330Z ----------------------------------------------------------------------
2022-03-31T18:09:00.4230663Z Traceback (most recent call last):
2022-03-31T18:09:00.4231703Z   File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1780, in wrapper
2022-03-31T18:09:00.4232092Z     method(*args, **kwargs)
2022-03-31T18:09:00.4232472Z   File "/var/lib/jenkins/workspace/test/test_jit_cuda_fuser.py", line 4422, in test_context_manager_test
2022-03-31T18:09:00.4233045Z     self.assertGraphContainsExactly(t_jit_3.graph_for(x, y), FUSION_GUARD, 0)
2022-03-31T18:09:00.4233690Z   File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/jit_utils.py", line 339, in assertGraphContainsExactly
2022-03-31T18:09:00.4234158Z     perform_assert(graph, kind, len(out_nodes), num_kind_nodes,
2022-03-31T18:09:00.4234686Z   File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/jit_utils.py", line 318, in perform_assert
2022-03-31T18:09:00.4235076Z     raise AssertionError(
2022-03-31T18:09:00.4235362Z AssertionError: graph(%x.1 : Tensor,
2022-03-31T18:09:00.4235635Z       %y.1 : Tensor):
2022-03-31T18:09:00.4236118Z   %2 : bool = prim::CudaFusionGuard[types=[Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0), Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0)]](%x.1, %y.1)
2022-03-31T18:09:00.4236553Z   %3 : Tensor = prim::If(%2)
2022-03-31T18:09:00.4236804Z     block0():
2022-03-31T18:09:00.4237102Z       %o.8 : Tensor = prim::CudaFusionGroup_0[cache_id=1650](%x.1, %y.1)
2022-03-31T18:09:00.4237453Z       -> (%o.8)
2022-03-31T18:09:00.4237684Z     block1():
2022-03-31T18:09:00.4237991Z       %5 : Function = prim::Constant[name="fallback_function", fallback=1]()
2022-03-31T18:09:00.4238425Z       %6 : (Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0)) = prim::CallFunction(%5, %x.1, %y.1)
2022-03-31T18:09:00.4238858Z       %7 : Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0) = prim::TupleUnpack(%6)
2022-03-31T18:09:00.4239209Z       -> (%7)
2022-03-31T18:09:00.4239421Z   return (%3)
2022-03-31T18:09:00.4239776Z with prim::CudaFusionGroup_0 = graph(%0 : Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0),
2022-03-31T18:09:00.4240186Z       %1 : Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0)):
2022-03-31T18:09:00.4240610Z   %2 : float = prim::Constant[value=4.]() # /var/lib/jenkins/workspace/test/test_jit_cuda_fuser.py:4417:20
2022-03-31T18:09:00.4240968Z   %3 : int = prim::Constant[value=1]()
2022-03-31T18:09:00.4241414Z   %o.1 : Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0) = aten::add(%0, %1, %3) # /var/lib/jenkins/workspace/test/test_jit_cuda_fuser.py:4416:16
2022-03-31T18:09:00.4241974Z   %o.5 : Float(4, 8, strides=[8, 1], requires_grad=0, device=cuda:0) = aten::add(%o.1, %2, %3) # /var/lib/jenkins/workspace/test/test_jit_cuda_fuser.py:4417:16
2022-03-31T18:09:00.4242354Z   return (%o.5)
2022-03-31T18:09:00.4242492Z 
2022-03-31T18:09:00.4242722Z Error: graph contains 1 prim::CudaFusionGuard nodes (excluding subgraphs) but expected 0
2022-03-31T18:09:00.4242987Z 
2022-03-31T18:09:00.4243123Z ======================================================================
2022-03-31T18:09:00.4243475Z FAIL [0.002s]: test_register_fuser (__main__.TestPassManagerCudaFuser)
2022-03-31T18:09:00.4243946Z ----------------------------------------------------------------------
2022-03-31T18:09:00.4244300Z Traceback (most recent call last):
2022-03-31T18:09:00.4244810Z   File "/opt/conda/lib/python3.9/site-packages/torch/testing/_internal/common_utils.py", line 1780, in wrapper
2022-03-31T18:09:00.4245190Z     method(*args, **kwargs)
2022-03-31T18:09:00.4245540Z   File "/var/lib/jenkins/workspace/test/test_jit_cuda_fuser.py", line 4426, in test_register_fuser
2022-03-31T18:09:00.4245953Z     self.assertFalse(torch._C._jit_set_nvfuser_enabled(True))
2022-03-31T18:09:00.4246285Z AssertionError: True is not false