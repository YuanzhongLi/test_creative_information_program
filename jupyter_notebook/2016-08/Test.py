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
pic = {
    '0': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '1': [['*'],
          ['|'],
          ['*'],
          ['|'],
          ['*']],
    '2': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*']],
    '3': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '4': [['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '5': [['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '6': [['*', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '7': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '8': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '9': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
}

def solve1(txt_num):
    nums_array = []
    for i in txt_num:
        nums_array.append(pic[i])
    nums = len(nums_array)
    row_num = 5
    with open('out1.txt', 'w') as f:
        for row in range(row_num):
            row_txt = ''
            for num_array in nums_array:
                for mark in num_array[row]:
                    row_txt += mark
                row_txt += '  '
            f.writelines(row_txt[:-2] + '\n')
            print(row_txt[:-2])
        


# -

solve1('813')

# +
# (2)
pic = {
    '0': [['*', '*', '*', '*'], ['|', ' ', ' ', '|'], ['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'], ['*', '*', '*', '*']],
    '1': [['*'], ['|'], ['*'], ['|'], ['*']],
    '2': [['*', '*', '*', '*'], [' ', ' ', ' ', '|'], ['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '], ['*', '*', '*', '*']],
    '3': [['*', '*', '*', '*'], [' ', ' ', ' ', '|'], ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'], ['*', '*', '*', '*']],
    '4': [['*', ' ', ' ', '*'], ['|', ' ', ' ', '|'], ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'], [' ', ' ', ' ', '*']],
    '5': [['*', '*', '*', '*'], ['|', ' ', ' ', ' '], ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'], ['*', '*', '*', '*']],
    '6': [['*', ' ', ' ', ' '], ['|', ' ', ' ', ' '], ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'], ['*', '*', '*', '*']],
    '7': [['*', '*', '*', '*'], [' ', ' ', ' ', '|'], [' ', ' ', ' ', '*'],
          [' ', ' ', ' ', '|'], [' ', ' ', ' ', '*']],
    '8': [['*', '*', '*', '*'], ['|', ' ', ' ', '|'], ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'], ['*', '*', '*', '*']],
    '9': [['*', '*', '*', '*'], ['|', ' ', ' ', '|'], ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'], [' ', ' ', ' ', '*']],
}


def toNumber(num_array):
    for key in pic.keys():
        if num_array == pic[key]:
            return key
    return '-'


def solve2(file_path):
    with open(file_path, 'r') as f:
        txt_rows = []
        col = 0
        row = 5
        for i in range(5):
            line = f.readline()
            line = line[:-1]
            col = max(col, len(line))
            txt_rows.append(line)
        # 番兵として右側に空白を10列追加
        canvas = [[' ' for _ in range(col + 10)] for _ in range(row)]
        for i, line in enumerate(txt_rows):
            for j, mark in enumerate(line):
                canvas[i][j] = mark
        x = 0
        ret = ''
        while (x < col):
            num_array_not_one = [[' ' for _ in range(4)] for _ in range(5)]
            for i in range(4):
                for j in range(5):
                    num_array_not_one[j][i] = canvas[j][x + i]
            key = toNumber(num_array_not_one)
            if key != '-':
                ret += key
                x += 6
                continue

            num_array_one = [[' ' for _ in range(1)] for _ in range(5)]
            for i in range(1):
                for j in range(5):
                    num_array_one[j][i] = canvas[j][x + i]
            key = toNumber(num_array_one)
            if key != '-':
                ret += key
                x += 3
                continue
        print(ret)


# -

solve2('out1.txt')

# +
# (3)
pic = {
    '0': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '1': [['*'],
          ['|'],
          ['*'],
          ['|'],
          ['*']],
    '2': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*']],
    '3': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '4': [['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '5': [['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '6': [['*', ' ', ' ', ' '],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '7': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '8': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '9': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
}

class Numobj(object):
    def __init__(self, txt_num, x, y):
        self.txt_num = txt_num
        self.x = x
        self.y = y
    
    def __repr__(self):
        return '{0}, ({1}, {2})'.format(self.txt_num, self.x, self.y)
        
def solve3(txt):
    input_list = txt.split(',')
    input_txt_num = input_list[0]
    nums = len(input_txt_num)
    numobjs = []
    x_cnt = 0
    for i in range(nums):
        txt_num = input_txt_num[i]
        num = int(txt_num)            
        y = int(input_list[1 + i * 2])
        x = x_cnt
        numobjs.append(Numobj(txt_num, x, y))
        if i < nums - 1:                
            x_cnt += int(input_list[2 + i * 2])
            if num == 1:
                x_cnt += 1
            else:
                x_cnt += 4
    col = numobjs[-1].x
    if numobjs[-1].txt_num == '1':
        col += 1
    else:
        col += 4
    row = 5
    tmp_max = 0
    for numobj in numobjs:
        tmp_max = max(numobj.y, tmp_max)
    row += tmp_max
    
    canvas = [[' ' for _ in range(col)] for _ in range(row) ]

    for numobj in numobjs:
        if numobj.txt_num == '1':
            for i in range(1):
                for j in range(5):
                    canvas[j + numobj.y][i + numobj.x] = pic[numobj.txt_num][j][i]
        else:
            for i in range(4):
                for j in range(5):
                    canvas[j + numobj.y][i + numobj.x] = pic[numobj.txt_num][j][i]
    with open('out3.txt', 'w')as f:        
        for row in canvas:
            row_txt = ''
            for mark in row:
                row_txt += mark
            f.writelines(row_txt + '\n')    
            print(row_txt)    


# -

solve3('813,0,4,1,3,2')

# +
# (4)
pic = {
    '0': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '1': [['*'],
          ['|'],
          ['*'],
          ['|'],
          ['*']],
    '2': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*']],
    '3': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '4': [['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '5': [['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '6': [['*', ' ', ' ', ' '],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '7': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '8': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '9': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
}

def toNumber(num_array):
    for key in pic.keys():
        if num_array == pic[key]:
            return key
    return '-'

def solve4(file_path):
    with open(file_path, 'r') as f:
        txt_rows = []
        col = 0
        row = 0
        while True:
            line = f.readline()
            if line == '':
                break
            else:
                line = line[:-1]
                row += 1
                col = max(col, len(line))
                txt_rows.append(line)
        # 番兵として右側に空白を10列追加        
        canvas = [[' ' for _ in range(col + 10)] for _ in range(row)]
        for i, line in enumerate(txt_rows):
            for j, mark in enumerate(line):
                canvas[i][j] = mark 

        x = 0        
        ret = ''
        while (x < col):
            for y in range(row - 4):
                num_array_not_one = [[' ' for _ in range(4)] for _ in range(5)]
                for i in range(5):
                    for j in range(4):
                        num_array_not_one[i][j] = canvas[y + i][x + j]                       
                
                key = toNumber(num_array_not_one)        
                if key != '-':
                    ret += key
                    x += 4
                    break
                    
                num_array_one = [[' ' for _ in range(1)] for _ in range(5)]
                for i in range(5):
                    for j in range(1):
                        num_array_one[i][j] = canvas[y + i][x + j]
                        
                key = toNumber(num_array_one)    
                if key != '-':
                    ret += key
                    x += 2
                    break
                
            x += 1
        print(ret)
        


# -

solve4('out3.txt')

# +
# (5)

pic = {
    '0': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '1': [['*'],
          ['|'],
          ['*'],
          ['|'],
          ['*']],
    '2': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*']],
    '3': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '4': [['*', ' ', ' ', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '5': [['*', '*', '*', '*'],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '6': [['*', ' ', ' ', ' '],
          ['|', ' ', ' ', ' '],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '7': [['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
    '8': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*']],
    '9': [['*', '*', '*', '*'],
          ['|', ' ', ' ', '|'],
          ['*', '*', '*', '*'],
          [' ', ' ', ' ', '|'],
          [' ', ' ', ' ', '*']],
}

def toNumberNotOne(num_array):    
    # 一致度
    score = 0
    ret = '-'
    for key in pic.keys():
        tmpscore = 0
        if key == '1':
            continue
        pic_array = pic[key]
        for i in range(4):
            for j in range(5):
                if pic_array[j][i] == num_array[j][i]:
                    tmpscore += 1
        if tmpscore > score:
            score = tmpscore
            ret = key
    # 最も一致しているもので 15/20 以上一致していたらその数であると判定する
    if score > 14:
        print(score, ret)
        return ret
    else:
        return '-'

def toNumberOne(num_array):
    score = 0
    ret = '-'
    one_array = pic['1']
    for i in range(1):
        for j in range(5):
            if one_array[j][i] == num_array[j][i]:
                score += 1
    if score > 2:
        return '1'
    else:
        return '-'

def solve5(file_path):
    with open(file_path, 'r') as f:
        txt_rows = []
        col = 0
        row = 0
        while True:
            line = f.readline()
            if line == '':
                break
            else:
                line = line[:-1]
                row += 1
                col = max(col, len(line))
                txt_rows.append(line)
        # 番兵として右側に空白を10列追加        
        canvas = [[' ' for _ in range(col + 10)] for _ in range(row)]
        for i, line in enumerate(txt_rows):
            for j, mark in enumerate(line):
                canvas[i][j] = mark                
        x = 0        
        ret = ''
        while (x < col):
            for y in range(row - 4):
                num_array_not_one = [[' ' for _ in range(4)] for _ in range(5)]
                for i in range(4):
                    for j in range(5):
                        num_array_not_one[j][i] = canvas[y + j][x + i]
                key = toNumberNotOne(num_array_not_one)
                if key != '-':
                    ret += key
                    x += 4
                    break
                    
                num_array_one = [[' ' for _ in range(1)] for _ in range(5)]
                for i in range(1):
                    for j in range(5):
                        num_array_one[j][i] = canvas[y + j][x + i]
                key = toNumberOne(num_array_one)    
                if key != '-':
                    ret += key
                    x += 2
                    break
                
            x += 1
        print(ret)



# -

solve5('out1.txt')


