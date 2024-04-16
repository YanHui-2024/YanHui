import torch
import torch.nn as nn

class DynamicModel(nn.Module):
    def __init__(self):
        super(DynamicModel, self).__init__()
        self.linear = nn.Linear(10, 10)

    def forward(self, x):
        num_iterations = int(x[0, 0].item())

        # Data-dependent loop
        for _ in range(num_iterations):
            x = self.linear(x)
            x = torch.relu(x)

        return x

model = DynamicModel()

# Using the tracing method for conversion
input_tensor = torch.randn(1, 10)
traced_model = torch.jit.trace(model, input_tensor)

# Test the models
test_input = torch.randn(1, 10)
test_input[0, 0] = 3  # Set the number of iterations
output1 = model(test_input)
output2 = traced_model(test_input)
print("Original PyTorch model output:", output1)
print("Traced TorchScript model output:", output2)

