#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/8 15:04
# @Author:   Domi
# @File:     exam532.py
# @Software: PyCharm

"""
532.《数组中的K-diff数对》（easy）

题目：给定一个整数数组和一个整数k, 你需要在数组里找到不同的k-diff数对。这里将k-diff数对
定义为一个整数对(i, j), 其中i和j都是数组中的数字，且两数之差的绝对值是k

思路：
"""


def find_pairs(nums, k):
    if k < 0:
        return 0
    if k == 0:
        return sum([nums.count(num) > 1 for num in set(nums)])  # sum([True, False, False, False])
    return sum([num + k in nums for num in set(nums)])


print(find_pairs([3, 1, 4, 1, 5], 0))
