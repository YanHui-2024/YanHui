import torch

torch._C._jit_override_can_fuse_on_cpu(True)

@torch.jit.script
def box_iou(box1, box2, eps:float=1e-5):
    # box1: [N, 4], box2: [M, 4]
    x1, y1, w1, h1 = box1.unsqueeze(1).unbind(2)
    x2, y2, w2, h2 = box2.unbind(1)

    xi = torch.max(x1, x2)  # Intersection
    yi = torch.max(y1, y2)

    wi = torch.clamp(torch.min(x1 + w1, x2 + w2) - xi, min=0)
    hi = torch.clamp(torch.min(y1 + h1, y2 + h2) - yi, min=0)
    return wi, hi

box_iou(torch.rand(4, 4), torch.rand(5, 4))
print(box_iou.graph_for(torch.rand(4, 4), torch.rand(5, 4)))