@torch.jit.script
class Timebase:
    def __init__(
        self,
        numerator,  # type: int
        denominator,  # type: int
    ):
        # type: (...) -> None
        self.numerator = numerator  # type: int
        self.denominator = denominator  # type: int