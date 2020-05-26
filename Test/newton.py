import torch
from torch.autograd import Variable


'''
# 创建一个多元函数，即Y=XW+b=Y=x1*w1+x2*w2*x3*w3+b，x不可求导，W,b设置可求导
X = torch.tensor([1.5, 2.5, 3.5], requires_grad=False)
W = torch.tensor([0.2, 0.4, 0.6], requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)
Y = torch.add(torch.dot(X, W), b)
print(Y)

# 判断每个tensor是否是可以求导的
print(X.requires_grad)
print(W.requires_grad)
print(b.requires_grad)
print(Y.requires_grad)


# 求导，通过backward函数来实现
Y.backward()

# 查看导数，也即所谓的梯度
print(W.grad)
print(b.grad)
                                         
'''


# t=torch.nn.Softmax(theta*x,dim=1)
# print(t)


def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum(dim=1, keepdim=True)  # 底求和
    return X_exp / partition  # 这里应用了广播机制


'''
theta=torch.eye(3,3)
x=torch.randn(3)
print(x)
print(x@theta)
print(torch.nn.Softmax(x@theta))
'''
'''
theta = torch.randn(3, 10, requires_grad=True)
x = torch.randn(10)  # x是横着的……
t = x@theta.t()
print(x)
print(theta)
print(t)
# print(torch.nn.Softmax(t))
t_exp = t.exp()
print(t_exp)
# print(t_exp.sum())
su = t_exp.sum()
print(su)
fuck = t_exp/su
print(fuck)
print(fuck.sum())  # softmax成功
tt=fuck[0]
print(tt.backward())
# print(t.backward())
# print(theta.mm(x.t()))

'''
'''
x = torch.Tensor([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

y1 = F.softmax(x, dim=0)  # 对每一列进行softmax
print(y1)
Z=y1[0]
x.requires_grad()


y2 = F.softmax(x, dim=1)  # 对每一行进行softmax
print(y2)

Softmax
'''


def My_SoftMax(my_theta, my_x):  # theta和x都是横向量
    TX = my_theta@my_x.t()
    under = TX.exp().sum()
    return TX.exp()/under


theta = torch.randn(3, 10, requires_grad=True)
x = torch.randn(10)  # x是横着的……
y = My_SoftMax(theta, x)
one = torch.zeros_like(y)  # 用这个来确定BIO？
one[0] = 1
print(y)
print(y@one.t())
y.sum().backward()
theta.grad  # 只能对标量求导
print(theta.grad)

'''
theta2=torch.rand(10,requires_grad=True)
y2=theta2.exp().sum()
y2.backward()
print(theta2.grad)
'''

xx = torch.tensor([20.],requires_grad=True)
ex=xx.exp().sum()
ex.backward()
print(ex)
print(xx.grad)
xx2=xx.grad
xx2.backward()
print(xx.grad)