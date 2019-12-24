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

solve4('out3.txt')
