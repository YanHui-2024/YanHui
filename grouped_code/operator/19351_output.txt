Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(gc.get_objects())
  File "<frozen importlib._bootstrap>", line 302, in _module_repr
  File "<frozen importlib._bootstrap>", line 295, in _module_repr
  File ".../site-packages/torch/_ops.py", line 60, in __getattr__
    op = torch._C._jit_get_operation(qualified_op_name)
RuntimeError: No such operator __file__::__file__