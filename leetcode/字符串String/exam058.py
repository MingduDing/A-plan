#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/21 22:15
# @Author:   Domi
# @File:     exam058.py
# @Software: PyCharm

"""
058.《最后一个单词的长度》（easy）

题目：给定一个仅包含大小写字母和空格' '的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回0

思路：rstrip()和split()函数
"""


def length_of_last_word(s):
    if not s:
        return 0
    return len((s.rstrip()).split(' ')[-1])


print(length_of_last_word('hello world'))
