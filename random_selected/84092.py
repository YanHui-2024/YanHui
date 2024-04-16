import torch

class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cv1 = torch.nn.Conv2d(3, 3, 5, 2, 1)

    def forward(self, x):
        x = self.cv1(x)
        return x

x = torch.randn(10, 3, 20, 20) * 2
m = MyModule().eval()
x = x.cuda()
m = m.cuda()

with torch.no_grad():
    print("outside result: ", torch.jit.trace(m, x))
    with torch.cuda.amp.autocast(enabled = True, dtype=torch.float16):
        print("inside result: ", torch.jit.trace(m, x))
