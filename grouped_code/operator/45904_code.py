model = torch.nn.MaxPool1d(2, stride=1, return_indices=True)
torch.jit.script(model)