#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/12 13:34
# @Author : Domi
# @File : exam027.py
# @Software: PyCharm

"""
27.移除元素（easy）

题目：给定一个数组nums和一个值val，你需要原地移除所有数值
等于val的元素，返回移除后数组的新长度。不要使用额外的数组
空间，必须在原地修改输入数组并只使用O(1)额外空间。

思路：数组是无序的，使用快慢指针，慢指针i自加1，快指针j放
在for循环中，遍历数组，判断前后值是否相等，相等时j后移，
不相等时i加1，值交换
"""


def remove_element(nums, value):
    """
    27.移除元素
    :param nums: 整数数组
    :param value: 数值
    :return: nums[:i]
    """
    n = len(nums)
    i = 0
    if n == 0:
        return None
    for j in range(n):
        if value != nums[j]:
            nums[i] = nums[j]
            i += 1
    print(nums[:i])


remove_element([2, 0, 1, 2, 2, 3, 0, 4, 2], 2)
