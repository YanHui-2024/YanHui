if orig._backward_hooks or orig._forward_hooks or orig._forward_pre_hooks:
    raise ValueError("Modules that have hooks assigned can't be compiled")