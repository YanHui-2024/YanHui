import torch
from typing import Final
net = torch.nn.Sequential(torch.nn.Conv2d(3, 64, (3, 3), 1, 1, bias=False),
                                      torch.nn.BatchNorm2d(64),
                                      torch.nn.PReLU(64)).cuda().eval()
img = torch.randn(3, 3, 112,112).cuda()
with torch.cuda.amp.autocast(True):
    net = torch.jit.trace(net, img, check_trace=False)
    net = torch.jit.freeze(net)
print(net.graph)
feature = net(img)  # forward pass
