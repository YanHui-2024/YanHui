import torch
import torch.jit

def fn1(x, y):
    r = torch.rand_like(y)
    return r*x

def traceandprint(f, inputs):
   traced_fn = torch.jit.script(f, inputs)
   out = traced_fn(*inputs)
   print(traced_fn.graph_for(*inputs))
   return traced_fn, out


x=torch.ones(5,5, device="cuda")
y=torch.ones(5, device="cuda")
fn, out = traceandprint(fn1, (x,y))
print(fn(x,y))
print(fn1(x,y))