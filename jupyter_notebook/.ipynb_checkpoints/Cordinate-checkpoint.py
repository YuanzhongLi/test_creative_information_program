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

from math import sqrt

# +
EPS = 1e-10
class Point(object):
    def __init__(self, x:float, y:float):
        self.x = float(x)
        self.y = float(y)
    def __add__(a, b):
        return Point(a.x + b.x, a.y + b.y)
    def __sub__(a, b):
        return Point(a.x - b.x, a.y - b.y)
    def __mul__(self, other):
        return Point (other * self.x, other * self.y)
    def __rmul__(self, other):
        return Point (other * self.x, other * self.y)        
    def __truediv__(self, other):
        return Point(self.x / float(other), self.y / float(other))
    def __eq__(self, other):
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y
    def __str__(self):
        return "[{0}, {1}]".format(self.x, self.y)
    
    def norm(self):
        return self.x * self.x + self.y * self.y
    def abs(self):
        return sqrt(self.norm())
    
class Vector(object):
    def __init__(self, x:float, y:float):
        self.x = float(x)
        self.y = float(y)
    def __add__(a, b):
        return Point(a.x + b.x, a.y + b.y)
    def __sub__(a, b):
        return Point(a.x - b.x, a.y - b.y)
    def __mul__(self, other):
        return Point (other * self.x, other * self.y)
    def __rmul__(self, other):
        return Point (other * self.x, other * self.y)        
    def __truediv__(self, other):
        return Point(self.x / float(other), self.y / float(other))
    def __eq__(self, other):
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y
    def __str__(self):
        return "[{0}, {1}]".format(self.x, self.y)
    
    def norm(self):
        return self.x * self.x + self.y * self.y
    def abs(self):
        return sqrt(self.norm())
    


# +
def equals(a, b):
    return abs(a - b) < EPS

def normP(p):
    return p.x * p.x + p.y * p.y

def absP(p):
    return sqrt(normP(p))


# -

class Circle(object):
    def __init__(self, c:Point, r:float):
        self.c = c
        self.r = float(r)
    def __str__(self):
        return "center: {0}, radius: {1}".format(self.c, self.r)


class Segment(object):
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return "p1: {0}, p2: {1}".format(self.p1, self.p2)


# +
# 内積
def dot(a, b):
    return a.x * b.x + a.y * b.y

# 外積
def cross(a, b):
    return a.x * b.y - a.y * b.x

# 直行判定
def isOrthogonal(a, b):
    return equals(dot(a, b), 0.0)

# 平行判定
def isParallel(a, b):
    return equals(cross(a, b), 0.0)

# 射影
# s: Segment, p: Point
def project(s, p):
    base = s.p2 - s.p1
    r = dot(p - s.p1, base) / base.norm()
    return s.p1 + base * r

# 反射
def reflect(s, p):
    return p + (project(s, p) - p) * 2.0

# 点と点の距離
def getDistance(a, b):
    return absP(a - b)

# 点と直線の距離
# l: Segment, p: Point
def getDistanceLP(l, p):
    return abs(cross(l.p2 - l.p1, p - l.p1) / absP(l.p2 - l.p1))

# 点と線分の距離
def getDistanceSP(s, p):
    if dot(s.p2 - s.p1, p - s.p1) < 0.0:
        return absP(p - s.p1)
    if dot(s.p1 - s.p2, p - s.p2) < 0.0:
        return absP(p - s.p2)
    return getDistanceLP(s, p)

COUNTER_CLOCKWISE = 1; # 反時計回り
CLOCKWISE = -1;        # 時計回り
ONLINE_BACK = 2;       # 逆向き平行
ONLINE_FRONT = -2;     # 順向き平行
ON_SEGMENT = 0;        # 順向き線分上

# 二つの線分の位置関係
# p0-p1とp0-p2の関係
def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if cross(a, b) > EPS:
        return COUNTER_CLOCKWISE
    if cross(a, b) < -EPS:
        return CLOCKWISE
    if dot(a, b) < -EPS:
        return ONLINE_BACK
    if a.nomr() < b.norm():
        return ONLINE_FRONT
    return ON_SEGMENT


# -

a = Point(0, 0)
b = Point(2, 0)
c = Point(-1, 1)
d = Point(1, 1)
s = Segment(a, b)
ans = ccw(a, b, c)
print(ans)

a.dot(b)

c1 = Circle(a, 1)

print(c1)

import numpy as np

a = np.array([1, 3], dtype=np.float64)
b = np.array([1, 2], dtype=np.float64)



a 
