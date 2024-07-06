import torch
from typing import List
class Boxes():
    def __init__(self, tensor):
        self.tensor = tensor
    @classmethod
    def cat(cls, box_lists: List):
        return cls(torch.cat([x.tensor for x in box_lists]))

def f(t: torch.Tensor):
    b = Boxes(t)
    c = Boxes(torch.tensor([3, 4]))
    return Boxes.cat([b, c])

if __name__ == "__main__":
    f_script = torch.jit.script(f)