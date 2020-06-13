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
    verify_set_path, vector_set, delet_invalid=True)

epoch = 30  # 迭代轮数
batch_size = 400


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
        base = random.randint(0, len(TrainSet_X)-batch_size)
        for i in range(batch_size):
            pass
            out = net(TrainSet_X[base+i])
            loss = loss_function(out, TrainSet_Y[base+i])
            optimizer.zero_grad()
            loss.backward(retain_graph=True)
            optimizer.step()

        num = 0
        right = 0
        TP = 0
        TPFP = 0
        TPFN = 0
        i = 0
        # 验证
        for X in VerifySet_Vector:
            prediction = net(X)
            j = 0
            switch = False
            for smax in prediction:
                atom = smax.argmax()
                if atom == 0:
                    TPFP += 1
                if VerifySet_Y[i][j] == 0:
                    TPFN += 1

                if switch and not atom == VerifySet_Y[i][j]:
                    pass
                    TP -= 1
                    switch = False

                elif switch and atom == VerifySet_Y[i][j] and atom == 2:
                    switch = False

                elif not switch and atom == VerifySet_Y[i][j] and atom == 0:
                    pass
                    switch = True
                    TP += 1

                if atom == VerifySet_Y[i][j]:
                    right += 1

                j += 1
                num += 1
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
    plt.savefig("out2.png", dpi=220)
