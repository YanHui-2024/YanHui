with torch.jit.fuser("fuser2", force_fusion=True):
    fused_op = torch.jit.script(op)