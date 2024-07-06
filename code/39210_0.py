from typing import List

import torch as th

class Mod(th.nn.Module):                                                                                                                                                                                                                    
    def __init__(self):
        super().__init__()

    def forward(self, s: str, l: List[str]):
        return l.index(s)

mod = Mod()
th.jit.script(mod)