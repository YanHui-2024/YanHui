NotSupportedError: unsupported kind of augumented assignment: Mod:
  File "<ipython-input-5-dcecdbcf8ec0>", line 3
@torch.jit.script
def mm(a,b):
    a %= b
      ~~ <--- HERE
    return a