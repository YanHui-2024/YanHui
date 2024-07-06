class MyModule(torch.nn.Module):
    def forward(self) -> Any:
        if self.training:
            return 'xx'
        else:
            return {}