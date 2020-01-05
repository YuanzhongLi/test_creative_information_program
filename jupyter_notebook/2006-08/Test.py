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
from CharacterCode import *

def isSmall(num):
    return num >= 97 and num <= 122

def isBig(num):
    return num >= 65 and num <= 90

def decodeChar1(ch, key):
    if ch.isalpha():
        int_num = AsciiStr2Int(ch)
        if isSmall(int_num):
            order = int_num - 97
            return Hexbytes2Str(Int2hexbytes((order - key) % 26 + 97))
        if isBig(int_num):
            order = int_num - 65
            return Hexbytes2Str(Int2hexbytes((order - key) % 26 + 65))
    return ch
       
def decodeText1(text, key):
    ret = ''
    for ch in text:
        ret += decodeChar1(ch, key)
    return ret

def solve1(file_path):
    with open(file_path, 'r', encoding='ascii') as f:
        tmp = f.readlines()
        txt_array = []
        for txt in tmp:
            if txt[-1] == '\n':
                txt_array.append(txt[:-1])
            else:
                txt_array.append(txt)
        for key in range(1, 26):
            print('key: ' + str(key))
            for txt in txt_array:
                print(decodeText1(txt, key))
            print('---end---\n')
        


# +
# solve1('test001.txt')

# +
# (2)
from CharacterCode import *

def isSmall(num):
    return num >= 97 and num <= 122

def isBig(num):
    return num >= 65 and num <= 90

def decodeChar1(ch, key):
    if ch.isalpha():
        int_num = AsciiStr2Int(ch)
        if isSmall(int_num):
            order = int_num - 97
            return Hexbytes2Str(Int2hexbytes((order - key) % 26 + 97))
        if isBig(int_num):
            order = int_num - 65
            return Hexbytes2Str(Int2hexbytes((order - key) % 26 + 65))
    return ch
       
def decodeText1(text, key):
    ret = ''
    for ch in text:
        ret += decodeChar1(ch, key)
    return ret

class Tmp(object):
    def __init__(self, al, cnt):
        self.al = al
        self.cnt = cnt
    def __repr__(self):
        return '{0}: {1}'.format(self.al, self.cnt)
    def __lt__(self, tmp):
        return self.cnt < tmp.cnt    

def solve2_1(file_path):
    with open(file_path, 'r', encoding='ascii') as f:
        text = f.read().lower()
        freq = []
        for i in range(26):
            order = i + 97
            al = Hexbytes2Str(Int2hexbytes(order))
            cnt = 0
            tmp = Tmp(al, cnt)
            freq.append(tmp)
        for ch in text:
            if ch.isalpha():
                idx = AsciiStr2Int(ch) - 97
                freq[idx].cnt += 1
        freq.sort()
        freq = freq[::-1]
        for tmp in freq:
            print(tmp)


# +
# solve2_1('test001.txt')

# +
from CharacterCode import *

def isSmall(num):
    return num >= 97 and num <= 122

def isBig(num):
    return num >= 65 and num <= 90

def decodeChar1(ch, key):
    if ch.isalpha():
        int_num = AsciiStr2Int(ch)
        if isSmall(int_num):
            order = int_num - 97
            return Hexbytes2Str(Int2hexbytes((order - key) % 26 + 97))
        if isBig(int_num):
            order = int_num - 65
            return Hexbytes2Str(Int2hexbytes((order - key) % 26 + 65))
    return ch
       
def decodeText1(text, key):
    ret = ''
    for ch in text:
        ret += decodeChar1(ch, key)
    return ret

class Tmp(object):
    def __init__(self, al, cnt):
        self.al = al
        self.cnt = cnt
    def __repr__(self):
        return '{0}: {1}'.format(self.al, self.cnt)
    def __lt__(self, tmp):
        return self.cnt < tmp.cnt    

def solve2_2(file_path):
    with open(file_path, 'r', encoding='ascii') as f:
        text = f.read().lower()
        freq = []
        for i in range(26):
            order = i + 97
            al = Hexbytes2Str(Int2hexbytes(order))
            cnt = 0
            tmp = Tmp(al, cnt)
            freq.append(tmp)
        for ch in text:
            if ch.isalpha():
                idx = AsciiStr2Int(ch) - 97
                freq[idx].cnt += 1
        freq.sort()
        freq = freq[::-1]
        for tmp in freq:
            print(tmp)


# +
from CharacterCode import *
from PriorityQueue import PriorityQueue

def isSmall(num):
    return num >= 97 and num <= 122

def isBig(num):
    return num >= 65 and num <= 90

freq = []

class Node(object):
    # 文字の場合node_idはasciiコード
    def __init__(self, al, cnt, node_id):
        self.al = al
        self.cnt = cnt
        self.node_id = node_id
        # parent, left, rightのnode_id 
        self.p = None
        self.r = None
        self.l = None
    def __repr__(self):                           
        return '{0}: {1}, ID: {2}\n'.format(self.al, self.cnt, self.node_id) + \
               '親ノード: {0}\n'.format(self.p) + \
               '左ノード: {0}, 右ノード: {1}'.format(self.l, self.r)
    def __lt__(self, node):
        if self.cnt == node.cnt:
            return self.node_id < node.node_id
        else:
            return self.cnt < node.cnt 

def encode3(ch):
    ret = ''
    global freq
    node = freq[AsciiStr2Int(ch)]
    while True:
        if node.p == None:
            break
        p = freq[node.p]
        if p.l == node.node_id:
            ret += '0'
        elif p.r == node.node_id:
            ret += '1'
        node = p
    return ret[::-1]        
        
def solve3_1(file_path):
    with open(file_path, 'r', encoding='ascii') as f:
        text = f.read().lower()
        global freq
        freq = [None for _ in range(127)]
        for i in range(127):
            if i == 10:
                node = Node('LF', 0, i)
                freq[i] = node
            elif i == 13:
                node = Node('CR', 0, i)
                freq[i] = node
            elif i == 32:
                node = Node('SP', 0, i)
            elif i >= 33 and i <= 126:
                al = Hexbytes2Str(Int2hexbytes(i))
                cnt = 0
                node = Node(al, cnt, i)            
                freq[i] = node
        for ch in text:
            if ch.isalpha():
                idx = AsciiStr2Int(ch)
                freq[idx].cnt += 1
        pq = PriorityQueue([])
        for node in freq:
            if node != None:
                pq.push(node)
        while len(pq) > 1:
            new_node_id = len(freq)
            r_node = pq.pop()
            l_node = pq.pop()
            new_node = Node('{0},{1}'.format(r_node.al, l_node.al), r_node.cnt + l_node.cnt, new_node_id)
            r_node.p = new_node_id
            l_node.p = new_node_id
            new_node.r = r_node.node_id
            new_node.l = l_node.node_id
            freq.append(new_node)
            pq.push(new_node)
        for i in range(127):
            node = freq[i]
            if node != None:
                code = None
                if node.al == 'LF':
                    code = encode3('\n')
                elif node.al == 'CR':
                    code = encode3('\r')
                elif node.al == 'SP':
                    code = encode3(' ')
                else:
                    code = encode3(node.al)
                print('{0}: {1}'.format(node.al, code))


# -

solve3_1('test001.txt')


# +
def test_make_graph():
    a = Node('A', 50, 65)
    b = Node('B', 20, 66)
    c = Node('C', 33, 67)
    d = Node('D', 15, 68)
    e = Node('E', 40, 69)
    global freq
    freq = [None for _ in range(127)]
    freq[65] = a
    freq[66] = b
    freq[67] = c
    freq[68] = d
    freq[69] = e       
    pq = PriorityQueue([])
    pq.push(a)
    pq.push(b)
    pq.push(c)
    pq.push(d)
    pq.push(e)
    new_node_id = 127
    while len(pq) > 1:
        new_node_id = len(freq)
        r_node = pq.pop()
        l_node = pq.pop()
        new_node = Node('{0},{1}'.format(r_node.al, l_node.al), r_node.cnt + l_node.cnt, new_node_id)
        r_node.p = new_node_id
        l_node.p = new_node_id
        new_node.r = r_node.node_id
        new_node.l = l_node.node_id
        freq.append(new_node)
        pq.push(new_node)          
    print(freq)
    
def encode3(ch):
    ret = ''
    node = freq[AsciiStr2Int(ch)]
    while True:
        if node.p == None:
            break
        p = freq[node.p]
        if p.l == node.node_id:
            ret += '0'
        elif p.r == node.node_id:
            ret += '1'
        node = p
    return ret[::-1]


# -

test_make_graph()

# +
from CharacterCode import *
from PriorityQueue import PriorityQueue

def isSmall(num):
    return num >= 97 and num <= 122

def isBig(num):
    return num >= 65 and num <= 90

freq = []

class Node(object):
    # 文字の場合node_idはasciiコード
    def __init__(self, al, cnt, node_id):
        self.al = al
        self.cnt = cnt
        self.node_id = node_id
        # parent, left, rightのnode_id 
        self.p = None
        self.r = None
        self.l = None
    def __repr__(self):                           
        return '{0}: {1}, ID: {2}\n'.format(self.al, self.cnt, self.node_id) + \
               '親ノード: {0}\n'.format(self.p) + \
               '左ノード: {0}, 右ノード: {1}'.format(self.l, self.r)
    def __lt__(self, node):
        if self.cnt == node.cnt:
            return self.node_id < node.node_id
        else:
            return self.cnt < node.cnt 

def encode3(ch):
    ret = ''
    global freq
    node = freq[AsciiStr2Int(ch)]
    while True:
        if node.p == None:
            break
        p = freq[node.p]
        if p.l == node.node_id:
            ret += '0'
        elif p.r == node.node_id:
            ret += '1'
        node = p
    return ret[::-1]        
        
def solve3_2(file_path):
    with open(file_path, 'r', encoding='ascii') as f:
        text = f.read().lower()
        global freq
        freq = [None for _ in range(127)]
        for i in range(127):
            if i == 10:
                node = Node('LF', 0, i)
                freq[i] = node
            elif i == 13:
                node = Node('CR', 0, i)
                freq[i] = node
            elif i == 32:
                node = Node('SP', 0, i)
            elif i >= 33 and i <= 126:
                al = Hexbytes2Str(Int2hexbytes(i))
                cnt = 0
                node = Node(al, cnt, i)            
                freq[i] = node
        for ch in text:
            if ch.isalpha():
                idx = AsciiStr2Int(ch)
                freq[idx].cnt += 1
        pq = PriorityQueue([])
        for node in freq:
            if node != None:
                pq.push(node)
        while len(pq) > 1:
            new_node_id = len(freq)
            r_node = pq.pop()
            l_node = pq.pop()
            new_node = Node('{0},{1}'.format(r_node.al, l_node.al), r_node.cnt + l_node.cnt, new_node_id)
            r_node.p = new_node_id
            l_node.p = new_node_id
            new_node.r = r_node.node_id
            new_node.l = l_node.node_id
            freq.append(new_node)
            pq.push(new_node)
        dic = {}    
        for i in range(127):
            node = freq[i]
            if node != None:
                code = None
                if node.al == 'LF':
                    code = encode3('\n')
                elif node.al == 'CR':
                    code = encode3('\r')
                elif node.al == 'SP':
                    code = encode3(' ')
                else:
                    code = encode3(node.al)
                dic[node.al] = len(code)
        total = 0
        mom = 0
        for i in range(127):
            node = freq[i]
            if node != None:
                cnt = node.cnt
                size = dic[node.al]
                total += (cnt * size)
                mom += cnt
        print('{0:.2f}'.format(total / mom))


# -

solve3_2('test001.txt')


