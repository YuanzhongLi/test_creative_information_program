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

import sys
sys.path.append('..')

import numpy as np


# +
# (1)
def format_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        ret = []
        for line in lines:
            if line[-1] == '\n':
                tmp = line[:-1]
                tmp_array = tmp.split('->')
                ret.append([int(tmp_array[0]), int(tmp_array[1])])
            else:
                tmp_array = line.split('->')
                ret.append([int(tmp_array[0]), int(tmp_array[1])])
        return ret 
    
class Edge(object):
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to
    def __repr__(self):
        return '{0}->{1}'.format(self.fr, self.to)
    def __eq__(self, edge):
        return (self.fr == edge.fr) and (self.to == edge.to)
    def __hash__(self):
        return hash('{0}->{1}'.format(self.fr, self.to))
    
def isCycle(graph):
    s = 0
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達 
    color = [0 for _ in range(node_num)]
    q = deque([s])
    color[s] = 1
    while (len(q) > 0):
        u = q.popleft()
        color[u] = 2
        for v in graph[u]:
            if v == 0:
                return True
            if color[v] == 0:
                q.append(v)
                color[v] = 1
    return False
    
def solve1(file_path):
    max_nodes = 10001
    orders = format_input(file_path)
    graph = [[] for _ in range(max_nodes)]
    reverse_graph = [[] for _ in range(max_nodes)]
    node_set = set([0])
    edge_set = set()
    cur_vt = 1
    cur_rt = 0
    ans3vt = None
    ans3rt = None
    ans4 = None
    for index, order in enumerate(orders):
        t = index+1
        x = order[0]
        y = order[1]
        node_set.add(x)
        node_set.add(y)
        edge = Edge(x, y)
        edge_set.add(edge)
        graph[x].append(y)
        reverse_graph[y].append(x)       
        # 1-4
        if isCycle(graph) and (ans4 == None):
            ans4 = t 
            
        # 1-3
        next_vt = len(node_set)
        next_rt = len(edge_set)
        if next_vt >= 1000 and cur_vt < 1000:
            ans3vt = t
        if next_rt >= 1000 and cur_rt < 1000:
            ans3rt = t
        cur_vt = next_vt
        cur_rt = next_rt
    # 1-1
    ans1 = len(node_set)
    # 1-2
    ans2_from_node = None
    ans2_from_node_num = 0
    ans2_to_node = None
    ans2_to_node_num = 0
    for v, g in enumerate(graph):
        if len(g) > ans2_from_node_num:
            ans2_from_node = v
            ans2_from_node_num = len(g)
    for v, rg in enumerate(reverse_graph):
        if len(rg) > ans2_to_node_num:
            ans2_to_node = v
            ans2_to_node_num = len(rg)
    print('1-1: {0}'.format(ans1))
    print('1-2:')
    print('最大出次数頂点: {0}, 出次数: {1}'.format(ans2_from_node, ans2_from_node_num))
    print('最大入次数頂点: {0}, 入次数: {1}'.format(ans2_to_node, ans2_to_node_num))
    print('1-3: tv= {0}, tr= {1}'.format(ans3vt, ans3rt))
    print('1-4: {0}'.format(ans4))               


# -

solve1('test001.txt')

# +
# (2)
from collections import deque

class Order(object):
    def __init__(self, x, y, t): # t:0 add, t:1 del
        self.x = x
        self.y = y
        self.t = t
    def __repr__(self):
        if self.t == 0:
            return '{0}->{1}'.format(self.x, self.y)
        else:
            return '!{0}->{1}'.format(self.x, self.y)
    def __hash__(self):
        if self.t == 0:
            return '{0}->{1}'.format(self.x, self.y)
        else:
            return '!{0}->{1}'.format(self.x, self.y)        
    def toString(self):
        if self.t == 0:
            return '{0}->{1}'.format(self.x, self.y)
        else:
            return '!{0}->{1}'.format(self.x, self.y)

def format_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        ret = []
        for line in lines:
            if line[-1] == '\n':
                tmp = line[:-1]
                tmp_array = tmp.split('->')
                x = int(tmp_array[0][-1])
                y = int(tmp_array[1])
                t = None
                if tmp_array[0][0] == '!':
                    t = 1
                else:
                    t = 0    
                order = Order(x, y, t)    
                ret.append(order)
            else:
                tmp_array = line.split('->')
                x = int(tmp_array[0][-1])
                y = int(tmp_array[1])
                t = None
                if tmp_array[0][0] == '!':
                    t = 1
                else:
                    t = 0    
                order = Order(x, y, t)    
                ret.append(order)
        return ret 
    
class Edge(object):
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to
    def __repr__(self):
        return '{0}->{1}'.format(self.fr, self.to)
    def __eq__(self, edge):
        return (self.fr == edge.fr) and (self.to == edge.to)
    def __hash__(self):
        return hash('{0}->{1}'.format(self.fr, self.to))
    
def getRt(graph):
    ret = set()
    s = 0
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達 
    color = [0 for _ in range(node_num)]
    q = deque([s])
    color[s] = 1
    while (len(q) > 0):
        u = q.popleft()
        ret.add(u)
        color[u] = 2
        for v in graph[u]:
            if color[v] == 0:
                q.append(v)
                color[v] = 1
    return ret

def make_graph(edge_set):
    max_nodes = 10001
    graph = [[] for _ in range(max_nodes)]
    for edge in edge_set:        
        graph[edge.fr].append(edge.to)
    return graph
    
def solve2(file_path):
    orders = format_input(file_path)        
    edge_set = set()
    isLT1000 = True # Rtが1000より小さいとき
    ans3 = []
    for index, order in enumerate(orders):
        t = index+1        
        if order.t == 0: # add
            x = order.x
            y = order.y
            edge = Edge(x, y)
            edge_set.add(edge)                    
            # t-1でRtが1000より小さくかつtのときにedgeの数が1000以上のとき
            if isLT1000 and len(edge_set) >= 1000:
                graph = make_graph(edge_set)
                Rt = getRt(graph)
                if len(Rt) >= 1000:
                    ans3.append(t)
                    isLT1000 = False
        if order.t == 1: # del
            x = order.x
            y = order.y
            edge = Edge(x, y)
            edge_set.remove(edge)
            # t-1でRtが1000以上のとき
            if not isLT1000:
                graph = make_graph(edge_set)
                Rt = getRt(graph)
                if len(Rt) < 1000:
                    isLT1000 = True                                                    
    # 2-1
    ans1 = len(edge_set)
    # 2-2    
    graph = make_graph(edge_set)
    Rt = getRt(graph)
    ans2 = len(Rt)
    print('2-1: {0}'.format(ans1))
    print('2-2: {0}'.format(ans2))    
    print('2-3: {0}'.format(ans3))


# -

solve2('test002.txt')

# +
# (3)-1
from collections import deque

class Order(object):
    def __init__(self, x, y, t): # t:0 add, t:1 del
        self.x = x
        self.y = y
        self.t = t
    def __repr__(self):
        if self.t == 0:
            return '{0}->{1}'.format(self.x, self.y)
        else:
            return '!{0}->{1}'.format(self.x, self.y)
    def __hash__(self):
        if self.t == 0:
            return '{0}->{1}'.format(self.x, self.y)
        else:
            return '!{0}->{1}'.format(self.x, self.y)        
    def toString(self):
        if self.t == 0:
            return '{0}->{1}'.format(self.x, self.y)
        else:
            return '!{0}->{1}'.format(self.x, self.y)

def format_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        ret = []
        for line in lines:
            if line[-1] == '\n':
                tmp = line[:-1]
                tmp_array = tmp.split('->')
                x = int(tmp_array[0][-1])
                y = int(tmp_array[1])
                t = None
                if tmp_array[0][0] == '!':
                    t = 1
                else:
                    t = 0    
                order = Order(x, y, t)    
                ret.append(order)
            else:
                tmp_array = line.split('->')
                x = int(tmp_array[0][-1])
                y = int(tmp_array[1])
                t = None
                if tmp_array[0][0] == '!':
                    t = 1
                else:
                    t = 0    
                order = Order(x, y, t)    
                ret.append(order)
        return ret 
    
class Edge(object):
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to
    def __repr__(self):
        return '{0}->{1}'.format(self.fr, self.to)
    def __eq__(self, edge):
        return (self.fr == edge.fr) and (self.to == edge.to)
    def __hash__(self):
        return hash('{0}->{1}'.format(self.fr, self.to))
    
def getRt(graph):
    ret = set()
    s = 0
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達 
    color = [0 for _ in range(node_num)]
    q = deque([s])
    color[s] = 1
    while (len(q) > 0):
        u = q.popleft()
        ret.add(u)
        color[u] = 2
        for v in graph[u]:
            if color[v] == 0:
                q.append(v)
                color[v] = 1
    return ret

def make_graph(edge_set):
    max_nodes = 10001
    graph = [[] for _ in range(max_nodes)]
    for edge in edge_set:        
        graph[edge.fr].append(edge.to)
    return graph

def refresh_edge_set(node_set, edge_set):
    ret = set()
    for edge in edge_set:
        if (edge.fr in node_set) and (edge.to in node_set):
            ret.add(edge)
    return ret    
    
def solve3_1(file_path):
    max_nodes = 10001
    orders = format_input(file_path)        
    node_set = set([0])
    edge_set = set()
    graph = [[] for _ in range(max_nodes)]
    for index, order in enumerate(orders):
        t = index+1        
        if order.t == 0: # add
            x = order.x
            y = order.y
            if x in node_set: # 常に辿りつける設定なので 
                node_set.add(x)
                node_set.add(y)
                edge = Edge(x, y)
                edge_set.add(edge)                    
                graph[x].append(y)
        if order.t == 1: # del
            x = order.x
            y = order.y
            edge = Edge(x, y)
            if edge in edge_set:
                edge_set.remove(edge) # 対象のエッジを削除
                graph = make_graph(edge_set) # 新しいエッジセットからグラフを再構築
                node_set = getRt(graph) # Rtがnode_setとなる
                edge_set = refresh_edge_set(node_set, edge_set) # node_setとedge_setによってたどり着ける範囲内でエッジを再構築
                graph = make_graph(edge_set) # さらにグラフを更新
                
    print('3-1: 頂点数= {0}, 有向辺数= {1}'.format(len(node_set), len(edge_set)))


# -

solve3_1('test002.txt')


