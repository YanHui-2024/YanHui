import torch
from typing import Dict

def fn(key: str, dictionary: Dict[str, torch.jit.ScriptModule]):
    return dictionary[key]

torch.jit.script(fn)