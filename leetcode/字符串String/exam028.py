#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/21 14:03
# @Author:   Domi
# @File:     exam028.py
# @Software: PyCharm

"""
028.《实现strStr()》（easy）

题目：给定一个haystack字符串和一个needle字符串，在haystack字符串中找出needle字符串
出现的第一个位置(从0开始)。如果不存在，则返回-1

思路：遍历一遍
"""


def str_str(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


print(str_str('hello', 'll'))
