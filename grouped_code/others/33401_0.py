======================================================================
ERROR: test_abs_cpu (__main__.TestFuser)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 592, in wrapper
    fn(*args, **kwargs)
  File "test_jit_fuser.py", line 79, in test_abs_cpu
    self._test_fused_abs()
  File "test_jit_fuser.py", line 74, in _test_fused_abs
    self.assertAllFused(func.graph_for(a))
  File "C:\Users\circleci\project\build\win_tmp\build\torch\jit\__init__.py", line 2094, in _graph_for
    self(*args, **kwargs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 87, in prof_func_call
    return prof_callable(func_call, *args, **kwargs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 84, in prof_callable
    return callable(*args, **kwargs)
RuntimeError: Caught an unknown exception!

======================================================================
ERROR: test_chunk_correctness (__main__.TestFuser)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 592, in wrapper
    fn(*args, **kwargs)
  File "test_jit_fuser.py", line 223, in test_chunk_correctness
    return self._test_chunk_correctness(self, 'cpu')
  File "test_jit_fuser.py", line 218, in _test_chunk_correctness
    self.checkScript(fn, [tensor])
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 398, in checkScript
    opt_script_outputs = scripted_fn(*recording_inputs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 87, in prof_func_call
    return prof_callable(func_call, *args, **kwargs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 84, in prof_callable
    return callable(*args, **kwargs)
RuntimeError: Caught an unknown exception!

======================================================================
ERROR: test_scalar (__main__.TestFuser)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 592, in wrapper
    fn(*args, **kwargs)
  File "test_jit_fuser.py", line 851, in test_scalar
    ge = self.checkScript(fn, (x, y))
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 398, in checkScript
    opt_script_outputs = scripted_fn(*recording_inputs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 87, in prof_func_call
    return prof_callable(func_call, *args, **kwargs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 84, in prof_callable
    return callable(*args, **kwargs)
RuntimeError: Caught an unknown exception!

======================================================================
ERROR: test_where_and_typing (__main__.TestFuser)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\jit_utils.py", line 592, in wrapper
    fn(*args, **kwargs)
  File "test_jit_fuser.py", line 906, in test_where_and_typing
    self.assertAllFused(script_f.graph_for(x, y), except_for={'prim::TupleConstruct'})
  File "C:\Users\circleci\project\build\win_tmp\build\torch\jit\__init__.py", line 2094, in _graph_for
    self(*args, **kwargs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 87, in prof_func_call
    return prof_callable(func_call, *args, **kwargs)
  File "C:\Users\circleci\project\build\win_tmp\build\torch\testing\_internal\common_utils.py", line 84, in prof_callable
    return callable(*args, **kwargs)
RuntimeError: Caught an unknown exception!

----------------------------------------------------------------------
Ran 46 tests in 11.883s

FAILED (errors=4, skipped=10)
Traceback (most recent call last):
  File "run_test.py", line 486, in <module>
    main()
  File "run_test.py", line 479, in main
    raise RuntimeError(message)
RuntimeError: test_jit_fuser failed!