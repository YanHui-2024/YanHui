if isinstance(foo, dict):
    for k, v in foo.items():
        assert isinstance(k, str)
        assert isinstance(v, Tensor)