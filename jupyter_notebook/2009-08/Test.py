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
from Unionfind import Unionfind

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '{0} {1}'.format(self.x, self.y)
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

class Rec:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.xw = x+w
        self.yh = y+h
        # 左下から時計回り
        self.p1 = Point(x, y)
        self.p2 = Point(x, y + h)
        self.p3 = Point(x + w, y + h)
        self.p4 = Point(x + w, y)
    def __repr__(self):
        return '{0} {1} {2} {3}'.format(self.x, self.y, self.w, self.h)
    def is_connected(self, rec):
        return (abs(self.x - rec.xw) <= (self.w + rec.w)) and \
               (abs(rec.x - self.xw) <= (self.w + rec.w)) and \
               (abs(self.y - rec.yh) <= (self.h + rec.h)) and \
               (abs(rec.y - self.yh) <= (self.h + rec.h)) and \
               (self.p1 != rec.p3) and \
               (self.p2 != rec.p4) and \
               (self.p3 != rec.p1) and \
               (self.p4 != rec.p2)
    def area(self):
        return self.w * self.h

class Cluster:
    def __init__(self):
        self.recs = []
        self.min_x = 1000
        self.max_x = -1
        self.min_y = 1000
        self.max_y = -1
    def __repr__(self):
        return str(self.recs)    
    def size(self):
        return len(self.recs)    
    def add_rec(self, rec):
        self.recs.append(rec)
        self.min_x = min(self.min_x, rec.x)
        self.min_y = min(self.min_y, rec.y)
        self.max_x = max(self.max_x, rec.xw)
        self.max_y = max(self.max_y, rec.yh)        
    def area(self):
        canvas = [[0 for _ in range(1051)] for _ in range(1051)]
        for rec in self.recs:
            for x in range(rec.x, rec.xw):
                for y in range(rec.y, rec.yh):
                    canvas[x][y] = 1
        area = 0
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                area += canvas[x][y]
        return area
    
def format_input(file_path):
    with open(file_path, 'r') as f:
        text_lines = f.readlines()
        ret = []
        for text in text_lines:
            if text[-1] == '\n':
                text = text[:-1]
            text_split = text.split(' ')
            x = int(text_split[0])
            y = int(text_split[1])
            w = int(text_split[2])
            h = int(text_split[3])
            ret.append(Rec(x, y, w, h))
    return ret 

recs = format_input('7.txt')

def make_clusters(recs):
    clusters = []
    unionfind = Unionfind(len(recs))
    for i in range(1, len(recs)):
        rec = recs[i]
        for j in range(i):            
            rec2 = recs[j]
            if rec.is_connected(rec2):                
                unionfind.unite(i, j)
    dic = {}            
    for index, key in enumerate(unionfind.par):
        if key in dic.keys():
            dic[key].append(index)
        else:
            dic[key] = [index]
    for value in dic.values():
        cluster = Cluster()
        for idx in value:
            cluster.add_rec(recs[idx])
        clusters.append(cluster)
    return clusters

def make_canvas(recs):
    canvas = [[0 for _ in range(1051)] for _ in range(1051)]
    for rec in recs:
        for x in range(rec.x, rec.xw):
            for y in range(rec.y, rec.yh):
                canvas[x][y] += 1
    maximum = 0
    for row in canvas:
        for n in row:
            maximum = max(maximum, n)
    return canvas, maximum

# def solve

# def solve3_1(file_path):
#     recs = format_input(file_path)
#     clusters = make_clusters(recs)
#     canvas, maximum = make_canvas(recs)
    


# -

def solve2(file_path):
    recs = format_input(file_path)
    for rec in recs:
        print(rec.area())


def solve3_1(file_path):
    recs = format_input(file_path)
    _, maximum = make_canvas(recs)
    print(maximum)


def solve3_2(file_path):
    recs = format_input(file_path)
    clusters = make_clusters(recs)
    print(len(clusters))


def solve3_3(file_path):
    recs = format_input(file_path)
    clusters = make_clusters(recs)
    tmp = []
    for cluster in clusters:
        tmp.append(cluster.size())
    print(max(tmp))    


def solve3_4(file_path):
    recs = format_input(file_path)
    clusters = make_clusters(recs)
    tmp = []
    for cluster in clusters:
        tmp.append(cluster.area())
    print(max(tmp))


solve3_4('7.txt')


def solve4_1(file_path):
    recs = format_input(file_path)
    canvas, maximum = make_canvas(recs)    
