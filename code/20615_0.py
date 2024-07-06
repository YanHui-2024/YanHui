@torch.jit.script
def fn(x):
    # type: (Dict[str, int])
    x.pop("hi")		# ok
    del x["hello"]	# torch.jit.frontend.UnsupportedNodeError: del statements aren't supported