import torch
import io
from typing import List
import torch.utils.collect_env
torch.utils.collect_env.main()

class OrderModuleShort(torch.nn.Module):
    def forward(self, arg: List[torch.Tensor]):
        return [(arg[1],), (arg[0].argmax(),)]

class OrderModuleLong(torch.nn.Module):
    def forward(self, long_arg_name: List[torch.Tensor]):
        return [(long_arg_name[1],), (long_arg_name[0].argmax(),)]

def evaluate(cls):
    om = cls()
    sm = torch.jit.script(om)
    print(sm.code)
    print(sm.graph)
    buffer = io.BytesIO()
    torch.jit.save(sm, buffer)
    buffer.seek(0)
    lm = torch.jit.load(buffer)

    for name, mod in [
            ("original", om),
            ("scripted", sm),
            ("loaded", lm),
        ]:
        try:
            mod([torch.zeros(0)])
        except Exception as exn:
            print()
            print(name)
            print(exn)


print("---short:")
evaluate(OrderModuleShort)
print()
print("---long:")
evaluate(OrderModuleLong)