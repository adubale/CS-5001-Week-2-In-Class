def decimal_To_Binary(N):
    if N == 0:
        return 0
    binary = 0
    position = 0
    while N > 0:
        binary += (N % 2) * (10 ** position)
        N = N // 2
        position += 1
    return binary
