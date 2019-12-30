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


# (1) 
def solve1(file_path):
    cnt = 0
    with open(file_path, 'r') as f:
        txt = f.read()
        if txt[-1] == '\n' and len(txt) > 1:
                txt = txt[:-1]
        for ch in txt:
            if ch == ';':
                cnt += 1
    return cnt


solve1('test001.txt')


# (2):
def solve2(file_path):
    with open(file_path, 'r') as f:
        txts = f.readlines()
    ret = []
    for index, txt in enumerate(txts):
        if 'main' in txt:
            print('{0}行目: {1}'.format(index+1, txt))


solve2('test001.txt')


# (3)
def solve3(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
        txts = []
        for index, txt in enumerate(text):
            if txt[-1] == '\n':
                txts.append(txt[:-1])
            else:
                txts.append(txt)
        s = set()
        for index, txt in enumerate(txts):
            if index < len(txts) - 1:
                next_txt = txts[index + 1]
                if txt == next_txt:
                    s.add(txt)                
    for txt in s:
        print(txt)


solve3('test002.txt')


# +
# (4)
class Line(object):
    def __init__(self, txt, initial_appear, appear_times):
        self.txt = txt
        self.initial_appear = initial_appear
        self.appear_times = appear_times
    
    def __lt__(self, line):
        self.initial_appear < line.initial_appear
        
    def __repr__(self):
        return '初登場行: {0}, 登場回数: {1}, txt: {2}'.format(self.initial_appear, self.appear_times, self.txt)

def solve4(file_path):
    with open(file_path, 'r') as f:        
        text = f.readlines()
        txts = []
        for index, txt in enumerate(text):
            if txt[-1] == '\n':
                txts.append(txt[:-1])
            else:
                txts.append(txt)
                
        dic = {} # 'txt': [初登場行, 登場回数]
        for index, txt in enumerate(txts):
            if txt in dic.keys():
                dic[txt][1] += 1
            else:
                dic[txt] = [index+1, 1]
    ret = []
    for key in dic.keys():
        obj = dic[key]
        initial_appear = obj[0]
        appear_times = obj[1]
        if appear_times > 1:
            ret.append(Line(key, initial_appear, appear_times))
    
    sorted(ret)
    for line in ret:
        print(line)
        


# -

solve4('test002.txt')


# +
# (5)
def formatnptxt(nparray):
    txt = ''
    for ch in nparray:
        txt += ch
    return txt    

def solve5(file_path, minimum_len):
     with open(file_path, 'r') as f:        
        text = f.readlines()
        txts = []
        max_len = 0
        for index, txt in enumerate(text):
            if txt[-1] == '\n':
                if len(txt[:-1]) >= minimum_len:
                    txts.append(txt[:-1])
                    max_len = max(max_len, len(txt[:-1]))
            else:
                if len(txt) >= minimum_len:
                    txts.append(txt)
                    max_len = max(max_len, len(txt))                    

        formatted_txts = np.array([[' ' for _ in range(max_len)] for _ in range(len(txts))])
        for i, txt in enumerate(txts):
            for j, ch in enumerate(txt):
                formatted_txts[i, j] = ch
        ret = set()
        sames = 0
        for i in range(0, len(formatted_txts) - 1):
            txt1 = formatted_txts[i]
            for j in range(i+1, len(formatted_txts)):
                txt2 = formatted_txts[j]
                booleans = (txt1 == txt2)
                same_scores = booleans.sum()
                if same_scores < max_len and (max_len - same_scores) < 5:
                    sames += 1
                    pair1 = '{0}\n{1}'.format(formatnptxt(txt1), formatnptxt(txt2))
                    pair2 = '{0}\n{1}'.format(formatnptxt(txt2), formatnptxt(txt1))                    
                    if (not (pair1 in ret)) and (not (pair2 in ret)):
                        ret.add(pair1)
                    
        for set_ele in ret:
            set_ele_array = set_ele.split('\n')
            print('{0}, {1}'.format(set_ele_array[0], set_ele_array[1]))
        print(sames)


# -

solve5('test002.txt', 2)

# +
# (6)
from LCS import LCS

def solve6(file_path, minimu_len):
    with open(file_path, 'r') as f:
        text = f.readlines()
        txts = []
        for index, txt in enumerate(text):
            if txt[-1] == '\n':
                if len(txt[:-1]) >= minimu_len:
                    txts.append(txt[:-1])
            else:
                if len(txt) >= minimu_len:
                    txts.append(txt)

        s = set()
        sames = 0
        for i in range(len(txts) - 1):
            txt1 = txts[i]
            txt1_len = len(txt1)
            for j in range(i + 1, len(txts)):
                txt2 = txts[j]
                txt2_len = len(txt2)
                if txt1 != txt2:
                    lcs = LCS(txt1, txt2)
                    lcs_len = len(lcs)
                    diff = abs(txt1_len - txt2_len) + min(txt1_len - lcs_len, txt2_len - lcs_len)
#                     print(txt1)
#                     print(txt2)
#                     print(lcs)
#                     print(txt1_len, txt2_len, lcs_len, diff)
#                     print('---------')
                    if diff < 4:
                        sames += 1
                        pair1 = '{0}\n{1}'.format(txt1, txt2)
                        pair2 = '{0}\n{1}'.format(txt2, txt1)
                        if (not (pair1 in s)) and (not (pair2 in s)):
                            s.add(pair1)
        for set_ele in s:
            set_ele_array = set_ele.split('\n')
            print('{0}, {1}'.format(set_ele_array[0], set_ele_array[1]))
        print(sames)


# -

solve6('test002.txt', 2)


# (7)
def solve7(file_path):
