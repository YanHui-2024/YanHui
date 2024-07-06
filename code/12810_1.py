Error message:
Traceback (most recent call last):
  File "ttt.py", line 11, in <module>
    fun(a)
  File "/usr/local/lib/python3.5/dist-packages/torch/nn/modules/module.py", line 477, in __call__
    result = self.forward(*input, **kwargs)
RuntimeError: 
Schema not found for node. File a bug report.
Node: %4 : Dynamic = prim::None()

Input types:
candidates were:
:
@torch.jit.script
def fun(a):
	return a[None, :]
          ~~~~ <--- HERE