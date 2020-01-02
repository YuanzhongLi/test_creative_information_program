import sys
inp = int(sys.argv[1])
from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def delta_func(M, l, c, r):
    bn = baseNumber(2, 8, M)
    index = biTo10([l, c, r])
    return bn[index]

def print_cell(cell):
    ret = ''
    for index, c in enumerate(cell):
        if index >= 100:
            break
        if c == 0:
            ret += '.'
        else:
            ret += '#'
    print(ret)

def update_cell(M, cell):
    cell_size = len(cell)
    ret = [0 for _ in range(cell_size)]
    for i, c in enumerate(cell):
        l = cell[(i-1) % cell_size]
        r = cell[(i+1) % cell_size]
        ret[i] = delta_func(M, l, c, r)
    return ret

def initailize(i):
    bn = baseNumber(2, 7, i)
    cnt = 0
    for bi in bn:
        if bi == 1:
            cnt += 1
    if cnt == 3:
        return 1
    else:
        return 0

def solve3_2(M):
    cell = [0 for _ in range(123)]
    for i, c in enumerate(cell):
        cell[i] = initailize(i)

    print_cell(cell)
    for t in range(1, 51):
        cell = update_cell(M, cell)
        print_cell(cell)

solve3_2(inp)
