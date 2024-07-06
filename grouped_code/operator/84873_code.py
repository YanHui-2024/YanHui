class Model(nn.Module):
    def __init__(self):
        super().__init__()
    
    def f(self, x):
        return x
    
module = Model()
traced_module = torch.jit.trace_module(module, {"f": torch.randn(3)})
torch.jit.freeze(traced_module.eval(), preserved_attrs=["f"])