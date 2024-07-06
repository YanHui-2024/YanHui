Expected type hint for result of tolist():
def to_list_missing_type_annotation(x):
    # type: (torch.Tensor) -> List[float]
    li = x.tolist()
         ~~~~~~~~~ <--- HERE
    return li