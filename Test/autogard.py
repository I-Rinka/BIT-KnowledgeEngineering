import torch.nn.functional as F
import torch
from torch.autograd import Variable
# x = torch.randn(3)
# x = Variable(x, requires_grad=True)
# y = x*x
# print(y)
# gardients = torch.FloatTensor([1, 1, 1])  # 梯度
# y.backward(gardients)
# x.grad
# print(x)
# print(x.grad)  # 值等于(X^2)'
# print(y)


def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum(dim=1, keepdim=True)  # 底求和
    return X_exp / partition  # 这里应用了广播机制


theta = torch.rand(2, 3)
print(theta)
print(softmax(theta))
print(F.softmax(theta,dim=1))#对每一行softmax


x = torch.Tensor([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

y1 = F.softmax(x, dim=0)  # 对每一列进行softmax
print(y1)
Z=y1[0]
x.requires_grad()


y2 = F.softmax(x, dim=1)  # 对每一行进行softmax
print(y2)

