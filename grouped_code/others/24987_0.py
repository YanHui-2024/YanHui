@torch.jit.ignore
class MyScriptClass(object):
    def unscriptable(self):
        return "a" + 200


class TestModule(torch.nn.Module):
    def __init__(self):
        super(TestModule, self).__init__()

    def forward(self, x):
        return MyScriptClass()

t = torch.jit.script(TestModule())