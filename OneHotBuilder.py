#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DBuilder.py
@Time    :   2020/05/01 18:18:31
@Author  :   Rinka 
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib


class OneHotBuilder:
    # 常规操作：
    def __init__(self, fileName, startDate, endDate):
        """初始化完后Run一下函数"""
        #决定OneHot是多少维的向量
        self.demension=15000
        self.fileName = fileName
        self.startDate = startDate
        self.endDate = endDate
        self.__f = open(self.fileName, "r")
        self.__dic1 = {}
        self.OneHotDic = {}
        self.Run()
        # self.topList=[]

    def __str__(self):
        return "file:%s\nstart:%s\nend:%s\n" % (self.fileName, self.startDate, self.endDate)

    # 功能函数：
    def __GetWord(self, line):
        """输入：文件读入的一行字符串|返回值：二维列表，二维列表的第二个属性为词性"""
        # line = self.__f.readline()
        splt = line.split('  ')
        out = []
        for v in splt:
            if v[0] == '[':
                out.append([v[1:v.find('/')], v[v.find('/'):]])
            else:
                out.append([v[0:v.find('/')], v[v.find('/'):]])
            # out.append([v[0:v.find('/')], v[v.find('/'):]])
        return out

    def __GetEntity(self, line):
        """得到命名实体|输入：文件读入的一行字符串|返回值：一维列表"""
        out = []
        # line = self.__f.readline()
        prePosition = line.find('[')
        while prePosition != -1:
            Position = line[prePosition:].find(']')
            Position = Position+prePosition
            if 'nt' in line[Position+1:Position+3]:
                splt = line[prePosition:Position].split('  ')
                Str = ''
                for v in splt:
                    Str = Str+v[0:v.find('/')]
                out.append(Str[1:])
            prePosition = line[Position:].find('[')
            if prePosition != -1:
                prePosition += Position
        return out

    # 建立字典(字典需要用已有的，输入的二元组也是已有的)，统计词频
    #更新词典
    def __UpdateDic(self, Dic, wordList):
        for word in wordList:
            if '/n' in word[1]:
                if not word[0] in Dic:
                    Dic[word[0]] = 1
                else:
                    Dic[word[0]] = Dic[word[0]]+1
        return Dic

    def Run(self):
        switch = False
        switch2 = False
        while True:
            line = self.__f.readline()
            # 输入输出停止/起始判断，通过两个开关来决定当前的状态
            if line.startswith(self.startDate) and switch == False:
                switch = True
            if line.startswith(self.endDate):
                switch2 = True
            elif switch2:
                break

            if switch:
                t = self.__GetWord(line)
                self.__UpdateDic(self.__dic1, t)
        self.topList=list(self.__dic1.items())
        self.topList.sort(key=lambda parameter_list: parameter_list[1],reverse=True)
        ran=min(self.demension-1,len(self.topList))
        for i in range(ran):
            self.OneHotDic[self.topList[i][0]]=i
        self.OneHotDic['UNKNOWN']=ran
        return

    def GetDemension(self,word):
        """输入：需要得到对应onehot向量下标的字符|返回：onehot向量维度"""
        if word in self.OneHotDic:
            return self.OneHotDic[word]
        else:
            return self.OneHotDic['UNKNOWN']
        

p1 = OneHotBuilder(
    R'C:\Users\I_Rin\Documents\Dev\KnowledgeEn\One\data/1998-01-2003版-带音.txt', "19980101", "19980120")
print(p1.OneHotDic)
print(p1.GetDemension('UNKNOWN'))
for i in range(100):
    print(p1.topList[i])