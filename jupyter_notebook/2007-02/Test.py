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


# #### (1), (2)
# - ヒントより区切りがない場合全マスを使った一本道となることがわかる
# - このときパネルはこの一本道に沿うので一本道と同じ数立てる
# (n-1)**2       

# #### (3)
# ##### 3-1
# 4 
# (0,1)-  (1,1)-  (2,1)-
# (1,1)|  (2,1)|
# (1,2)-  (3,2)-
# (3,2)|
# (1,3)-  (2,3)-
#
# ##### 3-2
# 4 
# (2,0)|
# (2,1)-
# (1,1)|  (2,1)|  (3,1)|
# (1,2)-
# (1,2)|  (3,2)|
# (0,3)-  (1,3)-  (2,3)-  (3,3)-
# (3,3)|

# +
class Panel(object):
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    def __repr__(self):
        return '({0},{1}): {2}'.format(self.x, self.y, self.s)

def format_txt(text):
    text = text.strip()
    txt_split_by_space = text.split()
    ret = []
    for txt_panel in txt_split_by_space:
        x = int(txt_panel[1])
        y = int(txt_panel[3])
        s = txt_panel[5]
        ret.append(Panel(x, y, s))
    return ret


# +
def solve4(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline())
        row = 2 * n + 1
        maze =[[' ' for _ in range(row)] for _ in range(row)]
        # init maze 
        # 格子点
        for i in range(len(maze)):
            for j in range(len(maze)):
                if ((i % 2 == 0) and (j % 2 == 0)):  
                    maze[i][j] = '+'           
    
        # 外枠            
        for i in range(len(maze)):
            if (i % 2 == 1 and i > 0):
                maze[0][i] = '-'
                maze[len(maze)-1][i] = '-' 
                maze[i][0] = '|'
                maze[i][len(maze)-1] = '|'                                                      
                    
        data = f.readlines()
        panels = []
        for text in data:
            tmp = format_txt(text)
            panels.extend(tmp)
        for panel in panels:
            x = panel.x
            y = panel.y
            s = panel.s
            if s == '-':
                maze[y * 2][x * 2 + 1] = s   
            if s == '|':
                maze[y * 2 + 1][x * 2] = s
        for maze_row in maze:
            row_txt = ''
            for mark in maze_row:
                row_txt += mark
        return maze
    
def printmaze(maze):
    for maze_row in maze:
      txt = ''
      for maze_mark in maze_row:
        txt += maze_mark
      print(txt)


# -

printmaze(solve4('test001.txt'))

# +
# (5)
from collections import deque

def init_maze2graph(maze):
    n = int((len(maze) - 1)/2)
    node_num = n**2
    graph = [[] for _ in range(node_num)]
    for i in range(n):
        for j in range(n):
            node_id = i * n + j 
            y = i * 2 + 1
            x = j * 2 + 1
            if maze[y][x-1] == ' ': # left
                graph[node_id].append(node_id-1)
            if maze[y-1][x] == ' ': # up
                graph[node_id].append(node_id-n)
            if maze[y][x+1] == ' ': # right
                graph[node_id].append(node_id+1)
            if maze[y+1][x] == ' ': # down
                graph[node_id].append(node_id+n)
    return graph            

def bfs(graph):
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達 
    color = [0 for _ in range(node_num)]
    ret = []
    for start in range(node_num):
        if (color[start] == 2):
            continue
        q = deque([start])
        color[start] = 1
        area = 0
        while (len(q) > 0):
            u = q.popleft()
            color[u] = 2
            area += 1
            for v in graph[u]:
                if color[v] == 0:
                    q.append(v)
                    color[v] = 1
        ret.append(area)
    return ret                    

def solve5(file_path):
    maze = solve4(file_path)
    graph = init_maze2graph(maze)
    areas = bfs(graph)
    return sorted(areas)[::-1]


# -

solve5('test002.txt')

# +
# (6)
from collections import deque
from math import sqrt
def init_maze2graph(maze):
    n = int((len(maze) - 1) / 2)
    node_num = n**2
    graph = [[] for _ in range(node_num)]
    for i in range(n):
        for j in range(n):
            node_id = i * n + j
            y = i * 2 + 1
            x = j * 2 + 1
            if maze[y][x - 1] == ' ':  # left
                graph[node_id].append(node_id - 1)
            if maze[y - 1][x] == ' ':  # up
                graph[node_id].append(node_id - n)
            if maze[y][x + 1] == ' ':  # right
                graph[node_id].append(node_id + 1)
            if maze[y + 1][x] == ' ':  # down
                graph[node_id].append(node_id + n)
    return graph


def dijkstra(graph):
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達
    color = [0 for _ in range(node_num)]
    inf = int(1e9 + 7)
    dist = [inf for _ in range(node_num)]
    parent = [-1 for _ in range(node_num)]
    s = 0
    q = deque([s])
    color[s] = 1
    dist[s] = 0
    while (len(q) > 0):
        u = q.popleft()
        color[u] = 2
        for v in graph[u]:
            if color[v] == 2:
                continue
            if dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
                color[v] = 1

    return dist, parent

def node_id2cord(node_id, n):
    x = node_id % n
    y = int(node_id / n)
    return x, y

def solve6(file_path):
    maze = solve4(file_path)
    graph = init_maze2graph(maze)
    dist, parent = dijkstra(graph)
    node_num = len(graph)
    n = int((len(maze) - 1) / 2)
    if (dist[node_num - 1] > node_num):
        return "cant achieve"
    e = node_num - 1
    root = [e]
    while (e != 0):
        p = parent[e]
        root.append(p)
        e = p
    root = root[::-1]
    ret = '(0, 0)'
    for i in range(1, len(root)):
        node_id = root[i]
        x, y = node_id2cord(node_id, n)
        ret += ' ({0}, {1})'.format(x, y)
    return ret


# -

solve6('test001.txt')


# (7)
class Node(object):
    def __init__(self, Id, x, y, isDoor):
        self.Id = Id
        self.x = x
        self.y = y
        self.isDoor = isDoor
        
    def __repr__(self):
        return 'id: {0}, ({1}, {2}), isDoor: {3}'.format(self.Id, self.x, self.y, self.isDoor)
    


# +
class Door(object):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
    def __repr__(self):
        return '({0}, {1})'.format(self.node1, self.node2)

def cord2node_id(x, y, n):
    return x + y * n
    
def format_txt2(text, n):
    text = text.strip()
    txt_split_by_space = text.split()
    panels = []
    doors = []
    for txt_panel in txt_split_by_space:
        if ('*' in txt_panel):
            x1 = int(txt_panel[1])
            y1 = int(txt_panel[3])
            x2 = int(txt_panel[7])
            y2 = int(txt_panel[9])
            id1 = cord2node_id(x1, y1, n)
            id2 = cord2node_id(x2, y2, n)
            node1 = Node(id1, x1, y1, True)
            node2 = Node(id2, x2, y2, True)
            door = Door(node1, node2)
            doors.append(door)
        else:    
            x = int(txt_panel[1])
            y = int(txt_panel[3])
            s = txt_panel[5]
            panels.append(Panel(x, y, s))
    return panels, doors

def inputdata(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline())
        row = 2 * n + 1
        maze =[[' ' for _ in range(row)] for _ in range(row)]
        # init maze 
        # 格子点
        for i in range(len(maze)):
            for j in range(len(maze)):
                if ((i % 2 == 0) and (j % 2 == 0)):  
                    maze[i][j] = '+'           
    
        # 外枠            
        for i in range(len(maze)):
            if (i % 2 == 1 and i > 0):
                maze[0][i] = '-'
                maze[len(maze)-1][i] = '-' 
                maze[i][0] = '|'
                maze[i][len(maze)-1] = '|'                                                      
                    
        data = f.readlines()
        panels = []
        doors = []
        for text in data:
            tmp_panels, tmp_doors = format_txt2(text, n)
            panels.extend(tmp_panels)
            doors.extend(tmp_doors)
            
        for panel in panels:
            x = panel.x
            y = panel.y
            s = panel.s
            if s == '-':
                maze[y * 2][x * 2 + 1] = s   
            if s == '|':
                maze[y * 2 + 1][x * 2] = s
        for maze_row in maze:
            row_txt = ''
            for mark in maze_row:
                row_txt += mark
        return n, maze, doors    
    
def init_graph(n, maze, doors):
    node_num = n**2
    graph = [[] for _ in range(node_num)]
    for i in range(n):
        for j in range(n):
            node_id = i * n + j
            y = i * 2 + 1
            x = j * 2 + 1
            if maze[y][x - 1] == ' ':  # left
                node = Node(node_id - 1, j - 1, i, False)
                graph[node_id].append(node)
            if maze[y - 1][x] == ' ':  # up
                node = Node(node_id - n, j, i - 1, False)
                graph[node_id].append(node)
            if maze[y][x + 1] == ' ':  # right
                node = Node(node_id + 1, j + 1, i, False)
                graph[node_id].append(node)
            if maze[y + 1][x] == ' ':  # down
                node = Node(node_id + n, j, i + 1, False)
                graph[node_id].append(node)
    for door in doors:
        graph[door.node1.Id].append(door.node2)
        graph[door.node2.Id].append(door.node1)
    return graph

def dijkstra2(graph):
    node_num = len(graph)
    # 0: 未発見, 1: 発見, 2: 到達
    color = [0 for _ in range(node_num)]
    inf = int(1e9 + 7)
    dist = [inf for _ in range(node_num)]
    dfnode = Node(-1, -1, -1, False)
    parent = [dfnode for _ in range(node_num)]
    s = 0
    node_s = Node(0, 0, 0, False)
    q = deque([node_s])
    color[s] = 1
    dist[s] = 0
    while (len(q) > 0):
        node_u = q.popleft()
        color[node_u.Id] = 2
        for node_v in graph[node_u.Id]:
            if color[node_v.Id] == 2:
                continue
            if dist[node_v.Id] > dist[node_u.Id] + 1:
                dist[node_v.Id] = dist[node_u.Id] + 1
                parent[node_v.Id] = node_u
                q.append(node_v)
                color[node_v.Id] = 1

    return dist, parent

def solve7(file_path):
    n, maze, doors = inputdata(file_path)
    graph = init_graph(n, maze, doors)
    dist, parent = dijkstra2(graph)
    node_num = len(graph)
    if (dist[node_num - 1] > node_num):
        return "cant achieve"
    node_e = Node(node_num-1, n - 1, n - 1, False)
    root = [node_e]
    while (node_e.Id != 0):
        node_p = parent[node_e.Id]
        root.append(node_p)
        node_e = node_p
    root = root[::-1]
    doors_set = set()
    for door in doors:
        doors_set.add('({0},{1})*({2},{3})'.format(door.node1.x, door.node1.y, door.node2.x, door.node2.y))
        doors_set.add('({0},{1})*({2},{3})'.format(door.node2.x, door.node2.y, door.node1.x, door.node1.y))
    i = 0
    ret = ''
    while (i < len(root)):
        if i < len(root) - 1:
            node1 = root[i]
            node2 = root[i+1]
            txt_id1 = '({0},{1})*({2},{3})'.format(node1.x, node1.y, node2.x, node2.y)
            txt_id2 = '({0},{1})*({2},{3})'.format(node2.x, node2.y, node1.x, node1.y)           
            isDoor = ((txt_id1 in doors_set) or (txt_id2 in doors_set))
            if (isDoor):
                i += 2
                ret += '({0},{1})*({2},{3}) '.format(node1.x, node1.y, node2.x, node2.y)
            else:
                i += 1
                ret += '({0},{1}) '.format(node1.x, node1.y)
        else:
            node = root[i]
            ret += '({0},{1}) '.format(node.x, node.y)
            i += 1
            
    return ret[:-1]        


# -

solve7('test003.txt')
