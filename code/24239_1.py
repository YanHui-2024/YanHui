Traceback (most recent call last):
  File "test.py", line 8, in <module>
    @torch.jit.script
  File "/opt/.miniconda/lib/python3.7/site-packages/torch/jit/__init__.py", line 1181, in script
    return _compile_function(fn=obj, qualified_name=qualified_name, _frames_up=_frames_up + 1, _rcb=_rcb)
  File "/opt/.miniconda/lib/python3.7/site-packages/torch/jit/__init__.py", line 1077, in _compile_function
    script_fn = torch._C._jit_script_compile(qualified_name, ast, _rcb, get_default_args(fn))
RuntimeError:
Arguments for call are not valid.
The following operator variants are available:

  aten::stack(Tensor[] tensors, int dim=0) -> (Tensor):
  Expected a value of type 'List[Tensor]' for argument 'tensors' but instead found type 'List[int]'.

  aten::stack(Tensor[] tensors, int dim=0, *, Tensor(a) out) -> (Tensor(a)):
  Expected a value of type 'List[Tensor]' for argument 'tensors' but instead found type 'List[int]'.

The original call is:
at test.py:10:5
@torch.jit.script
def full():
    torch.stack([channel(torch.randn(1, 3, 3) > 0) for _ in [0, 1, 2]])
    ~~~~~~~~~~~ <--- HERE