@torch.jit.script
def format_str(s: str) -> str:
    return "This is my %s in template" % s