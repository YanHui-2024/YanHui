import torch
import torch.nn as nn

class DynamicModel(nn.Module):
    def __init__(self):
        super(DynamicModel, self).__init__()
        self.linear1 = nn.Linear(10, 20)
        self.linear2 = nn.Linear(20, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.relu(x)

        # Data-dependent control flow
        if x.sum() > 0:
            x = self.linear2(x)
        else:
            x = -self.linear2(x)

        return x

model = DynamicModel()

# Using the tracing method for conversion
input_tensor = torch.randn(1, 10)
traced_model = torch.jit.trace(model, input_tensor)

# Test the models
test_input = torch.randn(1, 10)
output1 = model(test_input)
output2 = traced_model(test_input)
print("Original PyTorch model output:", output1)
print("Traced TorchScript model output:", output2)

