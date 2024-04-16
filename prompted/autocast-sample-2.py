import torch
from typing import Optional

def fn(inp: torch.Tensor, weight: torch.Tensor, bias: Optional[torch.Tensor] = None, running_mean=None, running_var=None):
    with torch.cuda.amp.autocast(enabled=True, dtype=torch.half):
        return torch.nn.functional.batch_norm(inp, running_mean, running_var, weight, bias)

fn_s = torch.jit.script(fn)

inp = torch.rand((5, 3, 224, 224), dtype=torch.float).cuda()
weight = torch.rand((3), dtype=torch.float).cuda()
bias = torch.rand((3), dtype=torch.float).cuda()
running_mean = torch.rand((3), dtype=torch.float).cuda()
running_var = torch.rand((3), dtype=torch.float).cuda()

print("bias is none")
fn_s(inp, weight, None, running_mean, running_var)

print("bias is not none")
fn_s(inp, weight, bias, running_mean, running_var)

