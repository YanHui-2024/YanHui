import torch
from typing import Optional

def fn(inp: torch.Tensor, other: Optional[torch.Tensor] = None):
    if other is None:
        other = torch.zeros_like(inp)
    with torch.cuda.amp.autocast(enabled=True, dtype=torch.half):
        return inp * other

fn_s = torch.jit.script(fn)

inp = torch.rand((5, 3, 224, 224), dtype=torch.float).cuda()
other = torch.rand((5, 3, 224, 224), dtype=torch.float).cuda()

print("other is none")
fn_s(inp, None)

print("other is not none")
fn_s(inp, other)

