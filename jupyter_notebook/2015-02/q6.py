def solve6():
    n = 1
    mod = 1<<26
    cur = 1
    k = 1
    while True:
        cur = (1103515245 * cur+12345) % mod
        if cur == 1:
            break
        k += 1
        if k > 100000000:
            k = -1
            break
    return k
k = solve6()
print(k)
