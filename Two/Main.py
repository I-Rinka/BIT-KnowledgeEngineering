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
import VectorGet as VG
import FileToTensor as FTT
import torch
import matplotlib.pyplot as plt

word_vector_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/WordVect.txt"
train_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/train.txt"
verify_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/veri.txt"

# 先读入指定区间，取出指定区间所有词的词向量
# 接下来建立词向量词典
# 读入文件，读到词后拼接前中后三个向量，然后输入模型训练

vector_set = VG.vector_essential(word_vector_path)


TrainSet_Vector = FTT.TransFileIntoTensor(
    train_set_path, vector_set)  # 获取两个向量集
VerifySet_Vector = FTT.TransFileIntoTensor(verify_set_path, vector_set)

batch_size = 200
epoch = 25  # 迭代轮数


def GetBatchVector(vector_set):  # 得到一个batch所需要的向量，随机梯度下降
    base = random.randint(0, len(vector_set)-batch_size)
    Y = torch.ones(batch_size, dtype=torch.long)
    X = vector_set[base+batch_size-1][0].unsqueeze(0)
    Y[batch_size-1] = vector_set[base+batch_size-1][1]
    for i in range(batch_size-1):
        X = torch.cat((X, vector_set[base+i][0].unsqueeze(0)))
        Y[i] = vector_set[base+i][1]
    return X, Y


class MultiClassify(torch.nn.Module):  # 建立神经网络，是简单的线性模型
    def __init__(self):
        super(MultiClassify, self).__init__()
        self.theta = torch.nn.Linear(150, 3)

    def forward(self, x):
        x = self.theta(x)
        return x


pltX = []
pltY = []

if __name__ == "__main__":

    net = MultiClassify()
    optimizer = torch.optim.SGD(net.parameters(), lr=0.05)
    loss_function = torch.nn.CrossEntropyLoss()
    for i in range(epoch):
        X, Y = GetBatchVector(TrainSet_Vector)

        # 梯度下降
        out = net(X)
        loss = loss_function(out, Y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        num = 0
        right = 0
        TP = 0
        TPFP = 0
        TPFN = 0
        for vec_xy in VerifySet_Vector:
            prediction = net(vec_xy[0])  # 预测
            num += 1
            max_dim = prediction.argmax()
            if max_dim == vec_xy[1]:
                right += 1
                if max_dim == 0 or max_dim == 1:
                    TP += 1
            if vec_xy[1] == 0 or vec_xy[1] == 1:
                TPFN += 1
            if max_dim == 0 or max_dim == 1:
                TPFP += 1
        if TPFN == 0 or TPFP == 0 or TP == 0:
            F1 = 0
        else:
            F1 = 2*(TP/TPFN)*(TP/TPFP)/((TP/TPFN)+(TP/TPFP))
        accuracy = right/num  # 能对上对应BIO的数量
        pltY.append(F1)
        pltX.append(i)
        print("Epoch:{} Accuracy:{} F1:{}".format(i, accuracy, F1))

    plt.plot(pltX, pltY)
    plt.savefig("out.png", dpi=220)
