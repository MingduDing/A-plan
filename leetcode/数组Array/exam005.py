#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/16 11:15
# @Author:   Domi
# @File:     exam005.py
# @Software: PyCharm

"""
005.《最长回文字串》（medium）

题目：给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度为1000

思路：动态规划
"""


def longest_palindrome(s):
    left = right = 0
    n = len(s)
    for i in range(n - 1):
        if 2 * (n - i) + 1 < right - left + 1:
            break
        l = r = i
        while l > 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        if r - l - 2 > right - left:
            left = l + 1
            right = r - 1
        l = i
        r = i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        if r - l - 2 > right - left:
            left = l + 1
            right = r - 1
    return s[left:right + 1]


print(longest_palindrome("babad"))
