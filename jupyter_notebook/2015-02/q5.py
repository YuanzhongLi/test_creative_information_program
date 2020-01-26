def make_func2_memo(memo_size=10000):
    memo = [0 for _ in range(memo_size)]
    memo[0] = 1
    mod = 1<<26
    for i in range(1, len(memo)):
        memo[i] = (1103515245 * memo[i-1]+12345) % mod
    return memo

def solve5():
    memo = make_func2_memo()
    print('g(2): ', memo[2])
    print('g(3): ', memo[3])

solve5()
