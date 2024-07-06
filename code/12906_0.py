import torch

T, B, Cin, Chid, nlayers = 5, 3, 10, 20, 2

class RNNTest(torch.nn.Module):
    def __init__(self):
        super(RNNTest, self).__init__()
        self.rnn = torch.nn.RNN(Cin, Chid, nlayers)

    def forward(self, x, lengths, h0):
        packed = torch.nn.utils.rnn.pack_padded_sequence(x, lengths)
        out, h = self.rnn(packed, h0)
        padded_outs, _ = torch.nn.utils.rnn.pad_packed_sequence(out)
        print(torch._C._get_tracing_state())
        return padded_outs

x, lengths, h0 = torch.rand(T, B, Cin), torch.LongTensor([5, 4, 3]), torch.randn(nlayers, B, Chid)

traced = torch.jit.trace(RNNTest(), (x, lengths, h0))
traced(x, lengths, h0)

T = 7
x, lengths, h0 = torch.rand(T, B, Cin), torch.LongTensor([7, 6, 5]), torch.randn(nlayers, B, Chid)

traced(x, lengths, h0)