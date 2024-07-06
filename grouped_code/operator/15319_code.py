import torch
import torch.nn as nn

a = torch.randn((8, 5, 30))
a_lengths = torch.randint(low=1, high=a.shape[1], size=(len(a),))
a_lengths, _ = torch.sort(a_lengths, descending=True)

b = torch.randn((16, 5, 30))
b_lengths = torch.randint(low=1, high=b.shape[1], size=(len(b),))
b_lengths, _ = torch.sort(b_lengths, descending=True)

lstm = nn.LSTM(30, 25, batch_first=True)

def feed_rnn(X: torch.Tensor, sorted_lengths: torch.Tensor) -> torch.Tensor:
    X = nn.utils.rnn.pack_padded_sequence(X, sorted_lengths, batch_first=True)
    X, hidden_states = lstm(X)
    # pad_packed_sequence returns a tuple of sequences and lengths
    X, sorted_lengths = nn.utils.rnn.pad_packed_sequence(X, batch_first=True)
    return X

func = torch.jit.trace(feed_rnn, (b, b_lengths), check_inputs=[(b, b_lengths), (a, a_lengths)])