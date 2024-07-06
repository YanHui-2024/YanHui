>>> import torch
>>> torch.save(torch.tensor([1., 2., 3.]), "tensor.pt")
>>> torch.load("tensor.pt")
tensor([1., 2., 3.])