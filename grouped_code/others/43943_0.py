class MyModule(torch.nn.Module):
    def forward(self, x):
        x = x[:, :, [0, 1]]
        return x
# will get torch.jit.frontend.NotSupportedError: slicing multiple dimensions with sequences not supported yet: