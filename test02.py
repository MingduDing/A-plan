"""
必选参数：变化大的在前，变化小的在后
默认参数：可以简化函数的调用，必须指向不变参数
可变参数：传入的参数个数可变，可以是0个。*args是可变参数，args接收的是一个tuple
命名关键字参数：命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数，限制关键字参数
关键字参数：允许传入0个或多个包含参数名的参数，在函数内部自动组成一个dict。**kw
"""
from os.path import join

"""
汉诺塔
"""
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)  # 把a上的n-1个盘子借助c移动到b
#         move(1, a, b, c)  # 把a上的1个盘子移动到c
#         move(n-1, b, a, c)  # 把b上的n-1个盘子借助a移动到c
# move(4, 'A', 'B', 'C')

"""
冒泡排序
"""
# def bubble_sort(alist):
#     for i in range(len(alist)-1, 0, -1):
#         for j in range(i):
#             if alist[j] > alist[j+1]:
#                 alist[j], alist[j+1] = alist[j+1], alist[j]
# a = [12, 4, 57, 19, 35, 47, 88, 24, 33, 19, 29, 56]
# bubble_sort(a)
# print(a)


"""
python 实现字符串大小写互换
A~Z 65~90
a~z 97~122
大小写之间相差35
ord()函数将字符串转化为ASCII码
chr()函数将ASCII码转化为字符串
"""
# def size_type(character):
#     n = len(character)
#     for i in range(n):
#         if 96 < ord(character[i]) < 127:
#             print(chr(ord(character[i]) - 32), end='')
#         elif 65 < ord(character[i]) < 90:
#             print(chr(ord(character[i]) + 32), end='')
#         else:
#             print(character[i], end='')
# string = 'My Name is DOMI'
# size_type(string)

"""
分段函数递归实现
"""
# def my_pow(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return pow(n, my_pow(n-1))
# print(my_pow(4))

"""
凯撒密码
"""
# s = input()
# t = ''
# for c in s:
#     if 'a' <= c <= 'z':
#         t += chr(ord('a') + (ord(c)-ord('a')+3) % 26)
#     elif 'A' <= c <= 'Z':
#         t += chr(ord('A') + (ord(c)-ord('A')+3) % 26)
#     else:
#         t += c
# print(t)

"""
最大乘积
"""
# def max_multiply(alist):
#     alist.sort(reverse=True)
#     return max(alist[0]*alist[1]*alist[2], alist[0]*alist[-2]*alist[-1])
#
# n = int(input())
# nums = list(map(int, input().split()))
# print(nums)
# print(max_multiply(nums))

"""
大字符串两数相乘
"""
# s1, s2 = input().split()
# ret = [0 for _ in range(len(s2)+len(s1))]  # 创建一个空数组
# for x in range(len(s2)):
#     for y in range(len(s1)):
#         ret[x+y+1] += int(s2[x])*int(s1[y])
# for i in range(len(ret)-1, 0, -1):
#     ret[i-1] += ret[i]//10
#     ret[i] %= 10
# if ret[0] == 0:
#     del ret[0]
# print(''.join(map(str, ret)))

"""
二分法递归实现
"""
# def binary_chop(alist, data):
#     n = len(alist)
#     if n < 1:
#         return False
#     mid = n // 2
#     if alist[mid] > data:
#         return binary_chop(alist[0:mid], data)
#     elif alist[mid] < data:
#         return binary_chop(alist[mid+1:], data)
#     else:
#         return True

"""
递归计算n！
"""
# from functools import reduce
# n = 10
# value = reduce(lambda x, y: x*y, range(1, n+1))
# print(value)

"""
递归实现斐波那契数列
"""
# alist = []
# for i in range(100):
#     if i == 0 or i == 1:
#         alist.append(1)
#     else:
#         alist.append(alist[i-1] + alist[i-2])
# print(alist)

"""
幂的递归
"""
# def foo(x, n):
#     if n == 0:
#         return 1
#     elif n == 2:
#         return x*x
#     else:
#         return foo(foo(x, n/2), 2) if not n % 2 else x*foo(foo(x, n//2), 2)
# y = 2
# m = 3
# print(foo(y, m))

"""
进制转换
"""
# def dec2bin(nums):
#     res = ''                        # 初始化空字符串res
#     if nums:                        # 如果输入nums不为空
#         res = dec2bin(nums // 2)    # 取商，一直除到nums为0
#         return res + str(nums % 2)  # 取余，倒序输出
#     else:                           # 否则
#         return res                  # 返回原值
# print(dec2bin(10))
# num = int(input('输入十进制数值：'))
# res = ''
# while True:
#     con = num // 2
#     rem = num % 2
#     res += str(rem)
#     if con == 0:
#         break
#     num = con
# for i in range(len(res)-1, -1, -1):
#     print(res[i], end='')

"""
合法IP
"""
# def legal_ip(address):
#     ip = address.split('.')
#     if int(ip[0]) == 0:
#         return False
#     return True if [1]*4 == [i.isdigit() and 0 <= int(i) <= 250 for i in ip] else False
# print(legal_ip('0.192.192.168'))


"""
统计字符串中各字符个数
"""
# a_str = input('请输入字符串：')
# res = {}
# for i in a_str:
#     res[i] = a_str.count(i)
# print(res)
# message = 'absdheowhfasckhkda'
# count = {}
# for i in message:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] += 1
# print(count)

"""
螺旋数组顺时针输出
"""
# def foo(matrix):
#     if len(matrix) == 0 or len(matrix[0]) == 0:
#         return []
#     ans = []
#     left, up, down, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
#     while left <= right and up <= down:
#         for i in range(left, right + 1):
#             ans += matrix[up][i],
#         up += 1
#         for i in range(up, down + 1):
#             ans += matrix[i][right],
#         right -= 1
#         for i in reversed(range(left, right + 1)):
#             ans += matrix[down][i],
#         down -= 1
#         for i in reversed(range(up, down + 1)):
#             ans += matrix[i][left],
#         left += 1
#     nums = ans[:(len(matrix) * len(matrix[0]))]
#     for i in nums[:-2]:
#         print(i, end=',')
#     return nums[-1]
#
#
# m, n = map(int, input().split())
# data = []
# count = 0
# while count < m:
#     s = input()
#     if s != '':
#         temp = [int(i) for i in s.split()]
#         data.append(temp)
#         count += 1
#     else:
#         break
# print(foo(data))
