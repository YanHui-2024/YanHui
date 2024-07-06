import torch

from typing import Dict

class TestModule(torch.nn.Module):
    def __init__(self):
        super(TestModule, self).__init__()

    def forward(self, dict_input):
       return dict_input['x']

input_1 = {'x': torch.tensor(1)}
input_2 = {'x': torch.tensor(2), 'y': torch.tensor(3)}

m = TestModule()
m_traced = torch.jit.trace(m, (input_1, ))
print(m_traced.graph)
print(m_traced(input_1))
print(m_traced(input_2))