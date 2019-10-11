# -*- coding: utf-8 -*-
# @Time: 2019/10/11 19:22
# @Author: Domi

count = 0
n = int(input())
num = [int(i) for i in input().split()]
nums = sorted(num, reverse=True)
i = 0
for j in range(1, n):
    if nums[i] >= 2 * nums[j]:
        nums[i] = nums[j]
        i += 1

print(len(set(nums)))
