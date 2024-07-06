class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.x = {True: 1}

model = MyModule()
model_s = torch.jit.script(model)