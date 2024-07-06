import torch
import torchvision

# An instance of your model.
model = torchvision.models.inception_v3(pretrained=True)

# An example input you would normally provide to your model's forward() method.
example = torch.rand(1, 3, 299, 299)

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)