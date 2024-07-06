model = torchvision.models.detection.keypoint_rcnn.keypointrcnn_resnet50_fpn(pretrained=True, min_size=200, max_size=300)
model.eval()
script_module = torch.jit.script(model)
torch._C._freeze_module(script_module._c)