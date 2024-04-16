import torch
import torch.nn as nn

class UnsupportedModel(nn.Module):
    def __init__(self):
        super(UnsupportedModel, self).__init__()
        self.linear = nn.Linear(10, 10)

    def forward(self, x):
        # Using Python's built-in len() function, which is unsupported in TorchScript
        input_length = len(x)

        # Using a list comprehension with the unsupported len() function
        output = [self.linear(x[i]) for i in range(input_length)]

        # Stack the list of tensors back to a tensor, this part is supported
        return torch.stack(output)

model = UnsupportedModel()

# Using the scripting method for conversion will fail
try:
    scripted_model = torch.jit.script(model)
except Exception as e:
    print(f"Scripting failed: {e}")

