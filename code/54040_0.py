import torch
@torch.jit.script
def t(input, bias):
  return torch.nn.functional.relu(input + bias)
input = torch.randn(2, 8, requires_grad=True)
bias = torch.randn(8, requires_grad=False)    # bias does NOT require grad
o = t(input, bias)
o.sum().backward()
o = t(input, bias)
o.sum().backward()
o = t(input, bias)
o.sum().backward()

print(t.graph_for(input, bias))
bwd_graph = list(list(t.get_debug_state().execution_plans.values())[0].code.grad_executor_states()[0].execution_plans.values())[0].graph
print(bwd_graph)