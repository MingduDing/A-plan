#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/5 17:00
# @Author:   Domi
# @File:     exam001.py
# @Software: PyCharm

"""
《最大乘积》

题目：给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，
使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)

思路：先将数组降序排序，然后考虑所有的情况，输出最大值
"""


def max_multiply(alist):
    alist.sort(reverse=True)  # 降序排列
    return max(alist[0]*alist[1]*alist[2], alist[0]*alist[-2]*alist[-1])


n = input()
nums = list(map(int, input().split()))  # 空格分割
print(max_multiply(nums))
