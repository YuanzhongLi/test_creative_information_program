def solve7():
    max_k = 67108864
    g_mod = 1<<26
    h_mod = 1<<10
    g_cur = 1
    h_cur = 1
    for k in range(1, max_k+1):
        g_cur = (1103515245 * g_cur+12345) % g_mod
        h_cur = g_cur % h_mod
#         print(g_cur, h_cur)
        if h_cur == 1:
            return k
    return -1

k = solve7()
print(k)
