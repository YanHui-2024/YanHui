@torch.jit.dataclass
class Normal:
    mu: Tensor
    sigma: Tensor

    def log_prob(self, value: Tensor) -> Tensor:
        ...