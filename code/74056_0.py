from typing import Final

import torch


class LinearActivation(torch.nn.Module):
    def forward(
        self, x: torch.Tensor, meta: dict[str, torch.Tensor]
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        meta = meta.copy()
        meta["meta_y_hat"] = x
        # return x, meta # would make it work
        return meta["meta_y_hat"], meta  # JIT claims it errors here


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.flag: Final = ""
        self.activation = LinearActivation()

    def forward(
        self, x: torch.Tensor, meta: dict[str, torch.Tensor]
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        meta = meta.copy()
        if self.flag != "":  # this branch should not even be compiled
            # assert False # would make it work
            score = x[:, -1:]
            x, meta = self.activation(
                x[:, :, :-1],  # replacing this with x, would make it work
                meta,
            )
            x = torch.cat((x, score), dim=1)  # removing this line makes it work
        else:
            x, meta = self.activation(x, meta)
        meta["meta_y_hat"] = x  # removing this line makes it work
        return meta["meta_y_hat"], meta


if __name__ == "__main__":
    model = torch.jit.script(Test())
    x, xs = model.forward(torch.ones(10, 10), {})