2023-03-15T16:06:39.6597601Z ================================== FAILURES ===================================
2023-03-15T16:06:39.6597885Z _________ TestJitCPU.test_variant_consistency_jit_diff_cpu_complex64 __________
2023-03-15T16:06:39.6598150Z Traceback (most recent call last):
2023-03-15T16:06:39.6598490Z   File "C:\actions-runner\_work\pytorch\pytorch\test\test_ops_jit.py", line 85, in test_variant_consistency_jit
2023-03-15T16:06:39.6598879Z     self.indiv_variant_test_jit(device, dtype, op, sample, func_type, variant, has_fake_function)
2023-03-15T16:06:39.6599279Z   File "C:\actions-runner\_work\pytorch\pytorch\test\test_ops_jit.py", line 136, in indiv_variant_test_jit
2023-03-15T16:06:39.6599585Z     check_against_reference(self,
2023-03-15T16:06:39.6599950Z   File "C:\actions-runner\_work\pytorch\pytorch\build\win_tmp\build\torch\testing\_internal\common_jit.py", line 108, in check_against_reference
2023-03-15T16:06:39.6600379Z     outputs_test = output_func(self.runAndSaveRNG(func, recording_inputs, kwargs))
2023-03-15T16:06:39.6600910Z   File "C:\actions-runner\_work\pytorch\pytorch\build\win_tmp\build\torch\testing\_internal\common_jit.py", line 160, in runAndSaveRNG
2023-03-15T16:06:39.6601259Z     results = func(*inputs, **kwargs)
2023-03-15T16:06:39.6601687Z   File "C:\actions-runner\_work\pytorch\pytorch\build\win_tmp\build\torch\testing\_internal\jit_metaprogramming_utils.py", line 471, in traced_fn
2023-03-15T16:06:39.6602114Z     self.assertExportImport(traced.graph, split_inputs.all_tensors)
2023-03-15T16:06:39.6602550Z   File "C:\actions-runner\_work\pytorch\pytorch\build\win_tmp\build\torch\testing\_internal\common_jit.py", line 148, in assertExportImport
2023-03-15T16:06:39.6602944Z     self.assertExportImportModule(m, inputs)
2023-03-15T16:06:39.6603348Z   File "C:\actions-runner\_work\pytorch\pytorch\build\win_tmp\build\torch\testing\_internal\common_jit.py", line 151, in assertExportImportModule
2023-03-15T16:06:39.6603740Z     m_import = self.getExportImportCopy(m)
2023-03-15T16:06:39.6604141Z   File "C:\actions-runner\_work\pytorch\pytorch\build\win_tmp\build\torch\testing\_internal\common_jit.py", line 174, in getExportImportCopy
2023-03-15T16:06:39.6604525Z     return torch.jit.load(fname, map_location=map_location)
2023-03-15T16:06:39.6604900Z   File "C:\actions-runner\_work\pytorch\pytorch\build\win_tmp\build\torch\jit\_serialization.py", line 162, in load
2023-03-15T16:06:39.6605388Z     cpp_module = torch._C.import_ir_module(cu, str(f), map_location, _extra_files, _restore_shapes)  # type: ignore[call-arg]
2023-03-15T16:06:39.6605886Z RuntimeError: open file failed because of errno 22 on fopen: Invalid argument, file path: C:\Users\RUNNER~1\AppData\Local\Temp\tmpbg1wa8z3