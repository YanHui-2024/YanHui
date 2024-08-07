# before analysis
y = rand(1,4)
z = rand(4,4)
x = exp(add(y, z)) # broadcasting add

# using the result of shape analysis, we insert expand nodes and replace
# broadcasting add with a non-broadcasting variant:

# after
y = rand(1,4)
z = rand(4,4)
x = exp(add_nobroadcast(expand_to(y, z), z)) # non-broadcasting add, nobroadcast could be an attribute if that turns out to work.

# fuser is modified to only work on non-broadcasting adds.
