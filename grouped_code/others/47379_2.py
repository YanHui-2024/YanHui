       if torch.jit.is_scripting():
            return x + 1
        else:
            if not torch.jit.is_tracing():
                return x + 1
            else:
                return x + 2