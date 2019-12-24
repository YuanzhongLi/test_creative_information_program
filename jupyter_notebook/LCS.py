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

import numpy as np


def LCS(s, t):    
    # dp[i, j]: sのi番目までの文字列とtのj番目までの文字列を比較した時のlcs
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        x = s[i - 1]
        for j in range(1, len(t) + 1):
            y = t[j - 1]
            if (x == y):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    ret = ""
    i = len(s)
    j = len(t)
    # 後ろから格納してlcs文字列を作成
    while (1):
        if (i == 0 or j == 0):
            break
        if (dp[i][j] == dp[i-1][j]):
            i-=1
        elif (dp[i][j] == dp[i][j-1]):
            j-=1
        else:
            i-=1
            j-=1
            ret+=s[i]
    # string reverse
    return ret[::-1]


LCS("abracadabra", "avadakedavra")
