
======================================================================
ERROR: test_permute (__main__.TestAutogradGenerated)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test/test_autograd.py", line 3665, in do_test
    check(name)
  File "test/test_autograd.py", line 3592, in check
    fn, (self_variable,) + args_variable)
  File "test/test_autograd.py", line 3498, in check_against_reference
    outputs_test = func(*nograd_inputs)
  File "test/test_autograd.py", line 3473, in script_fn
    CU = torch.jit.CompilationUnit(script)
  File "/data/users/zdevito/pytorch/torch/jit/__init__.py", line 352, in __init__
    self.define(lang, _frames_up=_frames_up + 1)
  File "/data/users/zdevito/pytorch/torch/jit/__init__.py", line 358, in define
    self.module._define(lang, rcb, False)
RuntimeError: 
arguments for call are not valid:
  
  for operator permute(Tensor self, IntList dims):
  expected at most 2 arguments  but found 5
  
  def the_method(i0):
      return i0.permute(0, 2, 3, 1)
             ~~~~~~~~~~ <--- HERE
  
for call at:

def the_method(i0):
    return i0.permute(0, 2, 3, 1)
           ~~~~~~~~~~ <--- HERE


======================================================================
ERROR: test_permute_neg_dim (__main__.TestAutogradGenerated)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test/test_autograd.py", line 3665, in do_test
    check(name)
  File "test/test_autograd.py", line 3592, in check
    fn, (self_variable,) + args_variable)
  File "test/test_autograd.py", line 3498, in check_against_reference
    outputs_test = func(*nograd_inputs)
  File "test/test_autograd.py", line 3473, in script_fn
    CU = torch.jit.CompilationUnit(script)
  File "/data/users/zdevito/pytorch/torch/jit/__init__.py", line 352, in __init__
    self.define(lang, _frames_up=_frames_up + 1)
  File "/data/users/zdevito/pytorch/torch/jit/__init__.py", line 358, in define
    self.module._define(lang, rcb, False)
RuntimeError: 
arguments for call are not valid:
  
  for operator permute(Tensor self, IntList dims):
  expected at most 2 arguments  but found 5
  
  def the_method(i0):
      return i0.permute(0, -2, -1, 1)
             ~~~~~~~~~~ <--- HERE
  
for call at:

def the_method(i0):
    return i0.permute(0, -2, -1, 1)
           ~~~~~~~~~~ <--- HERE