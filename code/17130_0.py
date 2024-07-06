import torch


class DummyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Conv2d(1, 2, 3)

    def forward(self, x):
        return torch.mean(self.layer(x))


m = DummyModel()
traced = torch.jit.trace(m, torch.rand([1, 1, 100, 300]))
traced.save('dummy_model.pt')