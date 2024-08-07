class resblock(ScriptModule):

    __constants__ = ["nblocks","ch","shortcut"]

    def __init__(self, ch, nblocks=1, shortcut=True):

        super().__init__()
        self.shortcut = shortcut
        self.nblocks = nblocks
        self.ch = ch
        self.module_list = nn.ModuleList()
        self.blockt1=add_conv(self.ch, self.ch//2, 1, 1)
        self.blockt2=add_conv(self.ch//2, self.ch, 3, 1)
        for _ in range(nblocks):
            resblock_one = nn.ModuleList()
            self.blockt1
            self.blockt2
            self.module_list.append(resblock_one)

    @script_method
    def forward(self, x):
        for _ in range(self.nblocks):#in_ch, out_ch, ksize, stride
            h = x
            h = self.blockt1(h)
            h = self.blockt2(h)
            x = x + h if self.shortcut else h
        return x