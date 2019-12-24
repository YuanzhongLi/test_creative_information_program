import sys

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
    # 最も一致しているもので 14/20 以上一致していたらその数であると判定する
    if score > 13:
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

solve5('out5.txt')
