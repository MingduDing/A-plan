#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/6 13:38
# @Author:   Domi
# @File:     exam189.py
# @Software: PyCharm

"""
189.《旋转数组》（easy）

题目：给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数

思路：4种
"""


def rotate_1(nums, k):
    """
    法1：一步一步旋转，单独写一个旋转一步的函数
    :param k:
    :param nums:
    :return:
    """
    def rotate_1_step(num):
        """
        实现旋转一步的操作
        :param num:
        :return:
        """
        tmp = num[-1]
        for i in range(len(num)-1, 0, -1):
            num[i] = num[i-1]
        num[0] = tmp

    for _ in range(k):
        rotate_1_step(nums)

    return nums


def rotate_2(nums, k):
    """
    法2：列表连接，注意k的取值可能大于列表长度，需要进行取余处理
    :param k:
    :param nums:
    :return:
    """
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


def rotate_3(nums, k):
    """
    法3：使用队列，每一步旋转可以看做弹出列表最后一个元素并加入到列表首端
    :param nums:
    :param k:
    :return:
    """
    for _ in range(k):
        nums.insert(0, nums.pop())  # pop弹出队尾元素
    return nums


def rotate_4(nums, k):
    """
    法4：双重逆序
    :param nums:
    :param k:
    :return:
    """
    k %= len(nums)
    nums[:] = reversed(nums)
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums


print(rotate_4([1, 2, 3, 4, 5, 6, 7], 3))
