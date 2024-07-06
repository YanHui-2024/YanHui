import torch
import torch.nn as nn
from typing import List

class ModelWithInputAsListOfTensor(nn.Module):
    def __init__(self):
        super(ModelWithInputAsListOfTensor, self).__init__()
        self.x = 2

    def forward(self, x: List[torch.Tensor]) -> List[torch.Tensor]:
        # print("Receiving type", type(x), len(x), type(x[0]))
        # print("Receiving list of tensor", len(x), type(x[0]))
        for each in x:
            each *= self.x
        return x

model = nn.Sequential(
    ModelWithInputAsListOfTensor(),
    ModelWithInputAsListOfTensor()
)

# Original model
test_input: List[torch.Tensor] = [torch.ones((2, 2)), torch.ones((3, 3)), torch.ones((4, 4))]
res = model(test_input)
print(res)

# Scripted model
scripted_model = torch.jit.script(model)
print(scripted_model)

print("---------------------")

# Input as typing.List[torch.Tensor]
test_input: List[torch.Tensor] = [torch.ones((2, 2)), torch.ones((3, 3)), torch.ones((4, 4))]
res = scripted_model(test_input)
print(res)

print("---------------------")

# Input as torch.jit.annotate(List[torch.Tensor])
test_input = torch.jit.annotate(List[torch.Tensor], [torch.ones((2, 2)), torch.ones((3, 3)), torch.ones((4, 4))])
res = scripted_model(test_input)
print(res)