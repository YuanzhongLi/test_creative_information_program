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

a = [1, 2]


def f1(x):
    x[0] = 100
    return


f1(a)
a


class Tmp(object):
    def __init__(self):
        self.a = [1, 2]
        self.b = 3
    def __repr__(self):
        return '{0}\n{1}'.format(self.a, self.b)            


def f2(tmp):
    a = tmp.a
    a[0] = 100
    b = tmp.b
    b = 100
    return 


t = Tmp()
f2(t)
t

# +
import copy as cp

def f3(tmp):
    a = cp.deepcopy(tmp.a)
    a[0] = 100
    b = tmp.b
    b = 100
    return

t2 = Tmp()
f3(t2)
t2
