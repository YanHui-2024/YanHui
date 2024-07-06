2022-03-31T17:11:07.8343008Z ======================================================================
2022-03-31T17:11:07.8345843Z ERROR [0.014s]: test_linear_1d_weight_mismatch_bias_dtype (__main__.TestCudaFuser)
2022-03-31T17:11:07.8347205Z ----------------------------------------------------------------------
2022-03-31T17:11:07.8347834Z Traceback (most recent call last):
2022-03-31T17:11:07.8348239Z   File "test_jit_cuda_fuser.py", line 3322, in test_linear_1d_weight_mismatch_bias_dtype
2022-03-31T17:11:07.8348595Z     jit_o = jitted(x, w, b)
2022-03-31T17:11:07.8349122Z   File "/opt/conda/lib/python3.7/site-packages/torch/testing/_internal/common_utils.py", line 428, in prof_func_call
2022-03-31T17:11:07.8349661Z     return prof_callable(func_call, *args, **kwargs)
2022-03-31T17:11:07.8350336Z   File "/opt/conda/lib/python3.7/site-packages/torch/testing/_internal/common_utils.py", line 425, in prof_callable
2022-03-31T17:11:07.8351373Z     return callable(*args, **kwargs)
2022-03-31T17:11:07.8355944Z RuntimeError: The following operation failed in the TorchScript interpreter.
2022-03-31T17:11:07.8356484Z Traceback of TorchScript (most recent call last):
2022-03-31T17:11:07.8357053Z   File "test_jit_cuda_fuser.py", line 3312, in t
2022-03-31T17:11:07.8357728Z         def t(x: torch.Tensor, w: torch.Tensor, b: torch.Tensor):
2022-03-31T17:11:07.8358665Z             o = torch.nn.functional.linear(x, w, b)
2022-03-31T17:11:07.8359542Z                 ~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
2022-03-31T17:11:07.8360079Z             return o.relu()
2022-03-31T17:11:07.8360774Z RuntimeError: mat2 must be a matrix, got 1-D tensor
2022-03-31T17:11:07.8361193Z 
2022-03-31T17:11:07.8361223Z 
2022-03-31T17:11:07.8361691Z ======================================================================
2022-03-31T17:11:07.8362326Z FAIL [0.006s]: test_int_tensor_input (__main__.TestCudaFuser)
2022-03-31T17:11:07.8363398Z ----------------------------------------------------------------------
2022-03-31T17:11:07.8364030Z Traceback (most recent call last):
2022-03-31T17:11:07.8364752Z   File "test_jit_cuda_fuser.py", line 4060, in test_int_tensor_input
2022-03-31T17:11:07.8365442Z     self._run_helper(t_jit, t, x)
2022-03-31T17:11:07.8366108Z   File "test_jit_cuda_fuser.py", line 154, in _run_helper
2022-03-31T17:11:07.8366768Z     self.assertGraphContainsExactly(jit_op.graph_for(*args), FUSION_GUARD, 1, consider_subgraphs=True)
2022-03-31T17:11:07.8367464Z   File "/opt/conda/lib/python3.7/site-packages/torch/testing/_internal/jit_utils.py", line 326, in assertGraphContainsExactly
2022-03-31T17:11:07.8367878Z     consider_subgraphs)
2022-03-31T17:11:07.8368360Z   File "/opt/conda/lib/python3.7/site-packages/torch/testing/_internal/jit_utils.py", line 320, in perform_assert
2022-03-31T17:11:07.8368781Z     graph, actual, kind, subgraph, expected))
2022-03-31T17:11:07.8369104Z AssertionError: graph(%x.1 : Tensor):
2022-03-31T17:11:07.8369413Z   %1 : bool = prim::Constant[value=0]()
2022-03-31T17:11:07.8369720Z   %2 : int[] = prim::Constant[value=[0]]()
2022-03-31T17:11:07.8370062Z   %3 : Tensor = aten::amax(%x.1, %2, %1) # test_jit_cuda_fuser.py:4057:23
2022-03-31T17:11:07.8370369Z   return (%3)
2022-03-31T17:11:07.8370503Z 
2022-03-31T17:11:07.8370734Z Error: graph contains 0 prim::CudaFusionGuard nodes (including subgraphs) but expected 1
2022-03-31T17:11:07.8370999Z 
2022-03-31T17:11:07.8371142Z ======================================================================
2022-03-31T17:11:07.8371486Z FAIL [0.012s]: test_native_batch_norm_backward (__main__.TestCudaFuser)
2022-03-31T17:11:07.8371946Z ----------------------------------------------------------------------
2022-03-31T17:11:07.8372293Z Traceback (most recent call last):
2022-03-31T17:11:07.8372652Z   File "test_jit_cuda_fuser.py", line 4195, in test_native_batch_norm_backward
2022-03-31T17:11:07.8373127Z     save_invstd, True, 1e-5, [True, True, True]), FUSION_GUARD)
2022-03-31T17:11:07.8373673Z   File "/opt/conda/lib/python3.7/site-packages/torch/testing/_internal/jit_utils.py", line 311, in assertGraphContains
2022-03-31T17:11:07.8374091Z     self.assertTrue(len(out_nodes) > 0)
2022-03-31T17:11:07.8374393Z AssertionError: False is not true
2022-03-31T17:11:07.8374576Z 
2022-03-31T17:11:07.8374694Z ======================================================================
2022-03-31T17:11:07.8375029Z FAIL [0.006s]: test_reduction_empty_axes (__main__.TestCudaFuser)
2022-03-31T17:11:07.8375493Z ----------------------------------------------------------------------
2022-03-31T17:11:07.8375838Z Traceback (most recent call last):
2022-03-31T17:11:07.8376169Z   File "test_jit_cuda_fuser.py", line 4047, in test_reduction_empty_axes
2022-03-31T17:11:07.8376506Z     self._run_helper(t_jit, t, x)
2022-03-31T17:11:07.8376834Z   File "test_jit_cuda_fuser.py", line 154, in _run_helper
2022-03-31T17:11:07.8377260Z     self.assertGraphContainsExactly(jit_op.graph_for(*args), FUSION_GUARD, 1, consider_subgraphs=True)
2022-03-31T17:11:07.8377929Z   File "/opt/conda/lib/python3.7/site-packages/torch/testing/_internal/jit_utils.py", line 326, in assertGraphContainsExactly
2022-03-31T17:11:07.8378338Z     consider_subgraphs)
2022-03-31T17:11:07.8378834Z   File "/opt/conda/lib/python3.7/site-packages/torch/testing/_internal/jit_utils.py", line 320, in perform_assert
2022-03-31T17:11:07.8379234Z     graph, actual, kind, subgraph, expected))
2022-03-31T17:11:07.8379550Z AssertionError: graph(%x.1 : Tensor):
2022-03-31T17:11:07.8379941Z   %1 : bool = prim::Constant[value=0]()
2022-03-31T17:11:07.8380231Z   %2 : NoneType = prim::Constant()
2022-03-31T17:11:07.8380560Z   %3 : int[] = prim::Constant[value=annotate(List[int], [])]()
2022-03-31T17:11:07.8380932Z   %4 : Tensor = aten::sum(%x.1, %3, %1, %2) # test_jit_cuda_fuser.py:4044:23
2022-03-31T17:11:07.8381272Z   return (%4)
2022-03-31T17:11:07.8381421Z 
2022-03-31T17:11:07.8381651Z Error: graph contains 0 prim::CudaFusionGuard nodes (including subgraphs) but expected 1