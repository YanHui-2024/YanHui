import torch
import torch.nn as nn

class LayerNormModule(nn.Module):
    def __init__(self):
        super(LayerNormModule, self).__init__()
        self.layer_norm = nn.LayerNorm(10)

    def forward(self, x):
        return self.layer_norm(x)

x = torch.randn(32, 10).cuda().half()
model = LayerNormModule().cuda().half()
y = model(x)

