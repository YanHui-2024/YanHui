import torch

@torch.jit.script
def script_fn(x):
    return x

print('*****Script function*****')
print(type(script_fn))
print(isinstance(script_fn, torch._C.GraphExecutor))

@torch.jit.trace(torch.zeros(3, 3))
def trace_fn(x):
    return x

print('*****Traced function*****')
print(type(trace_fn))
print(isinstance(trace_fn, torch._C.GraphExecutor))

class ScriptModule(torch.jit.ScriptModule):
    @torch.jit.script_method
    def forward(self, x):
        return x
sm = ScriptModule()

print('*****Script module*****')
print(type(sm))
print(isinstance(sm, torch._C.GraphExecutor))

class TracedModule(torch.nn.Module):
    def forward(self, x):
        return x
tm = torch.jit.trace(torch.zeros(3, 3))(TracedModule())

print('*****Traced module*****')
print(type(tm))
print(isinstance(tm, torch._C.GraphExecutor))
