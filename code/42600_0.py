class TestModule(torch.nn.Module):
    def __init__(self):
        super(TestModule, self).__init__()
        self.mod_a = create_placeholder_module(ModuleA)
        self.mod_b = create_placeholder_module(ModuleB)

    def init_params(self, inputs):
        if inputs.shape[0] == 1:
            self.mod_a = ModuleA(inputs.shape[1])  # Use input to create actual module
        elif inputs.shape[0] == 2:
            self.mod_b = ModuleB(inputs.shape[1])  # Use input to create actual module

    def forward(self, inputs):
        if inputs.shape[0] == 1:
            return self.mod_a(inputs)
        elif inputs.shape[0] == 2:
            return self.mod_b(inputs)

m = TestModule()
m.init_params(torch.randn(1, 3))  # only `self.mod_a` is initialized
m_scripted = torch.jit.script(m)

m_scripted(torch.randn(1, 3))  # behave as expected
m_scripted(torch.randn(2, 3))  # TODO: we want to throw error in this case