#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Main.py
@Time    :   2020/05/26 01:25:58
@Author  :   Rinka
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''
import random
import torch
import torch.nn as nn
import FileProcessor as FP
import VectorGet as VG
import FileToTensor as FTT
import matplotlib.pyplot as plt

word_vector_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/WordVect.txt"
train_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/train.txt"
verify_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/veri.txt"
# 先读入指定区间，然后根据指定区间每一行的每一个词都建立y的BIO
# 接下来建立词向量词典
# 继续读result的词，读到词后拼接前中后三个向量，然后输入模型训练

VE = VG.vector_essential(word_vector_path)

theta = torch.randn(3, 150)

TrainSet_Vector = FTT.TransFileIntoTensor(train_set_path, VE)  # 获取两个向量集
VerifySet_Vector = FTT.TransFileIntoTensor(verify_set_path, VE)


def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum()
    return X_exp / partition


def J_part(X, Y):
    return (softmax(X@theta.t())@Y).log()


theta = torch.rand(3, 150, requires_grad=True)


pltX = []
pltY = []

# epoch = 20

lr = 0.05


def Train_One_Epoch():
    add_base = random.randint(0, len(TrainSet_Vector)-batch_range)
    J = torch.zeros(1)
    for i in range(batch_range):
        pass
        J += J_part(TrainSet_Vector[add_base+i][0],
                    TrainSet_Vector[add_base+i][1])
    J.backward()
    theta.data = theta.data-lr*theta.grad.data  # 梯度下降
    return J.data



def Identify(XY):
    soft_ans = softmax(XY[0]@theta.t())
    max_a = soft_ans[2]
    max_dim = 2
    for i in range(2):
        if soft_ans[i] > max_a:
            max_a = soft_ans[i]
            max_dim = i
    if XY[1][max_dim] == 1:
        return True
    else:
        return False


class MyFirstNet(nn.Module):
    def __init__(self):
        super(MyFirstNet, self).__init__()
        self.lr = nn.Linear(150, 3)  # 相当于通过线性变换y=x*T(A)+b可以得到对应的各个系数，里面是内置了θ！？
        # self.sm = nn.Softmax()

    def forward(self, x):
        x = self.lr(x)
        # x = self.sm(x)
        return x


net = MyFirstNet()

weight = torch.ones(150, dtype=torch.float32)
loss_function = nn.CrossEntropyLoss(weight=weight)

optimizer = torch.optim.SGD(net.parameters(), lr=0.02)

epoch = 20
batch_range = 100

for i in range(epoch):
    add_base = random.randint(0, len(TrainSet_Vector)-batch_range)
    for i in range(batch_range-1):
        x = TrainSet_Vector[add_base+i][0]
        y = TrainSet_Vector[add_base+i][1]
        out = net(x)
        loss = loss_function(out, y)
        optimizer.zero_grad()   # 清空上一步的残余更新参数值
        loss.backward()         # 误差反向传播, 计算参数更新值
        optimizer.step()
    print(loss)
    pltY.append(loss)
    pltX.append(i)

plt.savefig("test3.png", dpi=220)
plt.show()
