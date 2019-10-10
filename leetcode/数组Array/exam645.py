#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/13 14:22
# @Author:   Domi
# @File:     exam645.py
# @Software: PyCharm

"""
645.《错误的集合》（easy）

题目：集合S包含从1到n的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的
另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。给定一个数组nums代表了集合S发生错误
后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回

思路：集合相减268
"""


def find_error_nums_1(nums):
    """
    法1：数学方法
    :param nums:
    :return:
    """
    nums_set = set(nums)                        # 获得输入数组的集合
    repeat = sum(nums) - sum(nums_set)          # 求和相减即为重复
    correct_set = set(range(1, len(nums) + 1))  # 理想情况下的数组
    defect = correct_set - nums_set             # 集合相减即为缺失
    return [repeat, defect.pop()]               # 返回结果


print(find_error_nums_1([1, 1]))
