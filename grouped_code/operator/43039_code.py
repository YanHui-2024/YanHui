import torch
import torchvision
from torch.utils import mkldnn as mkldnn_utils

# An instance of your model.
model = torchvision.models.resnet18(pretrained=True)
# Switch the model to eval model
model.eval()

model = mkldnn_utils.to_mkldnn(model)

# An example input you would normally provide to your model's forward() method.
example = torch.rand(1, 3, 224, 224).to_mkldnn()

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)

# Save the TorchScript model
traced_script_module.save("traced_resnet_model.pt")