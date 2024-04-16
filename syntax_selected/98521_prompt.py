import torch
import torchvision.transforms.functional as F
from typing import Union


def to_tuple(v: Union[int, tuple[int, int]]) -> tuple[int, int]:
    """Converts int or tuple to tuple of ints."""
    if torch.jit.isinstance(v, int):
        return v, v
    else:
        return v


def pad(img: torch.Tensor, new_size: Union[int, tuple[int, int]]) -> torch.Tensor:
    new_size = to_tuple(new_size)
    old_size = img.shape[-2:]
    pad_size = (torch.tensor(new_size) - torch.tensor(old_size)) / 2
    padding = torch.cat((torch.floor(pad_size), torch.ceil(pad_size)))
    padding[padding < 0] = 0
    padding = [int(x) for x in padding]
    return F.pad(img, padding=padding, padding_mode="edge")


out = torch.jit.script(pad)

# Another test program

