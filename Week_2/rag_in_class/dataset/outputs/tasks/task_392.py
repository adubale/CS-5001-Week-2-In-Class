def get_max_sum(n):
    if n < 0:
        return 0
    res = [0] * (n + 1)
    res[0] = 0
    res[1] = 1
    for i in range(2, n + 1):
        res[i] = max(i, res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5])
    return res[n]
