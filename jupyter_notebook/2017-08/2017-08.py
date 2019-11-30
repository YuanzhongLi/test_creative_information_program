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

# +
# (1) 
# A,Bそれぞれm^2n

# +
# (2)
file_path = 'mat1_sample.txt'

def solve():    
    with open(file_path, 'r') as f:
        text = f.read()
        text = text.split('.')[0]
        text_array = text.split(',')
        mat = []
        for text in text_array:
            row = text.split(' ')
            for index, strnum in enumerate(row):
                row[index] = int(strnum)
            mat.append(row)
        row_num = len(mat)
        col_num = len(mat[0])
        print(row_num, col_num)
    


# -

solve()

# +
# (3)
file_path1 = 'mat1_sample.txt'
file_path2 = 'mat2_sample.txt'
import numpy as np

def parse_file(file_path):    
    with open(file_path, 'r') as f:
        text = f.read()
        text = text.split('.')[0]
        text_array = text.split(',')
        mat = []
        for text in text_array:
            row = text.split(' ')
            for index, strnum in enumerate(row):
                row[index] = int(strnum)
            mat.append(row)
        return np.array(mat)
    
def solve(file_path1, file_path2):
    mat1 = parse_file(file_path1)
    mat2 = parse_file(file_path2)
    mat = np.dot(mat1, mat2)
    ans = 0    
    for i in range(0, len(mat)):
#         print(mat[i, i])
        ans += mat[i, i]
    return ans    


# -

solve(file_path1, file_path2)


# +
# (4)
class Ele(object):
    def __init__(self, mat_name:str, row:int, col:int):
        self.mat_name = mat_name
        self.row = row
        self.col = col
    def __repr(self):
        return 'mat_name: {0}, row_idx: {1}, col_idx: {2}'.fromat(self.mat_name, self.row, self.col)

def solve(m, n, s):
    # 次にpushするcacheのidx
    next_cache_idx = 0
    # cacheでidxに入っているものを指定
    cache = np.empty(s, dtype=Ele)
    # memmoryでmem_a[i, j] ai,jの入っているキャッシュのインデックスを返すキャッシュに入ってない場合-1
    mem_a = -1*np.ones((m, n), dtype=np.int)
    mem_b = -1*np.ones((n, m), dtype=np.int)
    a_num = 0
    b_num = 0
    for i in range(0, m):
        for j in range(0, m):
            for k in range(0, n):
                # ai,k
                if (mem_a[i, k] < 0): # キャッシュにない
                    a_num += 1
                    
                    if (cache[next_cache_idx] != None): # 入れるキャッシュの場所が空でない
                        # 追い出す
                        ele = cache[next_cache_idx]
                        # memを更新
                        if (ele.mat_name == 'A'):
                            mem_a[ele.row][ele.col] = -1
                        elif (ele.mat_name == 'B'):
                            mem_b[ele.row][ele.col] = -1
                    
                    ele = Ele('A', i, k)
                    cache[next_cache_idx] = ele # cacheに入れる
                    mem_a[i, k] = 1 # cacheにある
                    next_cache_idx += 1
                    if (next_cache_idx >= s):
                        next_cache_idx = 0
                # bk,j
                if (mem_b[k, j] < 0): # キャッシュにない
                    b_num += 1
                    
                    if (cache[next_cache_idx] != None): # 入れるキャッシュの場所が空でない
                        # 追い出す
                        ele = cache[next_cache_idx]
                        # memを更新
                        if (ele.mat_name == 'A'):
                            mem_a[ele.row][ele.col] = -1
                        elif (ele.mat_name == 'B'):
                            mem_b[ele.row][ele.col] = -1
                    
                    ele = Ele('B', k, j)
                    cache[next_cache_idx] = ele # cacheに入れる
                    next_cache_idx += 1
                    mem_b[k, j] = 1 # cacheにある
                    if (next_cache_idx >= s):
                        next_cache_idx = 0
    return a_num, b_num                            



# -

solve(8, 20, 40)


# +
# (5)
# u p v p w p
# -

# (6)
def solve(m, n, p, s):    
    # cacheでidxに入っているものを指定
    cache = np.empty(s, dtype=Ele)
    # memmoryでmem_a[i, j] ai,jの入っているキャッシュのインデックスを返すキャッシュに入ってない場合-1
    mem_a = -1*np.ones((m, n), dtype=np.int)
    mem_b = -1*np.ones((n, m), dtype=np.int)
    data = { 'a_num': 0, 'b_num': 0, 'next_cache_idx': 0 }
    
    def check_cache():
        if (cache[data['next_cache_idx']] != None): # 入れるキャッシュの場所が空でない
            ele = cache[data['next_cache_idx']]
            # memを更新
            if (ele.mat_name == 'A'):
                mem_a[ele.row][ele.col] = -1
            elif (ele.mat_name == 'B'):
                mem_b[ele.row][ele.col] = -1
                
    def check_A(i, k):
        if (mem_a[i, k] < 0): # キャッシュにない
            data['a_num'] += 1

            check_cache()

            ele = Ele('A', i, k)
            cache[data['next_cache_idx']] = ele # cacheに入れる
            data['next_cache_idx'] += 1
            mem_a[i, k] = 1
            if (data['next_cache_idx'] >= s):
                data['next_cache_idx'] = 0
    
    def check_B(k, j):
        if (mem_b[k, j] < 0): # キャッシュにない
            data['b_num'] += 1

            check_cache()

            ele = Ele('B', k, j)
            cache[data['next_cache_idx']] = ele # cacheに入れる
            data['next_cache_idx'] += 1
            mem_b[k, j] = 1
            if (data['next_cache_idx'] >= s):
                data['next_cache_idx'] = 0
    
    u = 0
    while (u < m):
        v = 0
        while (v < m):
            w = 0
            while (w < n):
                i = u
                while (i < u + p):
                    j = v
                    while (j < v + p):
                        k = w
                        while (k < w + p):
                            # ai,k
                            check_A(i,k)
                            # bk,j
                            check_B(k,j)
                            k += 1
                        j += 1
                    i += 1
                w += p
            v += p
        u += p
                            
    return data
    


solve(8, 20, 4, 40)

# +
# (7)
import math
import sys
sys.path.append('..')

from Divisors import *

def gcd(m, n):
    return math.gcd(m, n)

def get_p(m, n, s):
    g = gcd(m, n)
    g = gcd(g, s)
    tmp = int(m * n / g)
    divs = divisors(tmp)
    tmp1 = divs[int(len(divs) / 2)]
    tmp2 = divs[int(len(divs) / 2) + 1]
    
    

def solve(m, n, s):
    p = 50
    # cacheでidxに入っているものを指定
    cache = np.empty(s, dtype=Ele)
    # memmoryでmem_a[i, j] ai,jの入っているキャッシュのインデックスを返すキャッシュに入ってない場合-1
    mem_a = -1*np.ones((m, n), dtype=np.int)
    mem_b = -1*np.ones((n, m), dtype=np.int)
    data = { 'a_num': 0, 'b_num': 0, 'next_cache_idx': 0 }
    
    def check_cache():
        if (cache[data['next_cache_idx']] != None): # 入れるキャッシュの場所が空でない
            ele = cache[data['next_cache_idx']]
            # memを更新
            if (ele.mat_name == 'A'):
                mem_a[ele.row][ele.col] = -1
            elif (ele.mat_name == 'B'):
                mem_b[ele.row][ele.col] = -1
                
    def check_A(i, k):
        if (mem_a[i, k] < 0): # キャッシュにない
            data['a_num'] += 1

            check_cache()

            ele = Ele('A', i, k)
            cache[data['next_cache_idx']] = ele # cacheに入れる
            data['next_cache_idx'] += 1
            mem_a[i, k] = 1
            if (data['next_cache_idx'] >= s):
                data['next_cache_idx'] = 0
    
    def check_B(k, j):
        if (mem_b[k, j] < 0): # キャッシュにない
            data['b_num'] += 1

            check_cache()

            ele = Ele('B', k, j)
            cache[data['next_cache_idx']] = ele # cacheに入れる
            data['next_cache_idx'] += 1
            mem_b[k, j] = 1
            if (data['next_cache_idx'] >= s):
                data['next_cache_idx'] = 0
    
    u = 0
    while (u < m):
        v = 0
        while (v < m):
            w = 0
            while (w < n):
                i = u
                while (i < u + p):
                    j = v
                    while (j < v + p):
                        k = w
                        while (k < w + p):
                            # ai,k
                            check_A(i,k)
                            # bk,j
                            check_B(k,j)
                            k += 1
                        j += 1
                    i += 1
                w += p
            v += p
        u += p
                            
    return data


# -

solve(200, 150, 600)

cache[0] != None

gcd(200, 150)

int(3/2)


