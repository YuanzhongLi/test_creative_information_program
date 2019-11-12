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

# (1)
file_path = 'image1.txt'
def solve(file_path):
    with open(file_path, mode='r') as f:
        ret = []
        lines = f.readlines()
        for line in lines:
            ret.extend(line.rstrip('\n').split(' '))  
        print(int(len(ret) / 3))


solve(file_path)

# +
# (2)
import sys
sys.path.append('..')

import IsStrNumber as isn
from Divisors import divisors

file_path = 'image1.txt'

def is_white(cell):
    total = 0
    for c in cell:
        total += c
    return total == (255 * 3)

def solve(file_path):
    array = []
    cells = []
    with open(file_path, mode='r') as f:        
        lines = f.readlines()
        for line in lines:
            array.extend(line.rstrip('\n').split(' '))               
        for i in range(0, int(len(array) / 3)):
            idx = i * 3
            cell = [isn.STRtoNumber(array[idx]), isn.STRtoNumber(array[idx+1]), isn.STRtoNumber(array[idx+2])]
            cells.append(cell)
        cell_num = len(cells)
        divs = divisors(cell_num)
        width = 0
        for div in divs:
            if (width != 0):
                break
            col_num = div
            row_num = int(cell_num / div)            
            for i in range(0, row_num):
                right_end_cell = cells[i * col_num + col_num - 1]
                if (not is_white(right_end_cell)):
                    break
                if (i == row_num - 1):
                    width = col_num
                    
    print(width)   


# -

solve(file_path)

# +
# (3)
import sys
sys.path.append('..')

import IsStrNumber as isn

import numpy as np

file_path = 'image1.txt'

def is_white(cell):
    total = 0
    for c in cell:
        total += c
    return total == (255 * 3)

def light_degree(cell):
    ret = 0
    for c in cell:
        ret += c**2
    return ret  

def solve(file_path):
    array = []
    cells = []
    with open(file_path, mode='r') as f:        
        lines = f.readlines()
        for line in lines:
            array.extend(line.rstrip('\n').split(' '))               
        for i in range(0, int(len(array) / 3)):
            idx = i * 3
            cell = [isn.STRtoNumber(array[idx]), isn.STRtoNumber(array[idx+1]), isn.STRtoNumber(array[idx+2])]
            cells.append(cell)
        cell_num = len(cells)
        divs = divisors(cell_num)
        
        cell_order = np.array(range(0, cell_num))
        def cmp(order):
            cell = cells[order]
            return light_degree(cell)
        sorted_cell_order = sorted(cell_order, key=cmp)
        cell_idx = sorted_cell_order[int(cell_num / 2)]
        print('index: {0}, {1}'.format(cell_idx, cells[cell_idx]))


# -

solve(file_path, 10)

# +
# (4)
import sys
sys.path.append('..')

import IsStrNumber as isn

import numpy as np

file_path = 'image1.txt'

def is_white(cell):
    total = 0
    for c in cell:
        total += c
    return total == (255 * 3)

def light_degree(cell):
    ret = 0
    for c in cell:
        ret += c**2
    return ret  

def solve(file_path, k):
    array = []
    cells = []
    with open(file_path, mode='r') as f:        
        lines = f.readlines()
        for line in lines:
            array.extend(line.rstrip('\n').split(' '))               
        for i in range(0, int(len(array) / 3)):
            idx = i * 3
            cell = [isn.STRtoNumber(array[idx]), isn.STRtoNumber(array[idx+1]), isn.STRtoNumber(array[idx+2])]
            cells.append(cell)
        cell_num = len(cells)
        
        cell_order = np.array(range(0, cell_num))
        def cmp(order):
            cell = cells[order]
            return light_degree(cell)
        
        sorted_cell_order = sorted(cell_order, key=cmp)
        
        def pr(index):
            print('index: {0}, {1}'.format(index, cells[index]))
            
        for i in range(0, k):
            idx = int(cell_num * i / k)
            cell_idx = sorted_cell_order[idx]
            pr(cell_idx)
        


# -

solve(file_path, 4)

# +
# (5)
import sys
sys.path.append('..')

import IsStrNumber as isn
from Divisors import divisors

import numpy as np

file_path = 'image1.txt'

def is_white(cell):
    total = 0
    for c in cell:
        total += c
    return total == (255 * 3)

def light_degree(cell):
    ret = 0
    for c in cell:
        ret += c**2
    return ret 

def distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1]) + abs(cell1[2] - cell2[2])

def solve(file_path, k):
    array = []
    cells = []
    with open(file_path, mode='r') as f:        
        lines = f.readlines()
        for line in lines:
            array.extend(line.rstrip('\n').split(' '))               
        for i in range(0, int(len(array) / 3)):
            idx = i * 3
            cell = [isn.STRtoNumber(array[idx]), isn.STRtoNumber(array[idx+1]), isn.STRtoNumber(array[idx+2])]
            cells.append(cell)
        cell_num = len(cells)
        
        cell_order = np.array(range(0, cell_num))
        def cmp(order):
            cell = cells[order]
            return light_degree(cell)
        
        sorted_cell_order = sorted(cell_order, key=cmp)
        
        def pr(index):
            print('index: {0}, {1}'.format(index, cells[index]))
        
        # 最終的なclassterを代表するcellに対応するindexを入れていく
        # initialize
        representative_cells = []
        
        # classterに属する画素indexをそのclasster(array)に格納して管理
        # initialize
        classter_cells_array = []
        for i in range(0, 11):
            classter_cells = []
            for j in range(0, k):
                classter_cells.append([])
            classter_cells_array.append(classter_cells)         
        
        def get_cell(order_idx):
            return cells[sorted_cell_order[order_idx]]
        
        # 並べ替えた後(sorted_cell_order)のindex: t = 0
        for i in range(0, k):
            idx = int(cell_num * i / k)
            representative_cells.append(get_cell(idx))        
        
        # cellを分類する
        def classify(t, idx):
            cell = get_cell(idx)            
            classified_idx = 0
            min_dis = 3000
            for i in range(0, k):
                representative_cell = representative_cells[i]
                dis = distance(representative_cell, cell)
                if (dis <= min_dis):
                    classified_idx = i
                    min_dis = dis 
            classter_cells_array[t][classified_idx].append(idx)
        
        # cellをclasster分け : t = 0
        for i in range(0, len(sorted_cell_order)):
            cell = get_cell(i)
            classify(0, i)        
        
        def center_cell(classter):
            r = 0
            g = 0
            b = 0
            for i in classter:
                cell = get_cell(i)
                r += cell[0]
                g += cell[1]
                b += cell[2]
            return [int(r / len(classter)), int(g / len(classter)), int(b / len(classter))]        
        
        for t in range(1, 11):
            for i in range(0, k):
                representative_cells[i] = center_cell(classter_cells_array[t-1][i])
            for j in range(0, len(sorted_cell_order)):
                cell = get_cell(j)
                classify(t, j)
                
        print(representative_cells)   


# -

solve(file_path, 4)

# +
# (6)
import sys
sys.path.append('..')

from math import sqrt

def intsqrt(num):
    return int(sqrt(num))

import IsStrNumber as isn
from Divisors import divisors

import numpy as np

file_path = 'image1.txt'

def is_white(cell):
    total = 0
    for c in cell:
        total += c
    return total == (255 * 3)

def light_degree(cell):
    ret = 0
    for c in cell:
        ret += c**2
    return ret 

def distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1]) + abs(cell1[2] - cell2[2])

def solve(file_path, k):
    array = []
    cells = []
    with open(file_path, mode='r') as f:        
        lines = f.readlines()
        for line in lines:
            array.extend(line.rstrip('\n').split(' '))               
        for i in range(0, int(len(array) / 3)):
            idx = i * 3
            cell = [isn.STRtoNumber(array[idx]), isn.STRtoNumber(array[idx+1]), isn.STRtoNumber(array[idx+2])]
            cells.append(cell)
        cell_num = len(cells)
        divs = divisors(cell_num)        
        
        # initialize
        cell_order = np.array(range(0, cell_num))
        def cmp(order):
            cell = cells[order]
            return light_degree(cell)
        
        sorted_cell_order = sorted(cell_order, key=cmp)
        
        def pr(index):
            print('index: {0}, {1}'.format(index, cells[index]))
        
        # 最終的なclassterを代表するcellに対応するindexを入れていく
        # initialize
        representative_cells = []
        
        # classterに属する画素indexをそのclasster(array)に格納して管理
        # initialize
        classter_cells_array = []
        for i in range(0, 11):
            classter_cells = []
            for j in range(0, k):
                classter_cells.append([])
            classter_cells_array.append(classter_cells)         
        
        def get_cell(order_idx):
            return cells[sorted_cell_order[order_idx]]
        
        # 並べ替えた後(sorted_cell_order)のindex: t = 0
        for i in range(0, k):
            idx = int(cell_num * i / k)
            representative_cells.append(get_cell(idx))        
        
        # cellを分類する
        def classify(t, idx):
            cell = get_cell(idx)            
            classified_idx = 0
            min_dis = 3000
            for i in range(0, k):
                representative_cell = representative_cells[i]
                dis = distance(representative_cell, cell)
                if (dis <= min_dis):
                    classified_idx = i
                    min_dis = dis 
            classter_cells_array[t][classified_idx].append(idx)
        
        # cellをclasster分け : t = 0
        for i in range(0, len(sorted_cell_order)):
            cell = get_cell(i)
            classify(0, i)        
        
        def center_cell(classter):
            r = 0
            g = 0
            b = 0
            for i in classter:
                cell = get_cell(i)
                r += cell[0]
                g += cell[1]
                b += cell[2]
            return [int(r / len(classter)), int(g / len(classter)), int(b / len(classter))]        
        
        for t in range(1, 11):
            for i in range(0, k):
                representative_cells[i] = center_cell(classter_cells_array[t-1][i])
            for j in range(0, len(sorted_cell_order)):
                cell = get_cell(j)
                classify(t, j)
                
        compressed_cells = []
        # initailize
        for i in range(0, cell_num):
            compressed_cells.append([])
        

        for i, classters in enumerate(classter_cells_array[10]):
            for idx in classters:
                original_idx = sorted_cell_order[idx]
                compressed_cells[original_idx] = representative_cells[i]       
                
        w = intsqrt(len(cells))
        h = w
        s = w * h * 3
        w_b = w.to_bytes(4, byteorder='big')
        h_b = h.to_bytes(4, byteorder='big')
        s_b = s.to_bytes(4, byteorder='big')
        
        attribute = [77, 77, 0, 42, 0, 0, 0, 8, 0, 7, 1, 0, 0, 4, 0, 0,
                  0, 1, 'w', 1, 1, 0, 4, 0, 0, 0, 1, 'h', 1, 2, 0, 3, 0, 0, 0, 3, 0, 0, 0, 98, 1, 6,
                  0, 3, 0, 0, 0, 1, 0, 2, 0, 0, 1, 17, 0, 4, 0, 0,
                  0, 1, 0, 0, 0, 104, 1, 21, 0, 3, 0, 0, 0, 1, 0, 3,
                  0, 0, 1, 23, 0, 4, 0, 0, 0, 1, 's', 0, 0,
                  0, 0, 0, 8, 0, 8, 0, 8]
                
        
        with open('image.tif', 'wb') as fout:
            for i in attribute:
                if (i == 'w'):
                    fout.write(w_b)
                elif (i == 'h'):
                    fout.write(h_b)
                elif (i == 's'):
                    fout.write(s_b)
                else:
                    fout.write(i.to_bytes(1, byteorder='big'))
            for cell in compressed_cells:
                for i in range(0, 3):
                    fout.write(cell[i].to_bytes(1, byteorder='big'))
        
# -

solve(file_path, 4)
