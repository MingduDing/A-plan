#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/22 14:26
# @Author:   Domi
# @File:     exam125.py
# @Software: PyCharm

"""
125.《验证回文串》（easy）

题目：给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写

思路：“filter(str.isalnum,s)”即只保留s中属于字母和数字的字符，使用“join”方法把保留
的字符串联起来，并用lower方法将所有大写字符转为小写字符
"""


def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
