class MyModule(nn.Module):
    def forward(self):
        x = {i: i for i in range(2)}
        return x

model = MyModule()
model_s = torch.jit.script(model)