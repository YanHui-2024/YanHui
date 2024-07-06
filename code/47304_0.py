import torch
device = torch.device('cuda')
x = torch.tensor([0.],dtype=torch.double,requires_grad=True,device=device)

class Model(torch.nn.Module):
    def forward(self, x):
        return torch.exp(x**2)

# this code errors out
model_jit = torch.jit.script(Model()).to(device).double()
for j in range(3):
    out = model_jit(x)
    _ = torch.autograd.grad(out, x)
