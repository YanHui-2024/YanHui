RuntimeError: 
invalid argument 0: Sizes of tensors must match except in dimension 1. Got 3 and 1 in dimension 0 at /pytorch/aten/src/TH/generic/THTensorMoreMath.cpp:1317:
operation failed in interpreter:
    halt_probability = self.halt_noise(halt_probability, training)
    halt_probs.append(halt_probability)
    print(halt_probs)
    residual = torch.sum(torch.cat(halt_probs))
    states_tensor = torch.stack(states, dim=1)
                    ~~~~~~~~~~~ <--- HERE