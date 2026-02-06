def sum_Pairs(arr, n):
    """Calculate the sum of pairs in the array with a specific weighting pattern.

    For each element at index i (0-based), the contribution to the sum is:
    i * arr[i] - (n - 1 - i) * arr[i]

    This simplifies to: (2*i - (n - 1)) * arr[i]

    Args:
        arr: List of numbers to process
        n: Length of the array (must match len(arr))

    Returns:
        The computed sum based on the weighting formula
    """
    total = 0
    for i in range(n - 1, -1, -1):
        # Calculate the weighted contribution for each element
        weight = 2 * i - (n - 1)
        total += weight * arr[i]
    return total
