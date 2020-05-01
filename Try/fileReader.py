#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fileReader.py
@Time    :   2020/05/01 11:38:50
@Author  :   Rinka 
@Contact :   I_Rinka@outlook.com
@License :   (C)Copyright 2019-2020, BIT_Rinka
@Desc    :   None
'''

# here put the import lib


class fileReader:
    # 常规操作：
    def __init__(self, fileName, startDate, endDate):
        self.fileName = fileName
        self.startDate = startDate
        self.endDate = endDate
        self.__f = open(self.fileName, "r")


    def __str__(self):
        return "file:%s\nstart:%s\nend:%s\n" % (self.fileName, self.startDate, self.endDate)

# 功能函数：
    def VocProcess(self):
        """读取文件一行，将一行中的数据处理为二维列表|返回值：二维列表，二维列表的第二个属性为词性|当返回值为**时代表读到了结尾"""
        line = self.__f.readline()
        splt = line.split('  ')
        out = []
        for v in splt:
            out.append([v[0:v.find('/')], v[v.find('/'):]])
        return out

    def GetEntity(self):
        """得到命名实体|返回值：一维列表"""
        out = []
        line = self.__f.readline()
        prePosition=line.find('[')
        while prePosition!=-1:
            Position=line[prePosition:].find(']')
            Position=Position+prePosition
            if 'nt' in line[Position+1:Position+3]:
                splt=line[prePosition:Position].split('  ')
                Str=''
                for v in splt:
                    Str=Str+v[0:v.find('/')]
                out.append(Str[1:])
            prePosition=line[Position:].find('[')
            if prePosition!=-1:
                prePosition+=Position
        return out

    def LocateStart(self,start):
        """把行号定位到给定行号，如果此时继续读取会读到后一行"""
        line = self.__f.readline()
        while not line.startswith(start):
            line = self.__f.readline()
        return
            

p1 = fileReader(
    R'C:\Users\I_Rin\Documents\Dev\KnowledgeEn\One\data/1998-01-2003版-带音.txt', "19980101", "19980120")
# p1.LocateStart("19980101-01-001-013")
for i in range(10):
    print(p1.GetEntity())
    # print(p1.VocProcess())