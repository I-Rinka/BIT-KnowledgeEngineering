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

theta = torch.randn(3, 150)

TrainSet_Vector = FTT.TransFileIntoTensor(train_set_path, VE)
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

epoch = 50

lr = 0.1
batch_range = 2000


def Train_One_Epoch():
    add_base = random.randint(0, len(TrainSet_Vector)-batch_range)
    J = torch.zeros(1)
    for i in range(batch_range):
        pass
        J += J_part(TrainSet_Vector[add_base+i][0],
                    TrainSet_Vector[add_base+i][1])
    J.backward()
    theta.data = theta-0.01*theta.grad.data  # 梯度下降
    return J.data


def Identify(XY):
    soft_ans = softmax(XY[0]@theta.t())
    if XY[1].max(0) == soft_ans.max(0):
        return True

    return False


if __name__ == "__main__":
    for i in range(epoch):
        JD = Train_One_Epoch()
        pltX.append(i)
        pltY.append(JD)
        TP = 0
        TPFP = 0
        TPFN = 0
        for xy in VerifySet_Vector:
            judge = Identify(xy)
            if xy[1][0] == 1 or xy[1][1] == 1:  # 真实情况下为1的样本
                if judge:
                    TP += 1
                TPFN += 1
            if judge:
                TPFP += 1
        if TPFP == 0 or TPFN == 0:
            F1 = -1
        else:
            precision = TP/TPFP
            recall = TP/TPFN
            F1 = 2*precision*recall/(precision+recall)
        pltX.append(i)
        pltY.append(F1)
        print('\nEpoch:{} Precision:{} Recall:{} F1_rate:{}\n----------------------------\n'.format(i,
                                                                                                    precision, recall, F1))
    plt.plot(pltX, pltY)
    plt.show()
