#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/8 14:28
# @Author:   Domi
# @File:     exam509.py
# @Software: PyCharm

"""
509.《斐波那契数列》（easy）

题目：斐波那契数，通常用F(n)表示，形成的序列称为斐波那契数列。该数列由0和1开始，后面的每一项数字都是前面两项数字的和
F(0) = 0,  F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 给定 N，计算 F(N).

思路：递归
"""


def fib_single(N):
    """
    打印单个数
    :param N:
    :return:
    """
    if N == 0:
        return 0
    if N == 1:
        return 1
    else:
        return fib_single(N-1) + fib_single(N-2)


def fib_sum(N):
    """
    打印整个列表
    :param N:
    :return:
    """
    alist = []
    for i in range(N):
        if i == 0 or i == 1:
            alist.append(1)
        else:
            alist.append(alist[i-1]+alist[i-2])
    return alist


print(fib_sum(4))
