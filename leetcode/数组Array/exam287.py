#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/13 15:08
# @Author:   Domi
# @File:     exam287.py
# @Software: PyCharm

"""
287.《寻找重复数》（medium）

题目：给定一个包含n+1个整数的数组nums，其数字都在1到n之间（包括1和n），可知至少存在一个重复的整数。
假设只有一个重复的整数，找出这个重复的数

思路：二分查找，双指针
"""


def find_duplicate(nums):
    n = len(nums) - 1                        # 变量定义
    start, end = 1, n                        # 头指针和尾指针初始化
    while start+1 < end:                     # 满足条件时进入循环
        mid = start + (end-start) // 2       # 求中间索引值
        count = 0                            # 计数
        for num in nums:                     # 循环遍历
            if num < mid:                    # 如果当前值小于中间值
                count += 1                   # 统计小于mid的值出现的次数
        if count < mid:                      # 如果统计次数不小于中间值
            start = mid                      # 重复数出现在右半段
        else:                                # 否则
            end = mid                        # 重复数出现在左半段
    if nums.count(start) > nums.count(end):  # 统计元素出现次数
        return start                         # 返回头
    return end                               # 返回尾


print(find_duplicate([1, 3, 4, 2, 2]))
