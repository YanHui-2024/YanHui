@torch.jit.script
def fn(x):
    # type: (List[str])
    del x[0]		# torch.jit.frontend.UnsupportedNodeError: del statements aren't supported: