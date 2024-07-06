import torch
class Model(torch.jit.ScriptModule):
    def __init__(self):
        super(Model, self).__init__()

    @torch.jit.script_method
    def forward(self, x_list_list):
        # type: (List[List[Tensor]]) -> Tensor

        return x_list_list[0][0]


m = Model()
m.save("./model.pt")