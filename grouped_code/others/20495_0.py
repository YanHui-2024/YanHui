        class A(torch.jit.ScriptModule):
            def __init__(self):
                super(A, self).__init__()

            @torch.jit.script_method
            def forward(self, x):
                return x + self.whatisgoingon

        class B(A):
            def __init__(self):
                super(B, self).__init__()
            @torch.jit.script_method
            def bar(self, x):
                return x * x 
        
        A()