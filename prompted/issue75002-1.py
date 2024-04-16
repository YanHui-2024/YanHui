import torch
from typing import Optional

def fn(inp, weight, bias: Optional[torch.Tensor] = None):
    if bias is None:
        bias_ = torch.zeros_like(weight[0])
    else:
        bias_ = bias

    with torch.cuda.amp.autocast(enabled=True, dtype=torch.half):
        return torch.nn.functional.conv2d(inp, weight, bias_, 1, 3)

fn_s = torch.jit.script(fn)

inp = torch.rand((5, 3, 224, 224), dtype=torch.float).cuda()
weight = torch.rand((3, 3, 7, 7), dtype=torch.float).cuda()
bias = torch.rand((3), dtype=torch.float).cuda()

print("bias is none")
fn_s(inp, weight, None)

print("bias is not none")
fn_s(inp, weight, bias)

