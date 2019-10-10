#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/7/12 15:48
# @Author : Domi
# @File : exam066.py
# @Software: PyCharm

"""
66.加一（easy）

题目：给定一个由整数组成的非空数组所表示的非负整数，在该数基
础上加一。最高位数字存放在数组首位，数组中每个元素只存储一个
数字。可以假设除了整数0之外，这个整数不会以0开头。

思路：%取余是取出个位，//取商是踢掉个位。从后向前遍历，取出
个位加1然后取余，和原位进行比较，小就给carry赋值1，否则赋
值0。考虑特殊情况：最高位有进位时，需要补位。
"""


def plus_one(digits):
    """
    66.加一
    :param digits: 非负整数
    :return: digits
    """
    n = len(digits)
    carry = 1  # 设定一个进位

    for i in range(n-1, -1, -1):  # 倒序取数
        digit = (digits[i] + carry) % 10  # 个位（最低位）加1取余，传给digit
        carry = 1 if digit < digits[i] else 0  # 可以借鉴这个写法
        digits[i] = digit
    if carry == 1:
        print([1] + digits)  # 有进位时首位（最高位）补1
    else:
        print(digits)


plus_one([1, 3, 9])


