import torch
from torch import nn

torch.use_deterministic_algorithms(True)

class CustomModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.ConvTranspose2d(3, 32, kernel_size=3, stride=1, padding=1),
            nn.LeakyReLU(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Linear(32 * 16 * 16, 256),
            nn.LayerNorm(256),
            nn.LeakyReLU(),
            nn.Linear(256, 10),
        )

    def forward(self, x):
        x = self.layers[:3](x)
        x = x.view(x.size(0), -1)
        x = self.layers[3:](x)
        return x

def main():
    inputs = torch.randn(1, 3, 32, 32).cuda()
    model = CustomModel().eval().cuda()
    model = torch.jit.trace(model, inputs)

    # Modify model's parameters after tracing
    params = model.state_dict()
    params['layers.4.bias'] = torch.randn(256)
    model.load_state_dict(params)

    out_initial = model(inputs)
    for i in range(100):
        out_current = model(inputs)
        print(i, torch.equal(out_initial, out_current))
        assert torch.equal(out_initial, out_current)

if __name__ == "__main__":
    main()

