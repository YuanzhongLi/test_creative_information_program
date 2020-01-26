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


# +
def func1(n):
    Max = 10000    
    memo = [0 for _ in range(Max)]
    memo[0] = 1
    mod = 1<<24
    for i in range(1, Max):
        memo[i] = (161 * memo[i-1]+2457) % mod
    return memo[n]

def func1_v2(n):
    Max = 1000000+7
    memo = [0 for _ in range(Max)]
    memo[0] = 1
    mod = 1<<24
    for i in range(1, Max):
        memo[i] = (161 * memo[i-1]+2457) % mod
    return memo[n]

def make_func2_memo(memo_size=10000):
    memo = [0 for _ in range(memo_size)]
    memo[0] = 1
    mod = 1<<26
    for i in range(1, len(memo)):
        memo[i] = (1103515245 * memo[i-1]+12345) % mod
    return memo

def get_min_k(memo_size=1000007):
    memo = make_func2_memo(memo_size)
    for k in range(1, memo_size):
        if memo[0] == memo[k]:
            return k
    return -1

def solve1():
    n = 100
    print(func1(n))
    
def solve2():
    Max = 100
    memo = [0 for _ in range(Max)]
    memo[0] = 1
    mod = 1<<24
    # f(0) = 1でodd
    cnt = 0
    for i in range(1, Max):
        memo[i] = (161 * memo[i-1]+2457) % mod
        if memo[i] % 2 == 0:
            cnt += 1
    print(cnt)
    
def solve3():
    Max = 100
    memo = [0 for _ in range(Max)]
    memo[0] = 1
    mod = 1<<24
    # f(0) = 1, i: even
    cnt = 0
    for i in range(1, Max):
        memo[i] = (161 * memo[i-1]+2457) % mod
        if i % 2 == 1 and memo[i] % 2 == 0:
            cnt += 1
    print(cnt)
    
def solve4():
    n = 1000000
    print(func1_v2(n))
    
def solve5():
    memo = make_func2_memo()
    print('g(2): ', memo[2])
    print('g(3): ', memo[3])    
    
def solve6():
    n = 1
    mod = 1<<26
    cur = 1
    k = 1
    while True:                
        cur = (1103515245 * cur+12345) % mod
        if cur == 1:
            break
        k += 1
        if k > 100000000:
            k = -1
            break
    return k 

def solve7():
    max_k = 67108864
    g_mod = 1<<26
    h_mod = 1<<10
    g_cur = 1
    h_cur = 1
    for k in range(1, max_k+1):
        g_cur = (1103515245 * g_cur+12345) % g_mod
        h_cur = g_cur % h_mod
#         print(g_cur, h_cur)
        if h_cur == 1:
            return k        
    return -1        


# -

solve1()

solve7()

2 << 26


