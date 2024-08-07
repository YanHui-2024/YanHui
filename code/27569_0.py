from tempfile import TemporaryFile

import torch
import torch.onnx
import torch.jit
from torch import nn, Tensor

print(f"PyTorch version is {torch.__version__}")

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.module = nn.Linear(
            in_features=8, out_features=4)
        self.module2 = nn.Linear(
            in_features=4, out_features=2)
       
    def forward(self, x: Tensor) -> Tensor:
        preout = self.module(x)
        out = self.module2(preout)
        return out


model = Model()
model = torch.jit.script(model)

dummy_input = torch.randn(3, 8)
dummy_output = model(dummy_input)

with TemporaryFile() as temp:
    torch.onnx.export(model=model, 
                      args=dummy_input, 
                      example_outputs=dummy_output,
                      f=temp, 
                      verbose=True)