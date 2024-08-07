import torch
import torch.nn as nn
import torch.nn.functional as F

class LNGRUCell(nn.RNNCellBase):
    n_preact: torch.jit.Final[bool]
    """Layer-normalized GRU as in https://arxiv.org/pdf/1607.06450.pdf
    https://github.com/pytorch/pytorch/issues/12482#issuecomment-440485163"""

    def __init__(self, input_size, hidden_size, bias=True, n_preact=True):
        super().__init__(input_size, hidden_size, bias, num_chunks=3)
        self.n_preact = n_preact
        if n_preact:
            self.n_ih = nn.LayerNorm(int(3 * self.hidden_size))
            self.n_hh = nn.LayerNorm(int(3 * self.hidden_size))
        self.n_in = nn.LayerNorm(self.hidden_size)
        self.n_hn = nn.LayerNorm(self.hidden_size)
        # Orthogonal initialization
        nn.init.orthogonal_(self.weight_hh, 2 ** 0.5)
        nn.init.orthogonal_(self.weight_ih, 2 ** 0.5)
        if self.bias:
            nn.init.constant_(self.bias_hh, 0)
            nn.init.constant_(self.bias_ih, 0)

    def forward(self, x, gru_state):
        ih = x @ self.weight_ih.T + self.bias_ih
        hh = gru_state @ self.weight_hh.T + self.bias_hh
        if self.n_preact:  # In CUDA, with jit, breaks here
            ih = self.n_ih(ih)
            hh = self.n_hh(hh)

        i_r, i_z, i_n = ih.chunk(3, dim=1)
        h_r, h_z, h_n = hh.chunk(3, dim=1)
        # No idea why I need to do this, but ok...
        # assert i_n.shape# [-1] == self.hidden_size
        # assert h_n.shape# [-1] == self.hidden_size
        i_n = self.n_in(i_n)
        h_n = self.n_hn(h_n)

        r = torch.sigmoid(i_r + h_r)
        z = torch.sigmoid(i_z + h_z)
        n = torch.tanh(i_n + r * h_n)
        h = (1 - z) * n + z * gru_state
        return h

class LNGRUCell_WithAssert(nn.RNNCellBase):
    n_preact: torch.jit.Final[bool]
    """Layer-normalized GRU as in https://arxiv.org/pdf/1607.06450.pdf
    https://github.com/pytorch/pytorch/issues/12482#issuecomment-440485163"""

    def __init__(self, input_size, hidden_size, bias=True, n_preact=True):
        super().__init__(input_size, hidden_size, bias, num_chunks=3)
        self.n_preact = n_preact
        if n_preact:
            self.n_ih = nn.LayerNorm(int(3 * self.hidden_size))
            self.n_hh = nn.LayerNorm(int(3 * self.hidden_size))
        self.n_in = nn.LayerNorm(self.hidden_size)
        self.n_hn = nn.LayerNorm(self.hidden_size)
        # Orthogonal initialization
        nn.init.orthogonal_(self.weight_hh, 2 ** 0.5)
        nn.init.orthogonal_(self.weight_ih, 2 ** 0.5)
        if self.bias:
            nn.init.constant_(self.bias_hh, 0)
            nn.init.constant_(self.bias_ih, 0)

    def forward(self, x, gru_state):
        ih = x @ self.weight_ih.T + self.bias_ih
        hh = gru_state @ self.weight_hh.T + self.bias_hh
        if self.n_preact:
            ih = self.n_ih(ih)
            hh = self.n_hh(hh)

        i_r, i_z, i_n = ih.chunk(3, dim=1)
        h_r, h_z, h_n = hh.chunk(3, dim=1)
        # No idea why I need to do this, but ok...
        assert i_n.shape
        assert h_n.shape
        i_n = self.n_in(i_n)
        h_n = self.n_hn(h_n)

        r = torch.sigmoid(i_r + h_r)
        z = torch.sigmoid(i_z + h_z)
        n = torch.tanh(i_n + r * h_n)
        h = (1 - z) * n + z * gru_state
        return h




if __name__ == "__main__":
    na, batch_size, input_size, hidden_size = 2, 8, 128, 256
    class Agent(nn.Module):
        num_actions: torch.jit.Final[int]
        def __init__(self, with_assert=False, with_preact=True):
            super().__init__()
            self.num_actions = 2
            if with_assert: self.rnn = LNGRUCell_WithAssert(input_size + na, hidden_size, n_preact=with_preact)
            self.rnn = LNGRUCell(input_size + na, hidden_size, n_preact=with_preact)

        @torch.jit.export
        def get_next_state(self, x, gru_state, is_init, prev_action):
            return self.rnn(torch.cat([x, F.one_hot(prev_action, self.num_actions)], -1),
                            (1. - is_init.unsqueeze(-1)) * gru_state)

    # Input and hidden state
    x = torch.ones((batch_size, input_size)); xc = x.to('cuda')
    a = torch.randint(2, (batch_size,), dtype=torch.int64); ac = a.to('cuda')
    is_init = torch.zeros(batch_size); is_initc = is_init.to('cuda')
    h = torch.zeros((batch_size, hidden_size)); hc = h.to('cuda')
    # Without JIT, cuda and cpu. Works!
    cuda_lngru = Agent().to('cuda')
    cpu_lngru = Agent()
    _ = cuda_lngru.get_next_state(xc, hc, is_initc, ac)
    _ = cpu_lngru.get_next_state(x, h, is_init, a)
    # With JIT, cuda and cpu. CPU works! CUDA doesn't...
    cuda_lngru = torch.jit.script(Agent().to('cuda'))
    cpu_lngru = torch.jit.script(Agent())
    _ = cpu_lngru.get_next_state(x, h, is_init, a)
    try:
        _ = cuda_lngru.get_next_state(xc, hc, is_initc, ac)
        _ = cuda_lngru.get_next_state(xc, _, is_initc, ac)
    except Exception as e:
        print(f'CUDA size error: \n{e}')
    # With JIT and assert, CUDA works
    cuda_lngru = torch.jit.script(Agent(with_assert=True).to('cuda'))
    _ = cuda_lngru.get_next_state(xc, hc, is_initc, ac)
    print('Assert works!')
    # With JIT and without the "preactivation" LayerNorm, CUDA works
    cuda_lngru = torch.jit.script(Agent(with_preact=False).to('cuda'))
    _ = cuda_lngru.get_next_state(xc, hc, is_initc, ac)
    print('No preactivate works')