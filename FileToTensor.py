#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   FileToTensor.py
@Time    :   2020/05/27 23:37:41
@Author  :   Rinka
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib

import random
import FileProcessor as FP
import VectorGet as VG
import torch
import matplotlib.pyplot as plt


def ConvertOneSentence(line):
    pass
    spt = line.split('  ')
    Word = []
    Y = []
    BIO_switch1 = False
    if len(spt) >= 1:
        if spt and spt[0]:
            for w in spt:
                if w[0] == '[':
                    Word.append(w[1:w.find('/')])
                    Y.append(0)
                    BIO_switch1 = True
                else:
                    if BIO_switch1 == True:
                        Word.append(w[0:w.find('/')])
                        Y.append(1)
                        if ']' in w:
                            BIO_switch1 = False
                    else:
                        Word.append(w[0:w.find('/')])
                        Y.append(2)
    return Word, Y


def GetXYList(lines, delet_invalid=False):
    pass
    X_SET = []
    Y_SET = []
    for line in lines:
        X, Y = ConvertOneSentence(line)
        if not delet_invalid:
            if Y:
                X_SET.append(X)
                Y_SET.append(Y)
        if delet_invalid:
            if Y:
                if 0 in Y:
                    X_SET.append(X)
                    Y_SET.append(Y)
    return X_SET, Y_SET


def GetSentensVector(X_SET, VE):
    pass
    sentence = []
    for X in X_SET:
        bed = torch.zeros(len(X), 150)
        i = 0
        for word in X:
            if i == 0:
                preWord = VE.GetWordVector("Unknow")
            else:
                preWord = VE.GetWordVector(X[i-1])
            if i == len(X)-1:
                aftherWord = VE.GetWordVector("Unknow")
            else:
                aftherWord = VE.GetWordVector(X[i+1])
            nowWord = VE.GetWordVector(word)
            bed[i] += torch.cat([preWord[0], nowWord[0], aftherWord[0]])
            i += 1
        sentence.append(bed)
    return sentence


def TransFileIntoTensor(file_path, vector_essential, delet_invalid=False):
    '''
    唯一对外开放的函数
    输入文件位置后，得到对应的词向量和对应分类的元组列表
    '''
    data = FP.file_read(file_path)
    X_SET, Y_SET = GetXYList(data, delet_invalid=delet_invalid)
    X_VEC = GetSentensVector(X_SET, vector_essential)
    Y_VEC = []
    for Y in Y_SET:
        vec = torch.tensor(Y)
        Y_VEC.append(vec)

    return X_VEC, Y_VEC  # 这是一大坨集合
