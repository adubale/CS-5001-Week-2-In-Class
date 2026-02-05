def generate_matrix(n):
    if n <= 0:
        return []
    matrix = [[0] * n for _ in range(n)]
    row_st, row_ed = 0, n - 1
    col_st, col_ed = 0, n - 1
    current = 1
    while current <= n * n:
        for c in range(col_st, col_ed + 1):
            matrix[row_st][c] = current
            current += 1
        row_st += 1
        for r in range(row_st, row_ed + 1):
            matrix[r][col_ed] = current
            current += 1
        col_ed -= 1
        for c in range(col_ed, col_st - 1, -1):
            matrix[row_ed][c] = current
            current += 1
        row_ed -= 1
        for r in range(row_ed, row_st - 1, -1):
            matrix[r][col_st] = current
            current += 1
        col_st += 1
    return matrix
