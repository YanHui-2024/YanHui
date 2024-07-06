# Tracer vs Eager mode difference in tensor.shape
import torch
import onnxruntime

class Model(torch.nn.Module):
    def forward(self, hidden_states):
        batch_size, seq_length = hidden_states.shape[:2]
        real_seq_length = seq_length
        real_seq_length += 2                                            => real_seq_length and seq_legth should have different values
        return real_seq_length + seq_length


# Call export

# hidden_states is tensor of rank 2
hidden_states = torch.randn(2, 3, 5)
model = Model()

import io
onnx_io = io.BytesIO()
tracemodel = torch.jit.trace(model, (hidden_states, ))
torch.onnx.export(model, (hidden_states, ), onnx_io, verbose=True)

# Call onnxruntime runtime and compare outputs on dynamic inputs
ort_session = onnxruntime.InferenceSession(onnx_io.getvalue())

print(model(hidden_states))
print(tracemodel(hidden_states))
print(ort_session.run(None, {
                                ort_session.get_inputs()[0].name: hidden_states.numpy()
                            }))