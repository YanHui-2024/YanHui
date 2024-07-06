import torch
import timm.models.efficientnet
model = timm.create_model('mixnet_m', pretrained=False, scriptable=True)
model.to(device="cuda", dtype=torch.float32)
jit_model = torch.jit.script(model).eval()

# This line causes the failure.
jit_model = torch.jit.freeze(jit_model)

x = torch.rand((1, 3, 224, 224), device="cuda")
for i in range(10):
    print(f"Begin {i}")
    jit_model(x)