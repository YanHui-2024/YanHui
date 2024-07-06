RuntimeError: 
python value of type 'ellipsis' cannot be used as a value. Perhaps it is a closed over global variable? If so, please consider passing it in as an argument or use a local varible instead.:
def forward(self, x):
    getitem = x[(Ellipsis, slice(None, None, None))];  x = None
                 ~~~~~~~~ <--- HERE
    return getitem