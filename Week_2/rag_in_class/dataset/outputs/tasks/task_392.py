def get_max_sum(n: int) -> int:
    """Calculate the maximum sum for a given integer n using a dynamic programming approach.

    The function computes the maximum sum for each integer from 0 to n, where the sum for
    a given integer i is the maximum of i itself or the sum of the values at i/2, i/3, i/4,
    and i/5 (using integer division).

    Args:
        n: The integer for which to compute the maximum sum.

    Returns:
        The maximum sum for the given integer n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    # Initialize the result list with base cases
    res = [0, 1]

    # Handle the case where n is 0 or 1 directly
    if n <= 1:
        return res[n]

    # Compute the maximum sum for each integer from 2 to n
    for i in range(2, n + 1):
        # Calculate the sum of the values at i/2, i/3, i/4, and i/5
        sum_divisors = res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]
        # The current value is the maximum of i or the sum of the divisors
        res.append(max(i, sum_divisors))

    return res[n]
