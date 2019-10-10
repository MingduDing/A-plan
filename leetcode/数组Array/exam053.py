#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/12 15:00
# @Author : Domi
# @File : exam053.py
# @Software: PyCharm

"""
53.最大子序和（easy）

题目：给定一个整数数组nums，找到一个具有最大子数组（子数组
最少包含一个元素），返回其最大和。

思路：最大子序和能加入的一定是大于0的数。在原数组基础上不断
更新，大于0的往后加，小于0的不加。
"""


def max_sub_array(nums):
    """
    53.最大子序和
    :param nums: 整数数组
    :return: max(nums)
    """
    n = len(nums)
    for i in range(1, n):
        nums[i] += max(nums[i-1], 0)
    print(max(nums))


max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# max_sub_array([-1, -2, -3, -4])

