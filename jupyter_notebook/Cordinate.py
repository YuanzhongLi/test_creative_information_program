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
import numpy as np

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
    
    def __repr__(self):
        return "({0:.3f}, {1:.3f})".format(self.x, self.y)
            
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

# 二つのベクトルの位置関係
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

# 線分の交差判定
def intersect(p1, p2, p3, p4):
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and \
            ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)

def intersectSS(s1, s2):
    return intersect(s1.p1, s1.p2, s2.p1, s2.p2)

# 円と直線の交差判定
def intersectCL(c, l):
    return getDistanceLP(l, c.c) <= c.r

# 円と円の交差判定
def intersectCC(c1, c2):
    return getDistance(c1.c, c2.c) <= (c1.r + c2.r)

# 線分と線分の距離
def getDistance(s1, s2):
    if (intersectSS(s1, s2)):
        return 0.0
    return min(min(getDistanceSP(s1, s2.p1), getDistanceSP(s1, s2.p2)), \
               min(getDistanceSP(s2, s1.p1), getDistanceSP(s2, s1.p2)))

# 線分と線分の交点（必ず交点があり、それがどちらかの端点でない）
def getCrossPointSS(s1, s2):
    base = s2.p2 - s2.p1
    d1 = abs(cross(base, s1.p1 - s2.p1))
    d2 = abs(cross(base, s1.p2 - s2.p1))
    t = d1 / (d1 + d2)
    return s1.p1 + t * (s1.p2 - s1.p1)

# 円cと線分lの交点
def getCrossPoints(c, l):
    pr = project(l, c.c)
    e = (l.p2 - l.p1) / absP(l.p2 - l.p1)
    base = sqrt(c.r * c.r - norm(pr - c.c))
    return [pr + base * e, pr - base * e]

# 角度rad
def argRad(p):
    return np.arctan2(p.y, px)
# 角度deg
def argDeg(p):
    return np.rad2deg(argRad(p))

# 弧度法からベクトルへ a:スカラー, r:角度rad
def polar(a, r):
    return Point(np.cos(r) * a, np.sin(r) * a)
    
# 円c1と円c2の交点
def getCrossPointsCC(c1, c2):
    d = absP(c1.c - c2.c) # double
    a = np.arccos((c1.r * c1.r + d * d - c2.r * c2.r) / (2 * c1.r * d)) #double
    t = argRad(c2.c - c1.c) #double
    return [c1.c + polar(c1.r, t + a), c1.c + polr(c1.r, t - a)]

# 点の内包
# polygonはPointの集合:array
# polygon g, Point p
# 辺上にある場合は1, 内包の場合は2, 外の場合は0を返す
def contains(g, p):
    n = len(g)
    x = False
    for i in range(0, n):
        a = g[i] - p
        b = g[(i+1) % n] - p
        if (abs(cross(a, b)) < EPS and dot(a, b) < EPS):
            return 1
        if (a.y > b.y):
            a, b = b, a
        if (a.y < EPS and EPS < b.y and cross(a, b) > EPS):
            x = not x
        
    if (x):
        return 2
    else:
        return 0

# 点pを点baseP基準で角度theta<deg>回転する
def rotate(p, baseP, theta):
    rad_theta = np.deg2rad(theta)
    vec = p - baseP
    vecRotated = Point(vec.x * np.cos(rad_theta) - vec.y * np.sin(rad_theta), \
                       vec.x * np.sin(rad_theta) + vec.y * np.cos(rad_theta))
    return baseP + vecRotated
