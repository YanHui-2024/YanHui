import torch

from typing import List

def on_tensor(a, b) -> List[torch.Tensor]:
    c = a.repeat_interleave(b)
    return [c, a, b]
on_tensor_s = torch.jit.script(on_tensor)

def functional(a, b) -> List[torch.Tensor]:
    c = torch.repeat_interleave(a, b)
    return [c, a, b]
functional_s = torch.jit.script(functional)

offs = torch.tensor([0, 0, 2, 5, 7], dtype=torch.int64)
lens = torch.tensor([0, 0, 5, 0, 4], dtype=torch.int64)

r1 = on_tensor(offs, lens)
r2 = on_tensor_s(offs, lens)
print("a.repeat_interleave(b)")
print(r1)
print(r2)
print(on_tensor_s.graph)

print()

print("repeat_interleave(a, b")
r3 = functional(offs, lens)
r4 = functional_s(offs, lens)
print(r3)
print(r4)
print(functional_s.graph)