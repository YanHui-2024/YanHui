Traceback (most recent call last):
  File "/Users/npradhan/workspace/pyro_dev/pyro/examples/ex1.py", line 10, in <module>
    compiled_fn = torch.jit.trace(fn, (torch.zeros(2, 3), torch.ones(2, 3)))
  File "/Users/npradhan/miniconda2/envs/pytorch-master/lib/python3.6/site-packages/torch/jit/__init__.py", line 501, in trace
    module._create_method_from_trace('forward', func, example_inputs)
  File "/Users/npradhan/workspace/pyro_dev/pyro/examples/ex1.py", line 7, in fn
    return d.sample()
  File "/Users/npradhan/miniconda2/envs/pytorch-master/lib/python3.6/site-packages/torch/distributions/normal.py", line 54, in sample
    return torch.normal(self.loc.expand(shape), self.scale.expand(shape))
RuntimeError: Found an unsupported argument type in the JIT tracer: at::Generator*. File a bug report.