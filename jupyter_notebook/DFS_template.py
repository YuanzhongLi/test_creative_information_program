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
from collections import deque

# グラフの集合のパターン
# graphは隣接リスト
def dfs(graph):
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達 
    color = [0 for _ in range(node_num)]

    for s in range(node_num):
        if (color[s] == 2):
            continue
        q = deque([s])
        color[s] = 1
        while (len(q) > 0):
            u = q.pop()
            color[u] = 2
            for v in graphs[u]:
                if color[v] == 0:
                    q.append(v)
                    color[v] = 1
    return


# -

# 全ノードが一つのグラフ(連結している)パターン
# graphは隣接リスト
def bfs(graph, s):
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達 
    color = [0 for _ in range(node_num)]
    q = deque([s])
    color[s] = 1
    while (len(q) > 0):
        u = q.pop()
        color[u] = 2
        for v in graphs[u]:
            if color[v] == 0:
                q.append(v)
                color[v] = 1
    return
