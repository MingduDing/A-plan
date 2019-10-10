#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/22 14:49
# @Author:   Domi
# @File:     exam205.py
# @Software: PyCharm

"""
205.《同构字符串》（easy）

题目：给定两个字符串s和t，判断它们是否是同构的。如果s中的字符可以被替换得到t，那么这两个字符串是同构的。所有
出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身

思路：去重，遍历，哈希表
"""


def is_isomorphic_1(s, t):
    """
    法1：去重
    """
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


def is_isomorphic_2(s, t):
    """
    法2：遍历
    """
    for i in range(len(s)):
        if s[i+1:].find(s[i]) != t[i+1:].find(t[i]):
            return False
    return True


def is_isomorphic_3(s, t):
    """
    法3：哈希表
    """
    d = {}
    for i, v in enumerate(s):
        if v not in d:
            if t[i] in d.values():  # 如果相同位置出现同一个元素直接返回False
                return False
            else:
                d[v] = t[i]         # {'p':'t', 'a':'i', 'e':'l', 'r':'e'}
        if d[v] != t[i]:            # if v in d: d[v]是key，t[i]是value
            return False
    return True


print(is_isomorphic_3('paper', 'title'))
