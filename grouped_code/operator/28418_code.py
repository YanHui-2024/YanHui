import torch
import torch.nn as nn

torch.jit.script(nn.RNN(32, 64, 1))