```
    if not PY2 and py_args.kw_defaults:
        raise NotSupportedError(ctx_range, _vararg_kwarg_err)