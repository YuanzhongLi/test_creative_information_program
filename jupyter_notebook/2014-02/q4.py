import sys
inp = int(sys.argv[1])

memo = [0] * 141
memo[0], memo[1] = 0, 1
def init():
    for i in range(2, len(memo)):
        memo[i] = memo[i - 1] + memo[i - 2]
def solve4(x):
    init()
    return memo[x]

print(solve4(inp))
