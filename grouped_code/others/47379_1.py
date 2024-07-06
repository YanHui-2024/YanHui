RuntimeError: 
Python builtin <built-in method _is_tracing of PyCapsule object at 0x7fd9ad2d8e70> is currently not supported in Torchscript:
  File "/torch/jit/_trace.py", line 979
    code with ``torch.jit.trace``) and ``False`` otherwise.
    """
    return torch._C._is_tracing()
           ~~~~~~~~~~~~~~~~~~~~ <--- HERE
'is_tracing' is being compiled since it was called from 'A.forward'
  File "a.py", line 20
    def forward(self, x): 
        if torch.jit.is_scripting() or not torch.jit.is_tracing():
           ~~~~~~~~~~~~~~~~~~~~~~ <--- HERE                                                       
            return x + 1
        else:   