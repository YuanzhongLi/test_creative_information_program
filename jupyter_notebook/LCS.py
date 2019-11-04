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

s = "abracadabra"
t = "avadakedavra"


def LCS(s, t):    
    dp = np.zeros((len(s)+1, len(t)+1), dtype=np.int)
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


LCS(s, t)
