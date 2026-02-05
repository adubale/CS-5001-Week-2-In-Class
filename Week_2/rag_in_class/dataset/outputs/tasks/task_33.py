def decimal_To_Binary(N):
    if N == 0:
        return 0
    B_Number = 0
    cnt = 0
    while N != 0:
        rem = N % 2
        B_Number += rem * (10 ** cnt)
        N = N // 2
        cnt += 1
    return B_Number
