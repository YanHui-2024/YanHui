Traceback (most recent call last):
  File "/venv/lib/python3.8/site-packages/_pydevd_bundle/pydevd_exec2.py", line 3, in Exec
    exec(exp, global_vars, local_vars)
  File "<input>", line 1, in <module>
  File "<frozen importlib._bootstrap>", line 302, in _module_repr
  File "<frozen importlib._bootstrap>", line 295, in _module_repr
  File "/venv/lib/python3.8/site-packages/torch/_classes.py", line 10, in __getattr__
    proxy = torch._C._get_custom_class_python_wrapper(self.name, attr)
RuntimeError: Tried to instantiate class '__file__.__file__', but it does not exist! Ensure that it is registered via torch::class_
