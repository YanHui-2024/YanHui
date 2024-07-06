from torch import nn

import torch


class Model(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, a):
        # type: (Tensor)

        # [batch_size, sequence_length] →
        # [batch_size, sequence_length]
        a = torch.nn.functional.relu(a)
        return a


if __name__ == "__main__":
    model = Model()
    model = torch.jit.script(model)