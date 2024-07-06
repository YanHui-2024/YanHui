# More tests that are ok
test_enum_comp_diff_classes (jit.test_enum.TestEnum) ... ok
test_enum_iterate (jit.test_enum.TestEnum) ... python: Modules/gcmodule.c:380: visit_decref: Assertion `_PyGCHead_REFS(gc) != 0' failed.
Traceback (most recent call last):
  File "run_test.py", line 719, in <module>
    main()
  File "run_test.py", line 708, in main
    raise RuntimeError(err)
RuntimeError: test_jit failed! Received signal: SIGIOT