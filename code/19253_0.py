def pow_0(self,
          exponent: float):
    def backward(grad_output):
        grad_self = torch.where(torch.tensor(exponent == 0.0), torch.zeros_like(self), grad_output * exponent * torch.pow(self, exponent - 1))
        return grad_self, None
    return torch.pow(self, exponent), backward