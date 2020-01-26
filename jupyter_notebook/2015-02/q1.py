def func1(n):
    Max = 10000
    memo = [0 for _ in range(Max)]
    memo[0] = 1
    mod = 1<<24
    for i in range(1, Max):
        memo[i] = (161 * memo[i-1]+2457) % mod
    return memo[n]

def solve1():
    n = 100
    print(func1(n))

solve1()
