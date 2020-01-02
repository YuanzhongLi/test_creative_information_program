from N_DIGIT import baseNumber, baseNumbers

def biTo10(bi):
    ret = 0
    for index, b in enumerate(bi):
        ret += (2**index) * b
    return ret

def getReverse(n):
    bi = baseNumber(2, 8, n)
    b000 = bi[0]
    b001 = bi[1]
    b010 = bi[2]
    b011 = bi[3]
    b100 = bi[4]
    b101 = bi[5]
    b110 = bi[6]
    b111 = bi[7]
    bi[1], bi[3], bi[4], bi[6] = bi[4], bi[6], bi[1], bi[3]
    return biTo10(bi)

def hasReverse(n):
    return n == getReverse(n)

def solve2_3():
    ret = 0
    for i in range(256):
        if hasReverse(i):
            ret += 1
    return ret

print(solve2_3())
