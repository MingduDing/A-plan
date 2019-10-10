#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 17:03
# @Author:   Domi
# @File:     exam414.py
# @Software: PyCharm

"""
414.《第三大的数》（easy）

题目：给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)

思路：循环遍历
"""


def third_max_1(nums):
    """
    法1：三次遍历
    :param nums:
    :return:
    """
    top1, top2, top3 = float('-inf'), float('-inf'), float('-inf')
    length = len(nums)

    # 第一趟遍历寻找第一大数
    for i in range(length):
        if nums[i] > top1:
            top1 = nums[i]

    # 第二趟遍历寻找次大数
    for i in range(length):
        if top2 < nums[i] < top1:
            top2 = nums[i]

    # 第三趟遍历寻找第三大数
    for i in range(length):
        if top3 < nums[i] < top2:
            top3 = nums[i]

    return top1 if top3 == float('-inf') else top3  # 返回第三大数或第一个大数


def third_max_2(nums):
    """
    法2：
    :param nums:
    :return:
    """
    first = second = third = float('-inf')             # 初始化三个变量
    for num in nums:                                   # 循环遍历
        if num in [first, second, third]:              # 如果遇到相同的数
            continue                                   # 跳过
        if num > first:                                # 遇到最大的数
            third = second                             # 更新3个最大数
            second = first
            first = num                                # first, second, third = num, first, second
        elif num > second:                             # 如果在最大数和次大数之间
            third = second                             # 更新后两个数
            second = num                               # second, third = num, second
        elif num > third:                              # 如果在次大数和第三大数之间
            third = num                                # 更新第三大数
    return third if third != float('-inf') else first  # 返回第三大的数或最大的数


print(third_max_2([3, 2, 2, 1]))
