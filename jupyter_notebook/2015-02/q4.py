def func1_v2(n):
    Max = 1000000+7
    memo = [0 for _ in range(Max)]
    memo[0] = 1
    mod = 1<<24
    for i in range(1, Max):
        memo[i] = (161 * memo[i-1]+2457) % mod
    return memo[n]

def solve4():
    n = 1000000
    print(func1_v2(n))

solve4()
