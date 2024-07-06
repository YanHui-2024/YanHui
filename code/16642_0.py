
import torch
import torch.nn as nn
def test_fuse_batch_norm():
	
    class ResLike(torch.jit.ScriptModule):
        def __init__(self, optimize=True):
            super(ResLike, self).__init__(optimize)
            self.bn = nn.BatchNorm2d(16)
    
        @torch.jit.script_method
        def forward(self, x, y):
            return y + torch.relu(self.bn(x))
    
    model = ResLike().cuda()
    model_noopt = ResLike(optimize=False).cuda()
    model_noopt.load_state_dict(model.state_dict())
    x = torch.randn(2, 16, 8, 8, device='cuda')
    y = torch.randn(2, 16, 8, 8, device='cuda')
    with torch.no_grad():
        out = model(x, y)
        graph = model.graph_for(x, y)
        rep = str(graph)
    
        out_noopt = model_noopt(x, y)
        rep_noopt = str(model_noopt.graph_for(x, y))
        x = x.half()
        y = y.half()
        out_noopt = model_noopt(x,y)
        print("no jit", out_noopt.abs().max())
        out_opt = model(x,y)
        print("jit", out_opt.abs().max())
    

if __name__ == "__main__":
    test_fuse_batch_norm()