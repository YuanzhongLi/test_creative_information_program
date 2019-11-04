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
def divisors(n):
    ret = []
    end = int(sqrt(n)) + 1
    for i in range(1, end+1):
        if (n % i == 0):
            ret.append(i)
            if (i * i != n):
                ret.append(int(n / i))
    ret.sort()             
    return ret


divisors(100)
