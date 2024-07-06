for fuser in ["fuser1", "fuser2"]:
    for rq in [True, False]:
        c = torch.jit.fuser(fuser)
        c.__enter__()

        def ratio_iou(x1, y1, w1, h1, x2, y2, w2, h2):
            xi = torch.max(x1, x2)                                  # Intersection left
            yi = torch.max(y1, y2)                                  # Intersection top
            wi = torch.clamp(torch.min(x1+w1, x2+w2) - xi, min=0.)  # Intersection width
            hi = torch.clamp(torch.min(y1+h1, y2+h2) - yi, min=0.)  # Intersection height
            area_i = wi * hi                                        # Area Intersection
            area_u = w1 * h1 + w2 * h2 - wi * hi                    # Area Union
            return area_i / torch.clamp(area_u, min=1e-5)           # Intersection over Union

        ratio_iou_scripted = torch.jit.script(ratio_iou)

        x1, y1, w1, h1, x2, y2, w2, h2 = torch.randn(8, 100, 1000, device='cuda', requires_grad=not rq).exp()

        for i in range(10):
            ratio_iou_scripted.graph_for(x1, y1, w1, h1, x2, y2, w2, h2)
        #print(ratio_iou_scripted.graph_for(x1, y1, w1, h1, x2, y2, w2, h2))

        x1, y1, w1, h1, x2, y2, w2, h2 = torch.randn(8, 100, 1000, device='cuda', requires_grad=rq).exp()
        print(fuser, x1.requires_grad, ratio_iou_scripted(x1, y1, w1, h1, x2, y2, w2, h2).requires_grad)