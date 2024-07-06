import torch.nn as nn
import torch.jit as jit

class TestModule(jit.ScriptModule):
  def __init__(self):
    super().__init__()
    self.linear = nn.Linear(16, 16)


m = TestModule()
print(m.linear.in_features)