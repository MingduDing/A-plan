#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:     2019/8/5 17:11
# @Author:   Domi
# @File:     exam003.py
# @Software: PyCharm

"""
《六一儿童节》

题目：六一儿童节，老师带了很多好吃的巧克力到幼儿园。每块
巧克力j的重量为w[j]，对于每个小朋友i，当他分到的巧克力大
小达到h[i] (即w[j]>=h[i])，他才会上去表演节目。老师的目
标是将巧克力分发给孩子们，使得最多的小孩上台表演。可以保
证每个w[i]> 0且不能将多块巧克力分给一个孩子或将一块分给
多个孩子

思路：贪心
"""