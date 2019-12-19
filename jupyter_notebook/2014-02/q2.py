import sys

memo = [0] * 100
memo[0], memo[1] = 0, 1
def init():
    for i in range(2, 99):
        memo[i] = memo[i - 1] + memo[i - 2]

def solve2(x):
    init()
    return memo[x]

inp = int(sys.argv[1])

print(solve2(inp))
