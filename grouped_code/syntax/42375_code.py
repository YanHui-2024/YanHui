class TestModule(torch.nn.Module):
    def __init__(self):
        super(TestModule, self).__init__()
        
    def forward(self, list_of_str: List[str]):
        return sorted(list_of_str)

m = TestModule()
m_scripted = torch.jit.script(m)
# gives runtime error
m_scripted(["str3", "str2", "str1"]) 