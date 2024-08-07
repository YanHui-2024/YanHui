import torch                                                    
                                                                
@torch.jit.script                                               
def f(x):                                                       
    a, b, c, d = x.chunk(4, 1)                                  
    r = (a * b) + (c * d)                                       
    return x.sum(), r                                           
                                                                
x = torch.randn(2, 10, device='cuda', requires_grad=True)       
s, r = f(x)                                                     
grad_x, = torch.autograd.grad(s + r.sum(), x, create_graph=True)
grad_grad_x = torch.autograd.grad(grad_x.sum() + s + r.sum(), x)