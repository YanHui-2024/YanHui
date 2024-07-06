import torch
from torch import nn
import numpy as np

class Demo(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v, inds = x.sort(descending=True)
        # inds = x.argsort(descending=True)
        return inds

if __name__ == "__main__":
    input_tensor = torch.range(20, 80)
    demo = Demo()
    out = demo(input_tensor)
    torch.onnx.export(demo, input_tensor, "debug.onnx", verbose=True,
                        input_names=['data'],
                        opset_version=11,
                        do_constant_folding=True,
                        dynamic_axes={'data':{0:'batch'}})