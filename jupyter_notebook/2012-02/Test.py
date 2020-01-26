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
import random 

def make_data(file_path, data_num):
    with open(file_path, 'w', encoding='ascii') as f:
        for i in range(data_num):            
            x = random.randrange(30)
            y = random.randrange(30)
            if i < data_num-1:
                f.write('({0}, {1})\n'.format(x, y))
            else:
                f.write('({0}, {1})'.format(x, y))      
                
def make_data2(file_path, data_num):
    with open(file_path, 'w', encoding='ascii') as f:
        for i in range(data_num):            
            x = i
            y = None
            if i < 15:
                y = int(x * 0.5 + 2)
            else:
                y = int(4 * x - 50)
            if i < data_num-1:
                f.write('({0}, {1})\n'.format(x, y))
            else:
                f.write('({0}, {1})'.format(x, y))                  


# -

make_data('test001.txt', 30)
make_data2('test002.txt', 30)

# +
from PrintArray import PrintArray

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '({0}, {1})'.format(self.x, self.y)
    def __lt__(self, point):
        if self.y == point.y:
            return self.x < point.x
        else:
            return self.y < point.y
        
def inputdata(file_path):
    with open(file_path, 'r', encoding='ascii') as f:
        lines = f.readlines()
        ret = []
        for line in lines:
            line_list = line.strip().split(', ')
            p = Point(int(line_list[0][1:]), int(line_list[1][:-1]))
            ret.append(p)
        return ret
 
class DataGraph(object):
    def __init__(self):
        self.canvas = [[' ' for _ in range(64)] for _ in range(32)]
        for i in range(4):
            self.canvas[30-i*10][0] = str(i)
            if i > 0:
                self.canvas[30-i*10][1] = str(0)
        for i in range(30):
            self.canvas[29-i][2] = '|'
            
        self.canvas[30][2] = '+'        
        self.canvas[31][2] = str(0)
        
        for i in range(1, 4):
            self.canvas[31][2+i*20] = str(i)
            self.canvas[31][2+i*20+1] = str(0)   
        for i in range(3, 64):
            self.canvas[30][i] = '-'
            
    def show(self):
        PrintArray(self.canvas)
        
    def add(self, point, marker='*'):
            self.canvas[30-point.y][1+point.x*2+2] = marker

    def add_line_point(self, point, marker='o'):
        x = format_point5(point.x)
        i_x, s_x = divide(x)
        y = int(point.y)
        if x > 0:
            if s_x > 0:
                self.canvas[30-y][1+i_x*2+2] = marker
            else:
                self.canvas[30-y][1+i_x*2+1] = marker            
        

# 0.5刻みにformatする        
def format_point5(x):
    l = int(x // 1)
    r = l + 1
    m = l + 0.5
    abs_l = abs(x-l)
    abs_r = abs(x-r)
    abs_m = abs(x-m)
    tmp = [[abs_l, l], [abs_r, r], [abs_m, m]]
    tmp.sort()
    return tmp[0][1]

# intと小数に分ける
def divide(x):
    i = int(x // 1)
    return i, x - i     
        
def make_linear_data(a, b):
    ret = []
    s = set()
    esp = 1e-5
    for x in range(30):
        x1 = x
        y1 = int(a*x1+b - esp)
        x2 = x+0.5
        y2 = int(a*x2+b - esp)
        if not(y1 in s):
            s.add(y1)
            ret.append(Point(x1, y1))
        if not(y2 in s):
            s.add(y2)
            ret.append(Point(x2, y2))
    return ret

def calc_a_b(points):
    N = len(points)
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    
    for k in range(N):
        p = points[k]
        a1 += (p.x*p.y)
        a2 += p.x
        a3 += p.y
        a4 += p.x**2
    a1 *= N
    a4 *= N
    
    a = None
    if (a4 - a2**2) == 0:
        a = 1e9+7    
    else:
        a = (a1 - (a2 * a3)) / (a4 - a2**2)
    
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    
    for k in range(N):
        p = points[k]
        b1 += p.x**2
        b2 += p.y
        b3 += p.x*p.y
        b4 += p.x
    if (N*b1 - b4**2) == 0:
        b = 1e9+7
    else:
        b = (b1*b2 - b3*b4)/(N*b1 - b4**2)
    
    return a, b

def calc_E(a1, b1, a2, b2, xm, points):
    ret = 0
    for p in points:
        if p.x < xm:            
            ret += (abs(p.y - (a1*p.x+b1)))**2
        else:
            ret += (abs(p.y - (a2*p.x+b2)))**2
    return ret

def divide_points_by_xm(points, xm):
    ret1 = []
    ret2 = []
    for p in points:
        if p.x < xm:
            ret1.append(p)
        else:
            ret2.append(p)
    return ret1, ret2
        
def solve1():
    points = inputdata('test001.txt')
    points.sort()
    print(points[-1])
    return  

def solve2():
    points = inputdata('test001.txt')
    DG = DataGraph()
    for p in points:
        DG.add(p)
    DG.show()
    return
        
def solve3():
    points = make_linear_data(0.8, 2.0)
    DG = DataGraph()
    for p in points:
        DG.add_line_point(p)
    DG.show()
    return

def solve4():
    points = inputdata('test001.txt')    
    DG = DataGraph()
    a, b = calc_a_b(points)
    l_points = make_linear_data(a, b)
    for p in points:
        DG.add(p)
    for p in l_points:
        DG.add_line_point(p)
    DG.show()
    return

def solve5():
    points = inputdata('test002.txt')    
    DG = DataGraph()
    ans_a1 = None
    ans_b1 = None
    ans_a2 = None
    ans_b2 = None
    ans_xm = None
    e = 1e9+7
    for i in range(60):
        xm = 0.5 * i
        ps1, ps2 = divide_points_by_xm(points, xm)
        ps1.append(Point(xm, ))
        if len(ps1) == 0:
            a2, b2 = calc_a_b(ps2)
            em = calc_E(a2, b2, a2, b2, xm, points)
            if em < e:
                e = em
                ans_a1 = a2
                ans_b1 = b2
                ans_a2 = a2
                ans_b2 = b2
                ans_xm = xm
        elif len(ps2) == 0:
            a1, b1 = calc_a_b(ps1)
            em = calc_E(a1, b1, a1, b1, xm, points)
            if em < e:
                e = em
                ans_a1 = a1
                ans_b1 = b1
                ans_a2 = a1
                ans_b2 = b1
                ans_xm = xm
        else:
            a1, b1 = calc_a_b(ps1)
            a2, b2 = calc_a_b(ps2)
            em = calc_E(a1, b1, a2, b2, xm, points)
            if em < e:
                e = em
                ans_a1 = a1
                ans_b1 = b1
                ans_a2 = a2
                ans_b2 = b2
                ans_xm = xm
    print(ans_a1, ans_b1, ans_a2, ans_b2, ans_xm)
    return


# -

solve5()
