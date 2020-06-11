#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   VectorGet.py
@Time    :   2020/05/26 00:25:23
@Author  :   Rinka 
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib

import torch
import Util.FileProcessor as FR
import torch.nn as nn


class vector_essential:
    def __init__(self, vector_file_path):
        super().__init__()
        self.read = self.__read_vector_file(vector_file_path)
        self.wordDic = self.read[0]
        self.wordEmbed = self.read[1]

    def GetWordVector(self, word):
        return self.__return_dim(word, self.wordDic, self.wordEmbed)

    def __read_vector_file(self, path):
        """
        同时返回有单词的词典和向量列表
        """
        result = FR.file_read(path)
        wordDic = {}
        vectorList = []
        i = 0
        for line in result:
            vec = line.split(' ')
            float_vector = []
            for v in vec[1:]:
                float_vector.append(float(v))
            vectorList.append(float_vector)
            wordDic[vec[0]] = i
            i += 1
        embed = nn.Embedding(len(vectorList), len(vectorList[0]))
        embed.weight.data.copy_(torch.tensor(vectorList))
        return wordDic, embed

    def __return_dim(self, word, wordDic, embed):
        if word not in wordDic:
            return torch.zeros_like(embed((torch.tensor([0]))))
        return embed((torch.tensor([wordDic[word]])))


