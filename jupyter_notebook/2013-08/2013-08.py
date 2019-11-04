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

from numpy import sqrt


# (1
def R0_num(d):
    return (int(10.0 / d) + 1)**2


R0_num(1.001)


# +
# (2
def checkInside(x, y):
    return abs(x - 5.0)**2 + abs(y - 5.0)**2 <= 25.0

def R1_num(d):
    ret = 0
    col = row = int(10.0 / d) + 1
    for i in range(0, col):
        for j in range(0, row):
            if (checkInside(i * d, j * d)):
                ret += 1
    return ret

def solve(d):
    return (R1_num(d) / R0_num(d)) * 0.25


# -

solve(1.0)


# (3, 4
def solve(n):
    tmp_tri_area = 25.0 * sqrt(3.0)
    ret = tmp_tri_area
    increase = 3
    for i in range(0, n):
        tmp_tri_area /= 9
        ret += tmp_tri_area * increase
        increase *= 4

    return ret


solve(2)

# +
import sys
sys.path.append('..')

from Cordinate import *


# -

# (5, (6
def koch_points(n, p1, p2):
    ret = []
    def koch(n, p1, p2):
        if (n == 0):
            return
        s = p1 + (p2 - p1) / 3
        u = p1 + 2 * (p2 - p1) / 3
        t = rotate(u, s, 60)
        koch(n - 1, p1, s)
        ret.append(s)
        koch(n - 1, s, t)
        ret.append(t)
        koch(n - 1, t, u)
        ret.append(u)
        koch(n - 1, u, p2)
    koch(n, p1, p2)
    ret.insert(0, p1)
    ret.append(p2)
    return ret


def solve(d, n):
    p1 = Point(0, 0)
    p2 = Point(5, 5 * sqrt(3))
    p3 = Point(10, 0)
    polygon = []
    tmp1 = koch_points(n, p1, p2)
    polygon.extend(tmp1)
    polygon.pop(-1)
    tmp2 = koch_points(n, p2, p3)
    polygon.extend(tmp2)
    polygon.pop(-1)
    tmp3 = koch_points(n, p3, p1)
    polygon.extend(tmp3)
    polygon.pop(-1)

    check_points = []

    # 負方向への行間隔数
    negative_rows = int((5 * sqrt(3) / 3) / d + 1e-12)
    # 正方向への行間隔数
    positive_rows = int(5 * sqrt(3) / d + 1e-12)
    # 列間隔数
    columns = int(10 / d + 1e-12)

    # y軸負方向のグリッドをcheck_pointsに追加（x軸含めない
    for i in range(1, negative_rows+1):
        for j in range(0, columns+1):
            check_p = Point(d * j, -(d * i))
            check_points.append(check_p)

    # y軸正方向のグリッドをcheck_pointsに追加（x軸含める
    for i in range(0, positive_rows+1):
        for j in range(0, columns+1):
            check_p = Point(d * j, d * i)
            check_points.append(check_p)

    ret = 0
    for i in range(0, len(check_points)):
        point = check_points[i]
        if (contains(polygon, point) > 0):
            ret += 1
    return ret


solve(1, 7)




