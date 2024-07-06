import torch
import torch.nn.functional as F

@torch.jit.trace(torch.zeros(1, 2, 3))
def dropout_test(x):
    x = torch.neg(x)
    return F.dropout(x)

dropout_test(torch.zeros(1, 2, 3, requires_grad=True))