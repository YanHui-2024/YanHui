class TestModule(torch.nn.Module):
    def forward(self, x):
        return x.transpose(0,1)
    
class AnotherTestModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inner_module = TestModule()
        
    def forward(self, y):
        return self.inner_module(x=y)
    
module = AnotherTestModule()
trace_input = torch.ones([1,1])
traced_module = torch.jit.trace_module(module, dict(forward=(trace_input,)))
 
try:
    print('Original module')
    module(y=trace_input)
    print('Correct\n')
except RuntimeError as e:
    print(e, '\n')
 
try:
    print('Traced module')
    traced_module(y=trace_input)
    print('Correct\n')
except RuntimeError as e:
    print(e, '\n')
 
print('Traced module code')
print(traced_module.code)