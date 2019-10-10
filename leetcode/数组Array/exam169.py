#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 10:47
# @Author:   Domi
# @File:     exam169.py
# @Software: PyCharm

"""
169.《求众数》（easy）

题目：给定一个大小为n的数组，找到其中的众数. 众数是指在数组中出现次数大于n/2的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数

思路：位运算，分治算法
"""


def majority_element_1(nums):
    """
    法1：暴力字典统计法
    :param nums:
    :return:
    """
    count = {}
    for num in nums:  # 统计每个数字出现的次数
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return {v: k for k, v in count.items()}[max(count.values())]  # 形如dict[*]，输出的是值
    # return {v: k for k, v in count.items()}.values()


def majority_element_2(nums):
    """
    法2：数学统计
    :param nums:
    :return:
    """
    count, res = 0, nums[0]       # 初始化计数器和结果
    for i in range(len(nums)-1):  # 遍历数组中每一个数
        if nums[i] == res:        # 如果当前的数和结果变量相同
            count += 1            # 计数器+1
        else:                     # 否则
            count -= 1            # 计数器-1
            if count == 0:        # 如果减到了0
                res = nums[i+1]   # 那么更新结果变量为下一个数
    return res                    # 返回结果


def majority_element_3(nums):
    """
    法3：利用题目里面的漏洞，大于n/2
    :param nums:
    :return:
    """
    nums.sort()
    return nums[len(nums)//2]


print(majority_element_2([2, 2, 3, 3, 3, 2, 2]))
