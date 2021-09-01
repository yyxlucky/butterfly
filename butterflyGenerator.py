#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : yixuan yang
# @File    : butterflyGenerator.py

import util.CL as CL
import util.IO as IO
import numpy as np


def butterfly():
    io = IO.io()
    # cur1 = dt.datetime.now()
    # /Users/yxyang/Desktop/butterfly/American Revolution1.txt
    adjMat = io.__getitem__(0)
    # adjMatC = io.__getitem__(1)
    obj = io.__getitem__(2)
    attr = io.__getitem__(3)

    # 计算原形式背景和补形式背景下的概念格cl,clC
    cl = CL.cl(adjMat, obj, attr)

    bpCliques = cl.__getitem__(2)

    max = 0
    B = [0]

    print("BC(KG):", len(bpCliques))
    print("--------------")


    for bc in bpCliques:
        # print(bc.getL(), bc.getR())
        el = len(bc.getL())
        il = len(bc.getR())
        tempNum = el * (el -1) * il * (il -1) /4
        # print(tempNum)
        if tempNum >= max:
            max = tempNum
            B.pop()
            B.append(bc)

    print("--------------")
    print("The butterfly generator is:")
    print(B[0].getL(), B[0].getR())
    print("N is :", int(max))

    print("--------------")




    '''
    while(True):
        print("--------------")
        n = int(input("请输入N："))
        Nlist = []
        for bc in bpCliques:
            # print(bc.getL(), bc.getR())
            el = len(bc.getL())
            il = len(bc.getR())
            tempNum = el * (el -1) * il * (il -1) /4
            if tempNum >= n:
                Nlist.append(bc)

        print(len(Nlist))
    '''
    NClist = [0] * int(max+1)
    for bc in bpCliques:
        # print(bc.getL(), bc.getR())
        el = len(bc.getL())
        il = len(bc.getR())
        tempNum = int(el * (el -1) * il * (il -1) /4)
        # print(tempNum, NClist)
        NClist[tempNum] = NClist[tempNum] + 1


    for n in range(1, len(NClist)):
        if NClist[n] == 0:
            pass
        else:
            print(n, NClist[n])

    #C:\yyx\SCH\ThirdSeme\code and experiment\butterfly\American Revolution1.txt
    # C:\yyx\SCH\ThirdSeme\code and experiment\butterfly\dataset&result\FilmTrust1.txt







butterfly()
