def solve2():
    Max = 100
    memo = [0 for _ in range(Max)]
    memo[0] = 1
    mod = 1<<24
    # f(0) = 1でodd
    cnt = 0
    for i in range(1, Max):
        memo[i] = (161 * memo[i-1]+2457) % mod
        if memo[i] % 2 == 0:
            cnt += 1
    print(cnt)

solve2()
