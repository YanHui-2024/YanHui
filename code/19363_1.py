>>> m.linear.in_features
Traceback (most recent call last):
  File "/home/qbx2/anaconda3/lib/python3.7/site-packages/torch/jit/__init__.py", line 1197, in __getattr__
    return ScriptModule.__getattr__(self, attr)
  File "/home/qbx2/anaconda3/lib/python3.7/site-packages/torch/jit/__init__.py", line 1102, in __getattr__
    return Module.__getattr__(self, attr)
  File "/home/qbx2/anaconda3/lib/python3.7/site-packages/torch/nn/modules/module.py", line 535, in __getattr__
    type(self).__name__, name))
AttributeError: 'WeakScriptModuleProxy' object has no attribute 'in_features'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/qbx2/anaconda3/lib/python3.7/site-packages/torch/jit/__init__.py", line 1200, in __getattr__
    return getattr(self.__dict__["_original"](), attr)
AttributeError: 'NoneType' object has no attribute 'in_features'