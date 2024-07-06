class Root(torch.nn.Module):
    def __init__(self):
        super(Root, self).__init__()
        self.register_buffer('buffer1', torch.ones(2, 2))

    def forward(self, foo):
        return foo
ScriptRoot = torch.jit.script(Root) #  as opposed to Root()