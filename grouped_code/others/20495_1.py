attribute 'whatisgoingon' of type 'NoneType' is not usable in a script method (did you forget to add it __constants__?):
@torch.jit.script_method
def forward(self, x):
    return x + self.whatisgoingon
               ~~~~~~~~~~~~~~~~~~ <--- HERE