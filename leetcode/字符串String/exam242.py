#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/22 16:34
# @Author:   Domi
# @File:     exam242.py
# @Software: PyCharm

"""
242.《有效的字母异位词》（easy）

题目：给定两个字符串s和t，编写一个函数来判断t是否是s的字母异位词

思路：
"""


def is_anagram(s, t):
    return sorted(s) == sorted(t)


print(is_anagram('anagram', 'nagaram'))
