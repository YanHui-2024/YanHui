import torch
import torchvision
def foo(x, y):
    return 2 * x + y
traced_foo = torch.jit.trace(foo, (torch.rand(3), torch.rand(3)))
print(traced_foo)
print(isinstance(traced_foo, torch.jit.ScriptModule))
print(isinstance(traced_foo, torch.jit.TracedModule))

traced_net = torch.jit.trace(torchvision.models.resnet18(),
                             torch.rand(1, 3, 224, 224))
print(type(traced_net))
print(isinstance(traced_net, torch.jit.TracedModule))
print(isinstance(traced_net, torch.jit.ScriptModule))