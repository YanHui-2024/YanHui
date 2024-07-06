@torch.jit.interface
class RequestedIFace(object):
    def one(self, x, y):
        # type: (Tensor, Tensor) -> Tensor
        pass

    def two(self, x):
        # type: (Tensor) -> Tensor
        pass
      
orig_module = torch.jit.script(MyModel()) # or trace, or load
frozen_module = freeze(orig_module, iface=RequestedIFace)
frozen_module.two(x,y) # works