import torch
from typing import List
def simple_split(txt: str) -> List[str]:
	return txt.split()
ss = simple_split
jit_ss = torch.jit.script(ss)
ss('simple     split example') == jit_ss('simple     split example')