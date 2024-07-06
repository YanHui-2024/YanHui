", line 507, in build_UnaryOp                  
    raise NotSupportedError(err_range, "unsupported unary operator: " + op.__name__)                              
torch.jit.frontend.NotSupportedError: unsupported unary operator: Invert
:                           
at test.py:9:18                                                                                                   
    def forward(self, x):   
        return x[~self.bool_tensor]                                              
                 ~~~~~~~~~~ <--- HERE