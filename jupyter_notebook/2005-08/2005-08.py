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
import numpy as np
class Field(object):
    def __init__(self, idx:int, groups):
        self.idx = idx
        # ex [[1,2,4,5], [3, 6], [7]]
        self.groups = groups
    def __repr__(self):
        return '(idx: {0}, groups: {1})'.format(self.idx, self.groups)

class Point(object):
    def __init__(self, idx:int, life: int):
        self.idx = int(idx)
        self.life = int(life)
        # 隣接の点のidxを格納していく,最大3つ
        self.dists = []
        # 面している領域のidxを格納していく、最大3つ
        self.fields = []
    def __repr__(self):
        return '( idx: {0}, life: {1}, dists: {2}, fields: {3} )'.format(self.idx, self.life, self.dists, self.fields)


class Phase(object):
    def __init__(self, points, fields, player, hand):
        # 初期局面 { 'player': 0, 'hand': 0 }
        self.phase = { 'player': player, 'hand': hand }
        self.points = points
        self.fields = fields
    def add_point(self, point):
        self.points.append(point)
    def add_field(self, field):
        self.fields.append(field)
    
    def __repr__(self):
        ret = ''
        if (self.phase['player'] == 0):
            ret += '初期局面\n'
        elif (self.phase['player'] == 1):
            ret += '先手第{0}手\n'.format(self.phase['hand'])
        elif (self.phase['player'] == 2):
            ret += '後手第{0}手\n'.format(self.phase['hand'])
        ret += 'poins:\n{0}'.format(self.points[1:])
        ret += 'fields:\n{0}'.format(self.fields[1:])
        return ret
    
    # playerが1のとき先手,  2のとき後手
    def play_game(self, player):
        if (player == 1):
            self.phase['player'] = 1
            self.phase['hand'] += 1
        elif (player ==  2):
            self.phase['player'] = 2
            
    def go_back(self):
        
    def phase_back(self):
        if (self.phase['player'] == 1 and self.phase['hand'] == 1):
            self.phase['player'] = 0
            self.phase['hand'] = 0
        elif (self.phase['player'] == 1):
            self.phase['hand'] -= 1
            self.phase['player'] = 2
        elif (self.phase['player'] == 2):
            self.phase['player'] = 1
            
    def point_back(self):
        last_p = self.points.pop()
        
        # 他の点からlast_pを隣接点から削除
        for dist_pidx in last_p['dists']:
            for index, pidx in enumerate(self.points[dist_pidx]['dists']):
                if (pidx == last_p['idx']):
                    self.points[dist_pidx]['dists'].pop(index)
                    break
                    
        # pの追加で領域を作った(pが二つの領域に接する)
        if (len(last_p['fields']) == 2):
            f = self.fields.pop()
            
            # fに面するpoint全てから
            for 
            
            for group in f['groups']:
                # groupにlast_pがある場合
                if (last_p['idx'] in group): # このgroup内の点に接するfieldはpopしたfieldを除外するだけでいい
                    for pidx in group:
                        if (pidx != p['idx']):
                            for index, fidx enumerate(self.points[pidx]['fields']):
                                if (fidx == f['idx']):
                                    self.points[pidx]['fields'].pop(index)
                else:
                    
            

                


# +
# (3) a
n = 3
# points[0] は使わない
p0 = Point(0, 0)

p1 = Point(1, 0)
p1.dists.extend([4, 5])
p1.fields.extend([1, 2])

p2 = Point(2, 2)
p2.dists.extend([4])
p2.fields.extend([1])

p3 = Point(3, 3)
p3.fields.extend([2])

p4 = Point(4, 1)
p4.dists.extend([1, 2])
p4.fields.extend([1])

p5 = Point(5, 1)
p5.dists.extend([1])
p5.fields.extend([1, 2])

points = [p0, p1, p2, p3, p4, p5]

points[1:]

# +
f0 = Field(0, [])

f1 = Field(1, [[1, 2, 4, 5]])
f2 = Field(2, [[1, 5], [3]])

fields = [f0, f1, f2]

fields
# -

# (3) b
phase = Phase(points, fields, 2, 1)
phase

# +
# (4)初期の点の数さえ分かればいい(途中の領域とかどうなっているかは聞かれていない)
# -


b

a


