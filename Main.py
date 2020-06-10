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


TrainSet_X, TrainSet_Y = FTT.TransFileIntoTensor(
    train_set_path, vector_set, delet_invalid=True)  # 获取两个向量集
VerifySet_Vector, VerifySet_Y = FTT.TransFileIntoTensor(
    verify_set_path, vector_set)

epoch = 25  # 迭代轮数


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
    for turn in range(epoch):
        i = 0
        for X in TrainSet_X:
            pass
            out = net(X)
            loss = loss_function(out, TrainSet_Y[i])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            i += 1

        num = 0
        right = 0
        TP = 0
        TPFP = 0
        TPFN = 0
        i = 0
        # 验证
        for X in VerifySet_Vector:
            prediction = net(X)
            num += 1
            max_dim = prediction.argmax()
            if max_dim == VerifySet_Y[i]:
                right += 1
                if max_dim == 0 or max_dim == 1:
                    TP += 1
            if VerifySet_Y[i] == 0 or VerifySet_Y[i] == 1:
                TPFN += 1
            if max_dim == 0 or max_dim == 1:
                TPFP += 1
            i += 1

        if TPFN == 0 or TPFP == 0 or TP == 0:
            F1 = 0
        else:
            F1 = 2*(TP/TPFN)*(TP/TPFP)/((TP/TPFN)+(TP/TPFP))
        accuracy = right/num  # 能对上对应BIO的数量
        pltX.append(turn)
        pltY.append(F1)
        print("Epoch:{} Accuracy:{} F1:{}".format(turn, accuracy, F1))

    plt.plot(pltX, pltY)
    plt.savefig("out.png", dpi=220)
