R = 3
C = 3

def min_cost(cost: list[list[int]], m: int, n: int) -> int:
    """Calculate the minimum cost path from top-left to bottom-right of a cost matrix.

    Args:
        cost: 2D list representing the cost matrix (0-indexed, but m and n are 1-indexed)
        m: Row index (1-indexed) of the target cell
        n: Column index (1-indexed) of the target cell

    Returns:
        Minimum cost to reach cell (m, n) from (0, 0) moving only right or down
    """
    # Initialize DP table with zeros
    dp_table = [[0 for _ in range(C)] for _ in range(R)]

    # Base case: starting cell
    dp_table[0][0] = cost[0][0]

    # Fill first column (only down moves)
    for i in range(1, m + 1):
        dp_table[i][0] = dp_table[i - 1][0] + cost[i][0]

    # Fill first row (only right moves)
    for j in range(1, n + 1):
        dp_table[0][j] = dp_table[0][j - 1] + cost[0][j]

    # Fill rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp_table[i][j] = min(dp_table[i - 1][j - 1], dp_table[i - 1][j], dp_table[i][j - 1]) + cost[i][j]

    return dp_table[m][n]
