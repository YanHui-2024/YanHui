import torch

cu = torch.jit.CompilationUnit('''
def fizzbuzz(niter : int):
    for i in range(niter):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
    return niter
''')

print(cu.fizzbuzz.graph)