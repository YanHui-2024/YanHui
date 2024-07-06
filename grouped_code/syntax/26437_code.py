_GoogLeNetOutputs = namedtuple('GoogLeNetOutputs', ['logits', 'aux_logits2', 'aux_logits1'])
def fn(x):
    # type: (Tensor) -> _GoogLeNetOutputs
    return _GoogleNetOutputs(x, x, x)

print(torch.jit.annotations.get_signature(fn))