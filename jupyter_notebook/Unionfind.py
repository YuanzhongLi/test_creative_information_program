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

class Unionfind:
    def __init__(self, N):
        self.par = [i for i in range(N)] # 節点
        self.rank = [0 for _ in range(N)] # 木の高さ
        self.size = [1 for _ in range(N)] # 節点が属する木の節点数
        self.treeNum = N # 木の数
    def addNode(self, x): # 節点(木)追加
        self.par[x] = x
        self.rank[x] = 0
        self.size[x] = 1
        self.treeNum += 1
    def root(self, x): # 根を探すと同時に経路上にある節点の親が根になるように代入
        if self.par[x] == x:
            return x
        else:
            self.par[x] = Unionfind.root(self, self.par[x])
            return self.par[x]
    def same(self, x, y):
        return Unionfind.root(x) == Unionfind.root(y)
    def unite(self, x, y):
        x = Unionfind.root(self, x)
        y = Unionfind.root(self, y)
        if x == y:
            return
        self.treeNum -= 1        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
