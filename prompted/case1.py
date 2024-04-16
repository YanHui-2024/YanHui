import torch

# A simple PyTorch model that adds two tensors
class AddModel(torch.nn.Module):
    def forward(self, x, y):
        return x + y

# Create an instance of the PyTorch model and test it
model = AddModel()
x = torch.ones((2, 2))
y = torch.ones((2, 2))
z = model(x, y)
print(z)

# Convert the PyTorch model to TorchScript
scripted_model = torch.jit.script(model)

# Test the TorchScript-converted model
z1 = scripted_model(x, y)
print(z1)

print(torch.equal(z, z1))

