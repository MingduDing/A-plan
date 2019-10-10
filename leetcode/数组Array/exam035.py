#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/12 14:36
# @Author : Domi
# @File : exam035.py
# @Software: PyCharm

"""
35.搜索插入位置（easy）

题目：给定一个排序数组和一个目标值，在数组中找到目标值，并
返回其索引。如果目标值不存在与数组中，返回它将会被按顺序插
入的位置。

思路：数组是有序的，只需要找出第一个大于或等于目标值的索引
就行了，利用一个for循环实现。特殊情况：目标值在头和在尾
"""


def search_insert(nums, target):
    """
    35.搜索插入位置
    :param nums: 有序数组
    :param target: 目标值
    :return: 索引
    """
    n = len(nums)
    if nums[-1] < target:
        print(n)
    for i in range(n):
        if nums[i] >= target:
            print(i)
            break


search_insert([1, 3, 5, 6], 7)

