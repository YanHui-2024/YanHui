import torch                
                            
def pyfn(x):                
    raise RuntimeError('eh')
                            
                            
@torch.jit.script           
def f(x):                   
    return pyfn(x)          
                            
f(torch.randn(2, 2))        