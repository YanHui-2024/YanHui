﻿﻿Traceback (most recent call last):
  File "dtype.py", line 3, in <module>
    @torch.jit.script
  File "/Users/jamesreed/onnx-fairseq/pytorch/torch/jit/__init__.py", line 351, in script
    graph = _jit_script_compile(ast, rcb)
RuntimeError: 
arguments for call are not valid:
  
  for operator aten::zeros(int[] size, *, int dtype=<default>, int layout=<default>, int[] device=<default>) -> Tensor:
  argument dtype specified twice 
  @torch.jit.script
  def create_zeros():
      return torch.zeros(1, 2, 3, dtype=torch.long)
                                        ~~~~~~~~~~ <--- HERE
for call at:
@torch.jit.script
def create_zeros():
    return torch.zeros(1, 2, 3, dtype=torch.long)
           ~~~~~~~~~~~ <--- HERE

