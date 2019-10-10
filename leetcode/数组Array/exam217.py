#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 14:26
# @Author:   Domi
# @File:     exam217.py
# @Software: PyCharm

"""
217.《存在重复元素》（easy）

题目：给定一个整数数组，判断是否存在重复元素。如果任何值在数组中出现至少两次，函
数返回 true。如果数组中每个元素都不相同，则返回 false

思路：哈希表，逻辑运算符
"""


def contains_duplicate_1(nums):
    """
    法1：字典统计法
    :param nums:
    :return:
    """
    d = {}
    for num in nums:
        if num in d:
            return True
        d[num] = 1
    return False


def contains_duplicate_2(nums):
    """
    法2：利用set性质，比较长度
    :param nums:
    :return:
    """
    return len(nums) != len(set(nums))


print(contains_duplicate_1([1, 2, 3, 4]))
