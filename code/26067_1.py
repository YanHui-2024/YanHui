RuntimeError: 
module has no attribute 'sub':
at <ipython-input-33-82f6eee81215>:12:11
    def forward(self, x):
        x = x.relu()
        if self.sub is not None:
           ~~~~~~~~ <--- HERE
            x = self.sub(x)
        return x+1