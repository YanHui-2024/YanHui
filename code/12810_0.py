import torch


@torch.jit.script
def fun(a):
	return a[None, :]


if __name__ == '__main__':
	a = torch.tensor([0])
	fun(a)