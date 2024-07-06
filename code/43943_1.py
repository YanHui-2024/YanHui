class MyModule(torch.nn.Module):
    def forward(self, x):
        x = x[:, :].index_select(2, torch.tensor([0, 1]))
        # or
        idx = torch.tensor([0, 1])
        x = x[:, :, idx]
        return x