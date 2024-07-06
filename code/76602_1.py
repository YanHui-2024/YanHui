RuntimeError: 
Only ModuleList, Sequential, and ModuleDict modules are subscriptable:
  File "<ipython-input-3-6fafe8d819b8>", line 12
    def forward(self, x):
        return x + self.params["hi"] + self.params["bye"]
                   ~~~~~~~~~~~~~~~~ <--- HERE