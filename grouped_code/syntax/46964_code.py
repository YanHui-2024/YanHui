# Dockerfile
FROM python:3.6-slim-buster
USER root
WORKDIR /root
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install torch==1.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
COPY a.py /
RUN python3 /a.py

# a.py:
import torch
from torch import nn

class A(nn.Module):
    dim: torch.jit.Final[int] = 4

    def __init__(self):
        super().__init__()
        self.l = nn.Linear(10, 10)

    def forward(self, x):
        return self.l(x)


class B(nn.Module):
    def __init__(self):
        super().__init__()
        self.a = A()

    def forward(self, x):
        return self.a(x) + self.a.dim

b = B()
b = torch.jit.script(b)