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

# 左づめでの10進数xをdigits桁のN進数vectorにしてを返す
def baseNumber(N, digits, x):
    ret = [0 for _ in range(digits)]
    quotient = x
    counter = 0
    while quotient > 0:
        remainder = quotient % N
        quotient //= N
        ret[counter] = remainder
        counter += 1
    return ret;    


# +
# baseNumber(2, 10, 10)
# -

# 0からn-1までのN進数を上記のbaseNumberで返したvectorのvector
def baseNumbers(n, N, digits):
    ret = []
    for i in range(n):
        ret.append(baseNumber(N, digits, i))
    return ret

# +
# baseNumbers(10, 2, 4)
