#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/9 9:23
# @Author:   Domi
# @File:     exam561.py
# @Software: PyCharm

"""
561.《数组拆分》（easy）

题目：给定长度为2n的数组, 你的任务是将这些数分成n对, 例如(a1,b1), (a2,b2), ..., (an,bn)，
使得从1到n的min(ai,bi)总和最大

思路：排序
"""


def array_pair_sum(nums):
    nums.sort()
    return sum([nums[i] for i in range(0, len(nums), 2)])


print(array_pair_sum([1, 4, 3, 2]))
