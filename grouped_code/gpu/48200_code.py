import torch

@torch.jit.script
def test(A):

    D = A[:, None, :] - A[:, :, None]
    return torch.mean(D)

if __name__ == '__main__':
    for i in range(2):
        A = torch.rand(10, 10).cuda()
        out = test(A).cpu().item()
        print(out)