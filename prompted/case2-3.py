import torch
import torch.nn as nn
import numpy as np

class NumpyModel(nn.Module):
    def __init__(self):
        super(NumpyModel, self).__init__()
        self.linear = nn.Linear(10, 10)

    def custom_function(self, x):
        # Convert tensor to numpy array, perform an operation and convert back to tensor
        x_np = x.numpy()
        x_np = np.exp(x_np)
        return torch.from_numpy(x_np)

    def forward(self, x):
        x = self.linear(x)
        x = self.custom_function(x)  # Using a custom function that involves numpy
        return x

model = NumpyModel()

# Using the scripting method for conversion will fail
try:
    scripted_model = torch.jit.script(model)
except Exception as e:
    print(f"Scripting failed: {e}")

