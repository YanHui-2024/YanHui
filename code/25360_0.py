...

", line 504, in build_UnaryOp                                                                                     
    r = ctx.make_range(expr.lineno, expr.col_offset, expr.col_offset + len(op_token))                             
TypeError: object of type 'NoneType' has no len()