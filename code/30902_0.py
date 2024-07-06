import sys
import time
import psutil

import torch
from torch import nn
from torchvision import models

def get_vms():
    return psutil.Process().memory_info().vms

def sync_cuda():
    t0 = time.time()
    torch.cuda.synchronize('cuda')
    print(f"cuda sync took {time.time() - t0:.3f} second(s)")

if __name__ == '__main__':
    device = sys.argv[1]

    net = models.inception_v3(pretrained=True, aux_logits=True)
    net = torch.jit.script(net)
    if device == 'cuda':
        sync_cuda()

    net = net.to(device).eval()
    input = torch.randn(1,3,299,299,requires_grad=False).to(device)

    if device == 'cuda':
        sync_cuda()

    out0 = None
    with torch.no_grad():
        for i in range(30):
            t0 = time.time()
            pred = net(input)
            if out0 is not None and not torch.allclose(out0.logits, pred.logits):
                print(f"{i}: logits aren't allclose; abs-sum={(out0.logits - pred.logits).abs().sum()}")
            print(f"{i} vms:{get_vms() / 1024/1024/1024:.3f}Gb seconds/iter={time.time() - t0:.3f}")
            out0 = pred