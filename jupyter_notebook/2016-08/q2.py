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

solve2('out1.txt')
