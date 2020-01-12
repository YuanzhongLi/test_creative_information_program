from collections import OrderedDict
import numpy as np
import copy as cp
import time

dic = {}
dic['1'] = 0
dic['2'] = 1
dic['3'] = 2
dic['A'] = 0
dic['B'] = 1
dic['C'] = 2

def is_same(text):
    ret = True
    s = text[0]
    for mark in text:
        if mark != s:
            ret = False
            break
    return ret

def is_same_as_mark(text, m):
    ret = True
    for mark in text:
        if mark != m:
            ret = False
            break
    return ret

def get_revmark(mark):
    if mark == 'O':
        return 'X'
    elif mark == 'X':
        return 'O'
    else:
        return '-'

# その並びがmarkが2個あってかつ最後の一つが空いてるとき
def has2(text, mark):
    tmp = 0
    revm = get_revmark(mark)
    for m in text:
        if m == revm:
            return False
        elif m == mark:
            tmp += 1
    return tmp >= 2

def diff2(text):
    return ('O' in text) and ('X' in text)

def who_win(game):
    dic = OrderedDict()
    dic['row1'] = game[0][0] + game[0][1] + game[0][2]
    dic['row2'] = game[1][0] + game[1][1] + game[1][2]
    dic['row3'] = game[2][0] + game[2][1] + game[2][2]
    dic['col1'] = game[0][0] + game[1][0] + game[2][0]
    dic['col2'] = game[0][1] + game[1][1] + game[2][1]
    dic['col3'] = game[0][2] + game[1][2] + game[2][2]
    dic['cross1'] = game[0][0] + game[1][1] + game[2][2]
    dic['cross2'] = game[0][2] + game[1][1] + game[2][0]
    for txt in dic.values():
        if is_same(txt):
            return txt[0]
    return '-'

def will(Game, mark, inp):
    revm = get_revmark(mark)
    i = dic[inp[0]]
    j = dic[inp[1]]
    game = cp.deepcopy(Game)
    game[i][j] = mark

    dic_L = OrderedDict()
    dic_L['row1'] = game[0][0] + game[0][1] + game[0][2]
    dic_L['row2'] = game[1][0] + game[1][1] + game[1][2]
    dic_L['row3'] = game[2][0] + game[2][1] + game[2][2]
    dic_L['col1'] = game[0][0] + game[1][0] + game[2][0]
    dic_L['col2'] = game[0][1] + game[1][1] + game[2][1]
    dic_L['col3'] = game[0][2] + game[1][2] + game[2][2]
    dic_L['cross1'] = game[0][0] + game[1][1] + game[2][2]
    dic_L['cross2'] = game[0][2] + game[1][1] + game[2][0]

    win_cnt = 0
    diff2_cnt = 0

    for line in dic_L.values():
        if is_same_as_mark(line, mark):
            return 'win'
        elif has2(line, revm):
            return 'lose'
        elif has2(line, mark):
            win_cnt += 1
        if diff2(line):
            diff2_cnt += 1
    if win_cnt >= 2:
        return 'win'
    elif diff2_cnt == 8:
        return 'drow'
    else:
        return 'unknown'

def choice(game, mark):
    space = []
    for i in range(3):
        for j in range(3):
            if game[i][j] == '-':
                space.append([i, j])
    space_inp = []
    for sp in space:
        tmp = ''
        i = sp[0]
        j = sp[1]
        tmp += str(i+1)
        if j == 0:
            tmp += 'A'
        elif j == 1:
            tmp += 'B'
        elif j == 2:
            tmp += 'C'
        space_inp.append(tmp)
    ret = space_inp[np.random.randint(len(space_inp))]
    status = 'lose'
    for inp in space_inp:
        result = will(game, mark, inp)
        if result == 'win':
            status = 'win'
            return inp
        elif result == 'unknown':
            status = 'unknown'
            ret = inp
        elif result == 'drow':
            if status == 'lose':
                ret = inp
                status = 'drow'
    return ret

def random_choice(game):
    space = []
    for i in range(3):
        for j in range(3):
            mark = game[i][j]
            if mark == '-':
                space.append([i, j])

    space_inp = []
    for sp in space:
        tmp = ''
        i = sp[0]
        j = sp[1]
        tmp += str(i+1)
        if j == 0:
            tmp += 'A'
        elif j == 1:
            tmp += 'B'
        elif j == 2:
            tmp += 'C'
        space_inp.append(tmp)
    return space_inp[np.random.randint(len(space_inp))]

class Board(object):
    def __init__(self, game):
        self.game = game
        self.O_num = 0
        self.X_num = 0
        for row in game:
            for mark in row:
                if mark == 'O':
                    self.O_num += 1
                elif mark == 'X':
                    self.X_num += 1
        if self.O_num == self.X_num:
            self.next_turn = 'O'
        else:
            self.next_turn = 'X'
        self.game_turn = self.O_num + self.X_num
        if self.game_turn >= 9:
            self.is_game_end = True
        else:
            self.is_game_end = False

    def __repr__(self):
        ret = ''
        for row in self.game:
            ret += (''.join(row) + '\n')
        return ret
    def inp(self, inp):
        if self.game_turn >= 9:
            return 'すでにゲームは終了しています'

        i = dic[inp[0]]
        j = dic[inp[1]]
        if self.game[i][j] != '-':
            return 'すでに埋まっています'
        else:
            self.game[i][j] = self.next_turn
            if self.next_turn == 'X':
                self.next_turn = 'O'
            else:
                self.next_turn = 'X'

            self.game_turn += 1
            win = who_win(self.game)
            if win != '-':
                self.is_game_end = True
                return '{0}が勝ちました\n{1}'.format(win, self)
            elif self.game_turn >= 9:
                self.is_game_end = True
                return '引き分けです\n{0}'.format(self)
            else:
                return str(self)

def inputdata(file_path):
    with open(file_path, 'r', encoding='ascii') as f:
        txt_lines = f.readlines()
        game = [['-' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                game[i][j] = txt_lines[i][j]
        return Board(game)

def solve6():
    board = Board([['-' for _ in range(3)] for _ in range(3)])
    while board.game_turn < 9:
        inp = input()
        print('先手: {0}'.format(inp))
        print(board.inp(inp))
        if board.is_game_end:
            return
        inp = choice(board.game, 'X')
        print('後手: {0}'.format(inp))
        print(board.inp(inp))
        if board.is_game_end:
            return

solve6()
