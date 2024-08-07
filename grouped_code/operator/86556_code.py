import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(
            1, 2, kernel_size=(2,4), stride=2, padding=2, dilation=(2,1),
        )
        
    def forward(self, i0):
        x = self.conv1(i0)
        o0 = torch.max(x, i0)
        o1 = torch.clip(x, -1.5, 1.5)
        return o0, o1



inp = {
    'i0': torch.zeros((1,1,1,2), dtype=torch.float32),
}

mod = MyModule()

out = mod(**inp)
print(f'{out = }')

exported = torch.jit.trace(mod, list(inp.values()))
exported = torch.jit.optimize_for_inference(exported)

eout = exported(**inp) # <-- wrong results here
print(f'{eout = }')

eqs = []
for x, y in zip(out, eout):
    eqs.append(torch.allclose(x, y))
print(eqs)
assert all(eqs)