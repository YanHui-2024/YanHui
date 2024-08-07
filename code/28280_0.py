import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.register_buffer('a', torch.zeros(10))
        
    def forward(self, inputs):
        return self.non_scriptable(inputs)
    
    @torch.jit.ignore
    def non_scriptable(self, inputs):
        print(self.a.device)
        return inputs * self.a


# Not scripted: normal behaviour
m = Model()
m = m.to('cuda')
m(torch.zeros(10).to('cuda'))

# Scripted: fails
m = Model()
m = torch.jit.script(m)
m = m.to('cuda')
print(m.a.device)  # prints cuda
m(torch.zeros(10).to('cuda'))  # fails because m.a is on cpu inside non_scriptable