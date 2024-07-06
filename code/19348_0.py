import torch.nn as nn
import torch.jit as jit


class SomeScriptModule(jit.ScriptModule):
    def __init__(self):
        super().__init__()

        self.linear = nn.Linear(16, 16)
        self.conv2d = nn.Conv2d(3, 8, 3)
        self.conv3d = nn.Conv3d(3, 8, 3)
        self.gru = nn.GRU(16, 16)
        self.lstm = nn.LSTM(16, 16)

        for m in self.modules():
            print(m, type(m))

            if isinstance(m, nn.Linear):
                print(f'm is Linear')
                continue

            if isinstance(m, nn.Conv2d):
                print(f'm is Conv2d')
                continue

            if isinstance(m, nn.Conv3d):
                print(f'm is Conv3d')
                continue

            if isinstance(m, nn.GRU):
                print(f'm is GRU')
                continue

            if isinstance(m, nn.LSTM):
                print(f'm is LSTM')
                continue

            print('??????')


SomeScriptModule()