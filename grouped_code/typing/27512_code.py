def test(pos):
    return pos // 2

input = torch.tensor(4)
print(test(input)
# tensor(2)
print(torch.jit.script(test)(input))
# 2