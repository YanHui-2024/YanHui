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

