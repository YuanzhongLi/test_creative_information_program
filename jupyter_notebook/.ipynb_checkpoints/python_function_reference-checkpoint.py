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


