import torch


class MyModule(torch.nn.Module):
    def forward(self, x):
        return torch.split(x, x.size(1))


m = MyModule()
x = torch.randn(1, 2, 3, 4)

# ok to run the model
m(x)

# fail to trace it
print(torch.jit.trace(m, x))