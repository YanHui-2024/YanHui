import torch

class Model(torch.nn.Module):
        def __init__(self):
                super().__init__()
                self.l = torch.nn.LPPool2d(2, 3)
                self.n = torch.nn.LPPool2d(2, (7, 1)) # fails: Expected a value of type 'int' for argument 'kernel_size' but instead found type 'Tuple[int, int]'.

        def forward(self, x):
                o = []
                o.append(self.l(x))
                o.append(self.n(x)) # fails: Expected a value of type 'int' for argument 'kernel_size' but instead found type 'Tuple[int, int]'.
                o.append(torch.nn.functional.lp_pool2d(x, float(2), 3))
                o.append(torch.nn.functional.lp_pool2d(x, 2, 3)) # fails: Expected a value of type 'float' for argument 'norm_type' but instead found type 'int'.
                o.append(torch.nn.functional.lp_pool2d(x, float(2), (7, 1))) # fails: Expected a value of type 'int' for argument 'kernel_size' but instead found type 'Tuple[int, int]'.
                return o

model = Model()
x = torch.rand(1, 3, 7, 7)
print(*model(x), sep="\n") 
torch.jit.script(model)