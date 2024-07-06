torch.jit.frontend.NotSupportedError: unsupported binary operator: LShift:
  File "example.py", line 5
@jit.script
def func(inp):
    return inp<<1
              ~~ <--- HERE