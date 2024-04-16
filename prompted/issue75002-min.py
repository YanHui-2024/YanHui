import torch

def fn(inp, weight, bias=None):
    with torch.cuda.amp.autocast(enabled=True, dtype=torch.half):
        return torch.nn.functional.conv2d(inp, weight, bias, 1, 3)

fn_s = torch.jit.script(fn)

inp = torch.rand((5, 3, 224, 224), dtype=torch.float).cuda()
weight = torch.rand((3, 3, 7, 7), dtype=torch.float).cuda()
bias = torch.rand((3), dtype=torch.float).cuda()

fn_s(inp, weight, bias)

