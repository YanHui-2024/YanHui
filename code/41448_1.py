torch.jit.frontend.UnsupportedNodeError: DictComp aren't supported:
  File "main_test.py", line 6
    def forward(self):
        x = {i: i for i in range(2)}
            ~ <--- HERE
        return x