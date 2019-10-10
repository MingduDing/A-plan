#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/8 14:06
# @Author:   Domi
# @File:     exam485.py
# @Software: PyCharm

"""
485.《最大连续1的个数》（easy）

题目：给定一个二进制数组， 计算其中最大连续1的个数

思路：循环遍历，统计1的个数
"""


def find_max_consecutive_ones(nums):
    count = max_ones = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        max_ones = max(count, max_ones)  # 不断更新max_ones的值
    return max_ones


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
