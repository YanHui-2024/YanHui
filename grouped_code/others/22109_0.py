@torch.jit.script_method
def forward(self, x):
    x = self.conv(x)
    return x
    x = self.bn(x)
    return F.relu(x, inplace=True)