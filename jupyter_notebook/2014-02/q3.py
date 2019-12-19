import sys
inp1 = sys.argv[1]
inp2 = sys.argv[2]

def solve3(s1, s2):
    carry = 0
    ret = ''
    for i in range(32):
        ch1 = s1[31 - i]
        ch2 = s2[31 - i]
        n1 = int(ch1)
        n2 = int(ch2)
        a = n1 + n2 + carry
        if (a >= 10):
            carry = 1
        else:
            carry = 0
        b = a % 10
        ret += str(b)
    return ret[::-1]

print(solve3(inp1, inp2))
