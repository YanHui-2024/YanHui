import torch
import torchvision

resnet = torchvision.models.resnet18()
sample_image = torch.randn(1, 3, 224, 224)
resnet_jit = torch.jit.trace(resnet, sample_image)

features = resnet_jit(sample_image)
print features
