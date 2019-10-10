#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/5 17:18
# @Author:   Domi
# @File:     exam136.py
# @Software: PyCharm

"""
136.《只出现一次的数字》 (easy)

题目：给定一个非空整数数组，除了某个元素只出现一次以外，其
余每个元素均出现两次。找出那个只出现了一次的元素

思路：遍历，异或
"""


def single_number_1(nums):
    """
    法1：构建字典
    :param nums:
    :return:
    """
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    d_reverse = dict((val, key) for key, val in d.items())  # 实现字典键值对互换
    # d_reverse = dict(zip(d.values(), d.keys()))
    return d_reverse


def single_number_2(nums):
    """
    法2：异或
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):  # 遍历数组
        nums[0] ^= nums[i]         # 先转为二进制，再异或. 相同出0，不同出1. 与0异或：a^0 = a
    return nums[0]                 # 只出现一次的就是结果


print(single_number_1([1, 5, 2, 1, 4, 2, 4]))
