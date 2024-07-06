import torch
class ConstantTensor(torch.jit.ScriptModule):
    def __init__(self):
        super(ConstantTensor, self).__init__(optimize=False)