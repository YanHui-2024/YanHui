RuntimeError:                                                                                                                                                                                       
Unsupported operation: slicing tuples with a step isn't supported:                                
  File "a.py", line 19         
    def forward(self, x):                                                                         
        return self.x[::-1][0] + x                                                                                                                                                                  
               ~~~~~~~~~~~~ <--- HERE 