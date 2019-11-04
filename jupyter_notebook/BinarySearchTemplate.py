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

# +
def solve(mid):
    return True

def BS():
    ok = 1000 # 実在解
    ng = -1 # 非実在解
    while (abs(ok - ng) > 1):
        mid = int((ok + ng) / 2)
        if solve(mid) :
            ok = mid
        else:
            ng = mid
        
    return ok # ok が最終的な存在する実解    
