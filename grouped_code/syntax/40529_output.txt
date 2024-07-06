graph(%self : __torch__.TestModule,
      %2 : Dict(str, Tensor)):
  %3 : Long()[] = aten::values(%2)
  %4 : Long() = prim::ListUnpack(%3)
  return (%4)

tensor(1)
Traceback (most recent call last):
  File "/home/wanchaol/test_trace.py", line 24, in <module>
    print(m_traced(input_2))
  File "/home/wanchaol/pytorch/torch/nn/modules/module.py", line 722, in _call_impl
    result = self.forward(*input, **kwargs)
RuntimeError: The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
RuntimeError: Expected 1 elements in a list but found 2