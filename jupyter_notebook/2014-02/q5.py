import sys
inp1 = sys.argv[1]
inp2 = sys.argv[2]

def solve5(s1, s2):
    n1 = int(s1)
    n2 = int(s2)
    return n1 / (10**(31 - n2))

print(solve5(inp1, inp2))
