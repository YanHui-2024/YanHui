class ExperimentalLSTM(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()

    def forward(self, input):
        # type: (Tensor)
        packed = torch.nn.utils.rnn.pack_padded_sequence(
            input=input, lengths=torch.tensor([1, 2]), enforce_sorted=False
        )
        return packed
        # packed is
        # PackedSequence
        #     data
        #     batch_sizes
        #     sorted_indices
        #     unsorted_indices (this is the only different one, it's None in script)

        # output, lengths = torch.nn.utils.rnn.pad_packed_sequence(
        #     sequence=packed, total_length=2
        # )
        # # lengths is flipped, so is output
        # return output[0]

lstm = ExperimentalLSTM(input_dim=2, hidden_dim=2)
lstm = lstm.eval()

batch_size = 2

input = torch.arange(batch_size * 2 * 2).view(batch_size, 2, 2).float()
script_lstm = torch.jit.script(lstm)
script_out = script_lstm(input)
torch._C._jit_set_inline_everything_mode(False)
# print(script_lstm.graph)
print("script result\n{}".format(script_out))

print("\n")
eager_out = lstm(input)
print("eager result\n{}".format(eager_out))