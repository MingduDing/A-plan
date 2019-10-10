#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/15 16:17
# @Author:   Domi
# @File:     exam887.py
# @Software: PyCharm

"""
887.《鸡蛋掉落》（hard）

题目：你将获得K个鸡蛋，并可以使用一栋从1到N共有N层楼的建筑。每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层F，满足0<=F<=N任何从高于F的楼层落下的鸡蛋都会碎，从F楼层或比它低的楼层落下的鸡蛋都不会破。每次移动，你可以
取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层X扔下（满足 1<=X<=N）。
你的目标是确切地知道F的值是多少。无论F的初始值如何，你确定F的值的最小移动次数是多少？

思路：动态规划，二分查找
"""


def super_egg_drop(K, N):
    ts = [0]*K
    ts.append(0)
    for i in range(1, K+1):
        ts[i] = ts[i-1]*2 + 1
    if N <= ts[-1]:
        for i in ts:
            if i >= N:
                m = ts.index(i)
                break
    else:
        ans = ts[-1]
        m = K
        while N > ans:
            m += 1
            ans = bss(K, m)
    return m


def ass(i):
    ts = 1
    for i in range(1, i):
        ts = ts * 2 + 1
    return ts


def bss(i, j):
    if i == j:
        return ass(i)
    elif i == 1 and j > i:
        return j
    else:
        ans = bss(i, j-1) + bss(i-1, j-1) + 1
    return ans


print(super_egg_drop(2, 6))
