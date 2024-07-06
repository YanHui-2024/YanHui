In [1]: import torch

In [2]: torch.__version__
Out[2]: '1.12.0.dev20220412'

In [3]: import torch as th
   ...: 
   ...: 
   ...: class TestMod(th.nn.Module):
   ...:     def __init__(self):
   ...:         super().__init__()
   ...:         self.params = th.nn.ParameterDict(
   ...:             {"hi": th.nn.Parameter(th.zeros(3)), "bye": th.nn.Parameter(th.zeros(3))}
   ...:         )
   ...: 
   ...:     def forward(self, x):
   ...:         return x + self.params["hi"] + self.params["bye"]
   ...: 
   ...: 
   ...: mod = TestMod()
   ...: smod = th.jit.script(mod)