import torch
from torch import jit
import torch.nn as nn
from torch.autograd import Variable

class TestNet(nn.Module):
    def __init__(self):
        super(TestNet, self).__init__()
        self.net1 = nn.Linear(100, 200)
        self.net2 = nn.Linear(200, 1)
        self.sigmoid = nn.Sigmoid()
        self.ReLU = nn.ReLU(inplace=False)
        self.drop = nn.Dropout(0.5)
               
    def forward(self, V):
        return self.sigmoid(self.net2(self.drop(self.ReLU(self.net1(V))))).squeeze() 


use_cuda = True
net = TestNet()
criterion = nn.BCELoss()
if use_cuda:
    net.cuda()
    criterion.cuda()
    V = Variable(torch.randn(100, 100)).cuda()
    label = Variable(torch.randn(100)).cuda()
else:
    V = Variable(torch.randn(100, 100))
    label = Variable(torch.randn(100))

net.train()
fwd = jit.compile(net.forward)
for i in range(0,1000000):
    r = fwd(V)
    err = criterion(r, label)
    err.backward()   
