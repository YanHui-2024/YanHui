class TestModule(torch.nn.Module):
    def forward(self, x: torch.Tensor, k: Optional[int]):
        return x

m = TestModule()
gm = torch.fx.symbolic_trace(m)
scripted_gm = torch.jit.script(gm)