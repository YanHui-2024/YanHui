class MyModule(torch.nn.Module):
    def forward(self) -> Any:
        return 'xx' if self.training else {}