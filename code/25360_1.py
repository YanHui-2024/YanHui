import torch as th                                                                                                
                                                                                                                  
class TestMod(th.nn.Module):                                                                                      
    def __init__(self):                                                                                           
        super().__init__()                                                                                        
        self.register_buffer("bool_tensor", th.zeros(3,).bool())                                                  
                                                                                                                  
    def forward(self, x):                                                                                         
        return x[~self.bool_tensor]                                                                               
                                                                                                                  
mod = TestMod()                                                                                                   
smod = th.jit.script(mod)