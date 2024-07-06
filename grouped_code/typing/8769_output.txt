Traceback (most recent call last):
  File "test/test_jit.py", line 4407, in test_time_sequence_prediction
    self.checkTrace(Sequence(), (torch.rand(97, 999),), verbose=True)
  File "/Users/wanchaol/pytorch/torch/jit/__init__.py", line 558, in init_then_register
    self._create_methods(asts, rcbs)
RuntimeError:
arguments for call are not valid:

  for operator zeros(IntList size, int64_t dtype=<default>, IntList device=<default>, int64_t layout=<default>):
  expected a value of type Tensor for argument 'size' but found (Tensor, int)
