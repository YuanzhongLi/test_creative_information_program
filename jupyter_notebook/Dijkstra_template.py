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
from PriorityQueue import PriorityQueue

class Pair(object):
    # nodeは節点の番号    
    def __init__(self, cost, node): 
        self.cost = cost
        self.node = node
        
    def __repr__(self):
        return 'cost: {0}, node: {1}'.format(self.cost, self.node)
    
    def __lt__(self, pair):
        return self.cost < pair.cost
    
class NeighborNode(object):
    # cost: 隣接するノードからのコスト, p_node: 隣接するノード
    def __init__(self, node, cost, p_node): 
        self.node = node
        self.cost = cost
        self.p_node = p_node
    
# graphは隣接リストで要素はNeighborNode型
def dijkstra(graph, s):
    node_num = len(graph)
    color = [0 for _ in range(node_num)] # 0: 未到達, 1: 到達, 2: 探索済み
    inf = int(1e9+7)
    d = [inf for _ in range(node_num)] # startからのコスト
    p = [-1 for _ in range(node_num)] # 親ノードの番号
    PQ = PriorityQueue([])
    
    d[s] = 0
    PQ.push(Pair(0, s))
    color[s] = 1
    
    while len(PQ) > 0:
        f_pair = PQ.pop()
        u = f_pair.node
        color[u] = 2
        
        for v_NBnode in graph[u]:
            v = v_NBnode.node
            if color[v] == 2:
                continue
            if d[v] > d[u] + v_NBnode.cost:
                d[v] = d[u] + v_NBnode.cost
                p[v] = u
                PQ.push(Pair(d[v], v))
                color[v] = 1
    return d, p

def getRoot(d, p, end):
    root = []
    inf = int(1e9+7)
    if d[end] < inf:
        parent = end
        while parent != -1:
            root.append(parent)
            parent = p[parent]
    
    return d[end], root[::-1]  
