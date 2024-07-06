@torch.jit.script
class BoundingBoxList:
    def __init__(self, bbox, image_size: Tuple[int, int], mode: str):
        self.size = image_size
        self.mode = mode
        self.bbox = bbox

class Foo(torch.jit.ScriptModule):
    def __init__(self, bbox):
        super(Foo, self).__init__(False)
        self.words = torch.jit.Attribute(bbox, BoundingBoxList)

    @torch.jit.script_method
    def forward(self, input):
        # type: (str) -> int
        return self.words.convert("xyxy")

f = Foo(BoundingBoxList(torch.rand(3, 4), (2, 3), "xyxy"))