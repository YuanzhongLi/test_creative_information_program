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
    return (int(10.0 / d) + 1)**2;


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
def Kn_area(n):
    tmp_tri_area = 25.0 * sqrt(3.0)
    ret = tmp_tri_area
    increase = 3
    for i in range(0, n):
        tmp_tri_area *= 0.25
        ret += tmp_tri_area * increase
        increase *= 4
    
    return ret


Kn_area(2)

Kn_area(0) * 1.75


