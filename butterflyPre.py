#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : butterflyPre.py

import numpy as np

def proprocess():
    # 读入形式背景
    filename = input("请输入文件名：")
    # filename = '/Users/yxyang/Desktop/Intra-organisational networks.txt'

    with open(filename, "r") as f:
        numObj = int(f.readline())  # 获取对象数量
        numAttr = int(f.readline())
        adjMat = np.zeros(shape=(numObj, numAttr), dtype=int)  # 存储形式背景矩阵
        obj = []
        attr = []

        # 将形式背景存储到矩阵内
        lines = f.readlines()  # 读取全部内容

        for i in range(0, lines.__len__(), 1):  # (开始/左边界, 结束/右边界, 步长)

            list = []  ## 空列表, 将第i行数据存入list中
            word = lines[i].split()
            n1 = int(word[0])
            # print(n1)
            n2 = int(word[1])
            adjMat[n1 - 1][n2 - 1] = 1

    outFile = input("请输入写出矩阵结果的文件路径：")
    # outFile = '/Users/yxyang/Desktop/rs.txt'
    with open(outFile, 'w') as fi:

        fi.write(str(numObj) + "\n")
        fi.write(str(numAttr) + '\n')

        for i in range(numObj):
            for j in range(numAttr):
                if i == j:
                    adjMat[i][j] = 1
                fi.write(str(adjMat[i][j]))
                # fi.write(" ")
            fi.write('\n')



proprocess()
