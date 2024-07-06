import torch

class IndexPutModel(torch.nn.Module):
    def forward(self, x, update):
        x[..., torch.tensor([2, 1, 3]), 2:4] += update
        return x

x = torch.randn(3, 4, 5, 6, 7)
update = torch.randn(3, 1, 1, 3, 2)

trace_graph, torch_out, inputs_states = torch.jit.get_trace_graph(IndexPutModel(), (x, update), _force_outplace=True, _return_inputs_states=True)

print(trace_graph)