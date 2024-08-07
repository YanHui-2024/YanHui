class MyModule(torch.nn.Module):
    # __constants__ = ['sub'] # adding just this line works
    def __init__(self, sub):
        super(MyModule, self).__init__()
        # either of the following lines fails
        self.add_module('sub', sub)
        # or
        self.sub = sub
    
    def forward(self, x):
        x = x.relu()
        if self.sub is not None:
            x = self.sub(x)
        return x+1

m1 = MyModule(torch.nn.ReLU())
m2 = MyModule(None)
print(m1(torch.rand(5)))
print(m2(torch.rand(5)))
print(torch.jit.script(m1).code) # succeeds
print(torch.jit.script(m2).code) # fails