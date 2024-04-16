import torch
import numpy as np
from torch import nn
torch.use_deterministic_algorithms(True)


class Foo(nn.Module):
    """Simple CNN model."""
    def __init__(self):
        super().__init__()                
        self.prepro = nn.Sequential(
            nn.Conv2d(3, 24, kernel_size=3, stride=1, padding="same"),
            nn.BatchNorm2d(24),
            nn.ReLU())
        
    def forward(self, x):
        return self.prepro(x)
    
# Random inputs
inputs = torch.randn([1, 3, 352, 224]).cuda()

# Create model and trace it
foo = Foo().eval().cuda()
foo = torch.jit.trace(foo, inputs)

# Add random bias to BatchNorm so it is not zero
params = foo.state_dict()
params['prepro.1.bias'] = torch.randn([24])
foo.load_state_dict(params)

out_foo = foo(inputs)
for i in range(2000):
    out_curr = foo(inputs)
    print(i, torch.equal(out_foo, out_curr))    
    assert torch.equal(out_foo, out_curr)    
