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
import FileProcessor as FP
import VectorGet as VG
import torch
import matplotlib.pyplot as plt

word_vector_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/WordVect.txt"
train_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/train.txt"
verify_set_path = "C:/Users/I_Rin/Documents/Dev/College_KnowledgeEngineering/veri.txt"
# 先读入指定区间，然后根据指定区间每一行的每一个词都建立y的BIO
# 接下来建立词向量词典
# 继续读result的词，读到词后拼接前中后三个向量，然后输入模型训练

VE = VG.vector_essential(word_vector_path)
train_set = FP.file_read(train_set_path)
verify_set = FP.file_read(verify_set_path)


"19980119-08-004-006/m  亚洲/ns  十佳/jn  运动员/n  评选/vn  是/vl  [中国/ns  体育/n  记者/n  协会/n]nt  的/ud  一/m  项/qe  传统/a  活动/vn  ，/wd  每年/rz  由/p  中央/n  和/c  首都/n  新闻/n  单位/n  、/wu  地方{di4fang1}/n  体育/n  记者/n  协会/n  根据/p  当年{dang4nian2}/t  亚洲/ns  运动员/n  的/ud  表现/vn  评选/vt  ，/wd  至今/d  已/d  举办/vt  了/ul  １６/m  届/qe  。/wj  １９９７/t  年度/n  亚洲/ns  运动员/n  评选/vn  由/p  [中国/ns  体育/n  记者/n  协会/n]nt  和/c  [南京/ns  金鹏/nz  铝业/n  有限公司/n]nt  共同/d  举办/vt  。/wj  "


def line_processor(line):
    spt = line.split('  ')
    BIO_line = []
    BIO_switch1 = False
    if len(spt) >= 1:
        if spt and spt[0]:
            for w in spt:
                if w[0] == '[':
                    BIO_line.append([w[1:w.find('/')], "B"])
                    BIO_switch1 = True
                else:
                    if BIO_switch1 == False:
                        BIO_line.append([w[0:w.find('/')], "O"])
                    else:
                        BIO_line.append([w[0:w.find('/')], "I"])
                        if ']' in w:
                            BIO_switch1 = False
    return BIO_line


def GetBIOSet(data_set):
    BIOSet = []
    for line in data_set:
        bs = line_processor(line)
        if bs:
            BIOSet.append(bs)
    return BIOSet


BIO = {"B": 0, "I": 1, "O": 2}

train_set_BIO = GetBIOSet(train_set)
verify_set_BIO = GetBIOSet(verify_set)

theta = torch.randn(3, 150)

XY = []


def BIOLineToX(bio_line):
    for i in range(len(bio_line)):
        if i == 0:
            preWord = VE.GetWordVector("Unknow")
        else:
            preWord = VE.GetWordVector(bio_line[i-1][0])
        nowWord = VE.GetWordVector(bio_line[i][0])
        if i == len(bio_line)-1:
            aftherWord = VE.GetWordVector("Unknow")
        else:
            aftherWord = VE.GetWordVector(bio_line[i+1][0])
        vec = torch.cat([preWord[0], nowWord[0], aftherWord[0]])
        y = torch.zeros(3, dtype=torch.float32)
        y[BIO[bio_line[i][1]]] = 1
        XY.append([vec, y])
    return XY


for line in train_set_BIO:
    BIOLineToX(line)


def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum()
    return X_exp / partition


theta = torch.rand(3, 150, requires_grad=True)


def J_part(x, y):
    return (softmax(x@theta.t())@y+softmax(x@theta.t())@y).log()


pltX = []
pltY = []

epoch = 20
for i in range(epoch):
    J = J_part(XY[0][0], XY[0][1])
    for Jp in XY:
        J += J_part(Jp[0], Jp[1])
    J.backward()
    theta.data = theta-0.01*theta.grad.data
    num = J
    print(num)  # 居然真的能找到这个的最大值？
    pltX.append(i)
    pltY.append(num)

plt.plot(pltX, pltY)
plt.show()
