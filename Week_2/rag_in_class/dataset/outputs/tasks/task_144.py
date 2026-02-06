def sum_Pairs(arr, n):
    """Calculate a weighted sum of array elements based on their positions.

    For each element at index i (0-based), the weight is:
    - Positive contribution: i * arr[i]
    - Negative contribution: (n-1-i) * arr[i]
    The total sum is the sum of all these weighted contributions.

    Args:
        arr: List of numbers to be processed
        n: Number of elements to consider (must be <= len(arr))

    Returns:
        The computed weighted sum
    """
    total = 0
    for i in range(n - 1, -1, -1):
        weight = i - (n - 1 - i)
        total += weight * arr[i]
    return total
