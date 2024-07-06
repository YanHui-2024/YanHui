@torch.jit.script_method
    def forward(self, list_of_frame_dictionaries):
        # type: (List[Dict[str, Tensor]]) -> Tuple[Tensor, Tensor, Tensor, Tensor, Tensor] # noqa