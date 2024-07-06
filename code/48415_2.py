import torch

class SampleNet(torch.nn.Module):
    def __init__(self):
        super(SampleNet, self).__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        return self.linear(x)
    
m = torch.jit.script(SampleNet())
torch.jit.save(m, 'non/existent/path/model.pth')
# or torch.save(m, 'non/existent/path/model.pth') for a comparison