import torch

class BatchNormModel(torch.jit.ScriptModule):
    def __init__(self):
        super(BatchNormModel, self).__init__(optimize=False)
        self.bn = torch.nn.BatchNorm1d(10)

    @torch.jit.script_method
    def forward(self, x):
        return self.bn(x)


model = BatchNormModel()
model.eval()
model.cuda()
model.save("/tmp/bn_gpu.pt")