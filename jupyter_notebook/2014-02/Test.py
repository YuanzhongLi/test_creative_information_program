# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import sys
sys.path.append('..')

import numpy as np


def solve1(x):
    if (x <= 2):
        return 1
    else:
        return solve1(x - 1) + solve1(x - 2)


memo = [0] * 100
memo[0], memo[1] = 0, 1
def init():
    for i in range(2, 99):
        memo[i] = memo[i - 1] + memo[i - 2]
def solve2(x):
    init()
    return memo[x]


str1 = '00123456789012345678901234567890'
str2 = '00987654321098765432109876543210'


def solve3(s1, s2):
    carry = 0
    ret = ''
    for i in range(32):
        ch1 = s1[31 - i]
        ch2 = s2[31 - i]
        n1 = int(ch1)
        n2 = int(ch2)
        a = n1 + n2 + carry
        if (a >= 10):
            carry = 1
        else:
            carry = 0
        b = a % 10
        ret += str(b)
    return ret[::-1]



solve3(str1, str2)

memo = [0] * 141
memo[0], memo[1] = 0, 1
def init():
    for i in range(2, len(memo)):
        memo[i] = memo[i - 1] + memo[i - 2]
def solve4(x):
    init()
    return memo[x]


solve4(140)

str1 = '12345678901234567890123456789012'
str2 = '04'
def solve5(s1, s2):
    n1 = int(s1)
    n2 = int(s2)
    return n1 / (10**(31 - n2))


# +
def root(x):
    x = float(x)
    right = x
    left = 0.0
    esp = 1e-7
    while (abs(right - left) > esp):
        mid = (right + left) / 2
        if (mid * mid > x):
            right = mid
        else:
            left = mid
    return right        

def solve6():
    return (1 + root(5)) / 2


# +
# (a + b * root(5) / 2)** 2のa, b
def func1(a, b):
    new_a = int((a ** 2 + (b**2)*5) / 2)
    new_b = int(a * b)
    return new_a, new_b

# (a + b * root(5) / 2) * (c + d * root(5) / 2)
def func2(a, b, c, d):
    new_a = int((a * c + b * d * 5) / 2)
    new_b = int((a * d + b * c) / 2)
    return new_a, new_b

root5 = root(5)

class obj:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return '({0} + {1} * root5) / 2'.format(self.a, self.b)
    def cal(self):
        return (self.a + self.b * root5) / 2
    def f1(self):
        new_a, new_b = func1(self.a, self.b)
        return obj(new_a, new_b)

# (1+roo5/2)の2のindex-1乗のobjを格納
memo1 = [obj(0, 0)] * 9
memo1[1] = obj(1, 1)
def init_memo1():
    # 128 (2^7)まで計算
    for i in range(2, len(memo1)):
        memo1[i] = memo1[i - 1].f1()

init_memo1()

# ex) 139 = 128(2^7) + 8(2^3) + 2(2^1) + 1(2^0) = [1, 1, 0, 1, 0, 0, 0, 1]
def func3(x):
    ret = [0] * 8
    if (x >= 128):
        ret[7] = 1
        x -= 128
    if (x >= 64):
        ret[6] = 1
        x -= 64
    if (x >= 32):
        ret[5] = 1
        x -= 32
    if (x >= 16):
        ret[4] = 1
        x -= 16
    if (x >= 8):
        ret[3] = 1
        x -= 8
    if (x >= 4):
        ret[2] = 1
        x -= 4
    if (x >= 2):
        ret[1] = 1
        x -= 2
    if (x >= 1):
        ret[0] = 1
        x -= 1  
    return ret

def obj_mul(obj1, obj2):
    a = obj1.a
    b = obj1.b
    c = obj2.a
    d = obj2.b
    new_a, new_b = func2(a, b, c, d)
    return obj(new_a, new_b)

# (1+roo5/2)index乗のobjを格納
memo2 = [obj(0, 0)] * 141
memo2[1] = obj(1, 1)

for i in range(2, len(memo2)):
    digit2 = func3(i)
    obj_array = []
    for (index, j) in enumerate(digit2):
        if (j == 1):
            obj_array.append(memo1[index+1])
    tmp = obj_array[0]        
    for k in range(1, len(obj_array)):
        tmp = obj_mul(tmp, obj_array[k])
    memo2[i] = tmp


# -

def g(x):
    return memo2[x].cal() / root5


g(140)


def f(x):
    return solve4(x)


f(140) - g(140)


def solve8():
    Max = 0.0    
    for i in range(1, 141):
        Max = max(abs(f(i) - g(i)), Max)
    return Max        


solve8()


