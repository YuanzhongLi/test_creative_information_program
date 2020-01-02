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

# ### (1)
# 255 (11111111)
# 240 (11110000)

# ### (2)
# #### 2-1
# 111 -> 1
# 110 -> 0
# 101 -> 0
# 100 -> 1
# 011 -> 0
# 010 -> 1
# 001 -> 1
# 000 -> 0
# 150 (10010110) の一つ
#
# #### 2-2
# 111 -> 0, 1
# 110, 011 -> 0, 1
# 101 -> 0, 1
# 100, 001 -> 0, 1
# 010 -> 0, 1
# 000 -> 0, 1
# 2^6 = 64個

# +
# 2-3
from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def getReverse(n):
    bi = baseNumber(2, 8, n)
    b000 = bi[0]
    b001 = bi[1]
    b010 = bi[2]
    b011 = bi[3]
    b100 = bi[4]
    b101 = bi[5]
    b110 = bi[6]
    b111 = bi[7]
    bi[1], bi[3], bi[4], bi[6] = bi[4], bi[6], bi[1], bi[3]
    return biTo10(bi)  

def hasReverse(n):
    return n == getReverse(n)

def solve2_3():
    ret = 0
    for i in range(256):
        if hasReverse(i):
            ret += 1
    return ret    


# +
# solve2_3()

# +
# 3
from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def delta_func(M, l, c, r):
    bn = baseNumber(2, 8, M)
    index = biTo10([l, c, r])
    return bn[index]

def print_cell(cell):
    ret = ''
    for index, c in enumerate(cell):
        if index >= 100:
            break
        if c == 0:
            ret += '.'
        else:
            ret += '#'            
    print(ret)

    
def update_cell(M, cell):
    cell_size = len(cell)
    ret = [0 for _ in range(cell_size)]
    for i, c in enumerate(cell):
        l = cell[(i-1) % cell_size]
        r = cell[(i+1) % cell_size]
        ret[i] = delta_func(M, l, c, r)
    return ret         

def solve3_1(M):
    cell = [0 for _ in range(100)]
    cell[40] = 1
    print_cell(cell)
    for t in range(1, 51):
        cell = update_cell(M, cell)
        print_cell(cell)    


# -

solve3_1(90)

# +
from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def delta_func(M, l, c, r):
    bn = baseNumber(2, 8, M)
    index = biTo10([l, c, r])
    return bn[index]

def print_cell(cell):
    ret = ''
    for index, c in enumerate(cell):
        if index >= 100:
            break
        if c == 0:
            ret += '.'
        else:
            ret += '#'    
    print(ret)
    
def update_cell(M, cell):
    cell_size = len(cell)
    ret = [0 for _ in range(cell_size)]
    for i, c in enumerate(cell):
        l = cell[(i-1) % cell_size]
        r = cell[(i+1) % cell_size]
        ret[i] = delta_func(M, l, c, r)
    return ret

def initailize(i):
    bn = baseNumber(2, 7, i)
    cnt = 0
    for bi in bn:
        if bi == 1:
            cnt += 1
    if cnt == 3:
        return 1
    else:
        return 0

def solve3_2(M):
    cell = [0 for _ in range(123)]
    for i, c in enumerate(cell):
        cell[i] = initailize(i)
        
    print_cell(cell)
    for t in range(1, 51):
        cell = update_cell(M, cell)
        print_cell(cell)


# -

solve3_2(99)

# +
from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def delta_func(M, l, c, r):
    bn = baseNumber(2, 8, M)
    index = biTo10([l, c, r])
    return bn[index]

def print_cell(cell):
    ret = ''
    for index, c in enumerate(cell):
        if index >= 100:
            break
        if c == 0:
            ret += '.'
        else:
            ret += '#'    
    print(ret)
    
def update_cell(M, cell):
    cell_size = len(cell)
    ret = [0 for _ in range(cell_size)]
    for i, c in enumerate(cell):
        l = cell[(i-1) % cell_size]
        r = cell[(i+1) % cell_size]
        ret[i] = delta_func(M, l, c, r)
    return ret

def solve3_3(M):
    cell = []
    for zero_num in range(1, 41):
        array = []
        for i in range(zero_num):
            array.append(0)
        array.append(1)
        cell.extend(array)
            
    print_cell(cell)
    for t in range(1, 51):
        cell = update_cell(M, cell)
        print_cell(cell)


# -

solve3_3(129)

# +
# 4
from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def delta_func(M, l, c, r):
    bn = baseNumber(2, 8, M)
    index = biTo10([l, c, r])
    return bn[index]

def print_cell(cell):
    ret = ''
    for index, c in enumerate(cell):
        if index >= 100:
            break
        if c == 0:
            ret += '.'
        else:
            ret += '#'    
    print(ret)
    
def remake(cell):    
    div_idxs = []
    prev_c = -1
    for index, c in enumerate(cell):
        if c != prev_c:
            div_idxs.append(index)
            prev_c = c 
    div_idxs.append(len(cell))
    
    array = []
    for i in range(len(div_idxs) - 1):
        tmp = []
        l = div_idxs[i]
        r = div_idxs[i+1]
        for j in range(l, r):
            tmp.append(cell[j])
        array.append(tmp)
    
    ret = []
    isException = False
    for index, block in enumerate(array):
        content = block[0]
        size = len(block)
        if size >= 3:
            if content == 1:
                if index == 0:
                    isException = True
                ret.extend([1 for _ in range(size - 1)])
            elif content == 0:
                ret.extend([0 for _ in range(size + 1)])
        else:
            if content == 1:                
                ret.extend([1 for _ in range(size)])
            elif content == 0:
                ret.extend([0 for _ in range(size)])
    if isException:
        tmp = [ret[-1]]
        tmp.extend(ret[:-1])
        return tmp
    else:
        return ret
        
def update_cell(M, cell):
    cell_size = len(cell)
    ret = [0 for _ in range(cell_size)]
    for i, c in enumerate(cell):
        l = cell[(i-1) % cell_size]
        r = cell[(i+1) % cell_size]
        ret[i] = delta_func(M, l, c, r)
    return remake(cell)

def initailize(i):
    bn = baseNumber(2, 7, i)
    cnt = 0
    for bi in bn:
        if bi == 1:
            cnt += 1
    if cnt == 3:
        return 1
    else:
        return 0

def solve4_1(M):
    cell = [0 for _ in range(100)]
    for i, c in enumerate(cell):
        cell[i] = initailize(i)
        
    print_cell(cell)
    for t in range(1, 51):
        cell = update_cell(M, cell)
        print_cell(cell)
        if len(cell) < 3 or len(cell) > 2000:
            print('size-out-of-range')
            break


# -

solve4_1(53)

# +
from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def delta_func(M, l, c, r):
    bn = baseNumber(2, 8, M)
    index = biTo10([l, c, r])
    return bn[index]

def print_cell(cell):
    ret = ''
    for index, c in enumerate(cell):
        if index >= 100:
            break
        if c == 0:
            ret += '.'
        else:
            ret += '#'    
    print(ret)
    
def remake(cell):    
    div_idxs = []
    prev_c = -1
    for index, c in enumerate(cell):
        if c != prev_c:
            div_idxs.append(index)
            prev_c = c 
    div_idxs.append(len(cell))
    
    array = []
    for i in range(len(div_idxs) - 1):
        tmp = []
        l = div_idxs[i]
        r = div_idxs[i+1]
        for j in range(l, r):
            tmp.append(cell[j])
        array.append(tmp)
    
    ret = []
    isException = False
    for index, block in enumerate(array):
        content = block[0]
        size = len(block)
        if size >= 3:
            if content == 1:
                if index == 0:
                    isException = True
                ret.extend([1 for _ in range(size - 1)])
            elif content == 0:
                ret.extend([0 for _ in range(size + 1)])
        else:
            if content == 1:                
                ret.extend([1 for _ in range(size)])
            elif content == 0:
                ret.extend([0 for _ in range(size)])
    if isException:
        tmp = [ret[-1]]
        tmp.extend(ret[:-1])
        return tmp
    else:
        return ret
        
def update_cell(M, cell):
    cell_size = len(cell)
    ret = [0 for _ in range(cell_size)]
    for i, c in enumerate(cell):
        l = cell[(i-1) % cell_size]
        r = cell[(i+1) % cell_size]
        ret[i] = delta_func(M, l, c, r)
    return remake(cell)

def initailize(i):
    bn = baseNumber(2, 7, i)
    cnt = 0
    for bi in bn:
        if bi == 1:
            cnt += 1
    if cnt == 3:
        return 1
    else:
        return 0

def solve4_2(M):
    cell = []
    for zero_num in range(1, 11):
        array = []
        for i in range(zero_num):
            array.append(0)
        array.append(1)
        cell.extend(array)   
        
    print_cell(cell)
#     for t in range(1, 51):
    while True:
        cell = update_cell(M, cell)
        print_cell(cell)
        if len(cell) < 3 or len(cell) > 2000:
            print('size-out-of-range')
            break


# -

solve4_2(250)


