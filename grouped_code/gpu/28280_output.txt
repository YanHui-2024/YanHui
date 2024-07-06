cuda:0
cuda:0
cpu

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-49-a9cb0d104a1f> in <module>
     23 m = m.to('cuda')
     24 print(m.a.device)  # prints cuda
---> 25 m(torch.zeros(10).to('cuda'))  # fails because m.a is on cpu inside non_scriptable

~/.conda/envs/MTMSF/lib/python3.7/site-packages/torch/nn/modules/module.py in __call__(self, *input, **kwargs)
    543             result = self._slow_forward(*input, **kwargs)
    544         else:
--> 545             result = self.forward(*input, **kwargs)
    546         for hook in self._forward_hooks.values():
    547             hook_result = hook(self, input, result)

RuntimeError: RuntimeError: expected device cuda:0 but got device cpu