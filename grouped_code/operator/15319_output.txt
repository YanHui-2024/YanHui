RuntimeError: 
The size of tensor a (8) must match the size of tensor b (16) at non-singleton dimension 0

...

ERROR: Graphs differed across invocations!
	Graph diff:
		  graph(%input.1 : Tensor
		        %lengths.1 : Tensor) {
		    %2 : Device = prim::Constant[value="cpu"]()
		    %3 : int = prim::Constant[value=4]()
		    %4 : bool = prim::Constant[value=0]()
		    %5 : bool = prim::Constant[value=0]()
		    %lengths : Tensor = aten::to(%lengths.1, %2, %3, %4, %5)
		    %7 : bool = prim::Constant[value=1]()
		    %input : Tensor, %batch_sizes : Tensor = aten::_pack_padded_sequence(%input.1, %lengths, %7)
		    %10 : int = prim::Constant[value=1](), scope: LSTM
		-   %11 : int = prim::Constant[value=16](), scope: LSTM
		?                                    ^^
		+   %11 : int = prim::Constant[value=8](), scope: LSTM
		?                                    ^