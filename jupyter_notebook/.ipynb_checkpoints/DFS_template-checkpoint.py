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

# graphsはgraphの集合で隣接行列
def bfs(graphs):
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達 
    color = [0 for _ in range(node_num)]

    for start in range(node_num):
        if (color[start] == 2):
            continue
        q = deque([start])
        color[start] = 1
        while (len(q) > 0):
            u = q.popleft()
            color[u] = 2
            for v in graph[u]:
                if color[v] == 0:
                    q.append(v)
                    color[v] = 1
    return
