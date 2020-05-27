import torch
import matplotlib.pyplot as plt
y = torch.tensor([0, 1, 0], dtype=torch.float)


def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum()
    return X_exp / partition


pltX = []
pltY = []


def train():
    # 求导大法
    theta = torch.rand(3, 10, requires_grad=True)
    x = torch.randn(10)
    x2 = torch.randn(10)
    # print(softmax(x@theta.t())@y)
    for i in range(200):
        J = (softmax(x@theta.t())@y+softmax(x@theta.t())@y).log()
        J.backward()
        # print(theta.grad)
        theta.data = theta-0.01*theta.grad.data
        print("round"+str(i))
        num = (softmax(x@theta.t())@y+softmax(x@theta.t())@y).log()
        print(num)  # 居然真的能找到这个的最大值？
        pltX.append(i)
        pltY.append(num)

    plt.plot(pltX, pltY)
    plt.show()


theta = torch.rand(3, 10, requires_grad=True)
x = torch.randn(10)
x2 = torch.randn(10)
# print(softmax(x@theta.t())@y)
print(softmax(x@theta.t())@y.t())
print(softmax(x@theta.t())@y)
J = torch.zeros(1)
J += (softmax(x@theta.t())@y.t()).log()
J += (softmax(x2@theta.t())@y.t()).log()
print(J)
J.backward()
# print(theta.grad)
# theta.data = theta-0.01*theta.grad.data
print(theta.grad)
print(theta.data)
print(J.data)
for i in range(20):
    pltX.append(i)
    pltY.append(J.data)


plt.plot(pltX, pltY)
plt.show()