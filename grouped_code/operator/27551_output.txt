(tensor([[[[-0.8175, -0.3000,  0.0693, -1.0097],
          [-0.3261,  0.6817, -0.8282, -1.8818],
          [-1.1303,  1.8587,  0.0275, -0.2838]],

         [[ 0.2386,  0.3672,  1.0122, -1.3396],
          [ 0.6037, -0.8609,  0.6339,  0.8278],
          [ 1.0117, -0.3204, -1.6440,  2.8207]]]]),)

Traceback (most recent call last):
  File "/tmp/1.py", line 12, in <module>
    print(torch.jit.trace(m, x))
  File "torch/jit/__init__.py", line 860, in trace
    check_tolerance, _force_outplace, _module_class)
  File "torch/jit/__init__.py", line 999, in trace_module
    module._c._create_method_from_trace(method_name, func, example_inputs, var_lookup_fn, _force_outplace)
  File "torch/nn/modules/module.py", line 543, in __call__
    result = self._slow_forward(*input, **kwargs)
  File "torch/nn/modules/module.py", line 529, in _slow_forward
    result = self.forward(*input, **kwargs)
  File "/tmp/1.py", line 6, in forward
    return torch.split(x, x.size(1))
  File "torch/functional.py", line 77, in split
    return tensor.split(split_size_or_sections, dim)
  File "torch/tensor.py", line 339, in split
    return super(Tensor, self).split_with_sizes(split_size, dim)
TypeError: split_with_sizes(): argument 'split_sizes' (position 1) must be tuple of ints, not Tensor