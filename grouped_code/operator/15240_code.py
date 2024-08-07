import torch
import torch.nn.functional as F
from torch import nn

class LSTM(nn.Module):

    def __init__(self, d_in, d_hid, num_layers=1):
        super().__init__()
        self.rnn = nn.LSTMCell(d_in, d_hid)

    def forward(self, input, hidden):
        for emb_t in input.split(1, dim=1):
            hidden = self.rnn(emb_t.squeeze(1), hidden)
        return hidden

B, T, C = 1, 5, 3 # batch_size, seq_len, channels
f = LSTM(C, C)
z = torch.randn((B, T, C))
h = torch.randn((B, C))
c = torch.randn((B, C))

inputs = (z, (h, c))
y = f(*inputs)

print('tracing')
tf = torch.jit.trace(f, inputs)
ty = tf(*inputs)

print('saving')
tf.save('tf.pt')

print('loading')
tfl = torch.jit.load('tf.pt')
tyl = tfl(*inputs)