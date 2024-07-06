RuntimeError: 
Only ModuleList, Sequential, and ModuleDict modules are subscriptable:
  File "test.py", line 12
    def forward(self, x):
        self.module_list[0]
        self.parameter_list[0]
        ~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
        return x