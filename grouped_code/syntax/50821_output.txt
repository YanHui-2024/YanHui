torch/jit/frontend.py in __init__(self, ctx, offending_node, reason)
    109         node_type = type(offending_node)
    110         range_len = len(node_start_tokens.get(node_type, ' '))
--> 111         source_range = ctx.make_range(offending_node.lineno,
    112                                       offending_node.col_offset,
    113                                       offending_node.col_offset + range_len)

AttributeError: 'NoneType' object has no attribute 'lineno'