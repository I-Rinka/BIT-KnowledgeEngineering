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
import FileProcessor as FP
import VectorGet as VG
import FileToTensor as FTT
import torch
import matplotlib.pyplot as plt

word_vector_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/WordVect.txt"
train_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/train.txt"
verify_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/veri.txt"
# 先读入指定区间，然后根据指定区间每一行的每一个词都建立y的BIO
# 接下来建立词向量词典
# 继续读result的词，读到词后拼接前中后三个向量，然后输入模型训练

VE = VG.vector_essential(word_vector_path)

# theta = torch.randn(3, 150)

TrainSet_Vector = FTT.TransFileIntoTensor(train_set_path, VE)  # 获取两个向量集
VerifySet_Vector = FTT.TransFileIntoTensor(verify_set_path, VE)

batch_size = 100


def GetBatchVector(vector_set):
    base = random.randint(0, len(vector_set)-batch_size)
    Y = torch.ones(batch_size, dtype=torch.long)
    X = vector_set[base+batch_size-1][0].unsqueeze(0)
    Y[batch_size-1] = vector_set[base+batch_size-1][1]
    for i in range(batch_size-1):
        X = torch.cat((X, vector_set[base+i][0].unsqueeze(0)))
        Y[i] = vector_set[base+i][1]
    return X, Y


class MultiClassify(torch.nn.Module):
    def __init__(self):
        super(MultiClassify, self).__init__()
        self.theta = torch.nn.Linear(150, 3)

    def forward(self, x):
        x = self.theta(x)
        return x


epoch = 20

pltX = []
pltY = []
pltY2 = []

if __name__ == "__main__":

    net = MultiClassify()
    optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
    loss_function = torch.nn.CrossEntropyLoss()
    for i in range(epoch):
        X, Y = GetBatchVector(TrainSet_Vector)
        out = net(X)
        loss = loss_function(out, Y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if i % 2 == 0:
            num = 0
            right = 0
            TP = 0
            TPFP = 0
            TPFN = 0
            for vec_xy in VerifySet_Vector:
                prediction = net(vec_xy[0])
                num += 1
                if prediction.argmax() == vec_xy[1]:
                    right += 1
                    if prediction.argmax() == 0 or prediction.argmax() == 1:
                        TP += 1
                if vec_xy[1] == 0 or vec_xy[1] == 1:
                    TPFN += 1
                if prediction.argmax() == 0 or prediction.argmax() == 1:
                    TPFP += 1
                if TPFN == 0 or TPFP == 0 or TP == 0:
                    F1 = 0
                else:
                    F1 = 2*(TP/TPFN)*(TP/TPFP)/((TP/TPFN)+(TP/TPFP))
                accuracy = right/num
                pltY.append(accuracy)
                pltY2.append(F1)
                pltX.append(i)
            print("Epoch:{} Accuracy:{} F1:{}".format(i, accuracy, F1))

    plt.plot(pltX, pltY)
    plt.savefig("test3.png", dpi=220)
    plt.show()
    plt.plot(pltX, pltY2)
    plt.savefig("test4.png", dpi=220)
    plt.show()
