import torch
from torch.autograd import Variable
x = torch.randn(3)
x = Variable(x, requires_grad=True)
y = x*x
print(y)
gardients = torch.FloatTensor([1, 1, 1])  # 梯度
y.backward(gardients)
x.grad
print(x)
print(x.grad)  # 值等于(X^2)'
print(y)
