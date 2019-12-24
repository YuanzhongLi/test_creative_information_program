import sys
inp = sys.argv[1]

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

solve3(inp)
