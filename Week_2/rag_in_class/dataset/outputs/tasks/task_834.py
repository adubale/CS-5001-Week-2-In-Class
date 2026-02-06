def generate_matrix(n: int) -> list[list[int]]:
    """
    Generate an n x n matrix filled with numbers from 1 to n² in a spiral order.

    Args:
        n: The size of the matrix (must be positive). Returns empty list if n <= 0.

    Returns:
        A list of lists representing the spiral matrix, or empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize an n x n matrix filled with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Define the boundaries of the current spiral layer
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1
    current = 1

    while current <= n * n:
        # Fill top row from left to right
        for col in range(col_start, col_end + 1):
            matrix[row_start][col] = current
            current += 1
        row_start += 1

        # Fill right column from top to bottom
        for row in range(row_start, row_end + 1):
            matrix[row][col_end] = current
            current += 1
        col_end -= 1

        # Fill bottom row from right to left (if still within bounds)
        if row_start <= row_end:
            for col in range(col_end, col_start - 1, -1):
                matrix[row_end][col] = current
                current += 1
            row_end -= 1

        # Fill left column from bottom to top (if still within bounds)
        if col_start <= col_end:
            for row in range(row_end, row_start - 1, -1):
                matrix[row][col_start] = current
                current += 1
            col_start += 1

    return matrix
