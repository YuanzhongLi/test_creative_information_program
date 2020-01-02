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

def remake(cell):
    div_idxs = []
    prev_c = -1
    for index, c in enumerate(cell):
        if c != prev_c:
            div_idxs.append(index)
            prev_c = c
    div_idxs.append(len(cell))

    array = []
    for i in range(len(div_idxs) - 1):
        tmp = []
        l = div_idxs[i]
        r = div_idxs[i+1]
        for j in range(l, r):
            tmp.append(cell[j])
        array.append(tmp)

    ret = []
    isException = False
    for index, block in enumerate(array):
        content = block[0]
        size = len(block)
        if size >= 3:
            if content == 1:
                if index == 0:
                    isException = True
                ret.extend([1 for _ in range(size - 1)])
            elif content == 0:
                ret.extend([0 for _ in range(size + 1)])
        else:
            if content == 1:
                ret.extend([1 for _ in range(size)])
            elif content == 0:
                ret.extend([0 for _ in range(size)])
    if isException:
        tmp = [ret[-1]]
        tmp.extend(ret[:-1])
        return tmp
    else:
        return ret

def update_cell(M, cell):
    cell_size = len(cell)
    ret = [0 for _ in range(cell_size)]
    for i, c in enumerate(cell):
        l = cell[(i-1) % cell_size]
        r = cell[(i+1) % cell_size]
        ret[i] = delta_func(M, l, c, r)
    return remake(cell)

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

def solve4_2(M):
    cell = []
    for zero_num in range(1, 11):
        array = []
        for i in range(zero_num):
            array.append(0)
        array.append(1)
        cell.extend(array)

    print_cell(cell)
    for t in range(1, 51):
    # while True:
        cell = update_cell(M, cell)
        print_cell(cell)
        if len(cell) < 3 or len(cell) > 2000:
            print('size-out-of-range')
            break

solve4_2(inp)
