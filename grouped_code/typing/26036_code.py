@torch.jit.script
def fn(x: List[bool]):
    x.clear()

fn([True, False])