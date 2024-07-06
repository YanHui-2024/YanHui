import torch

torch.jit.annotations.parse_type_line('# type: __import__("os").system("ls") -> 234', None, 1)