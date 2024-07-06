@torch.jit.script 
def mm(a,b): 
    a.fmod_(b) 
    return a 