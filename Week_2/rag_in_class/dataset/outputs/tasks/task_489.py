def frequency_Of_Largest(n, arr):
    """Return the frequency of the largest element in the array.

    Args:
        n: Length of the array (unused in logic but kept for API compatibility).
        arr: List of numbers to analyze.

    Returns:
        int: Count of how many times the maximum value appears in the array.
    """
    if not arr:
        return 0

    max_val = arr[0]
    frequency = 1

    for num in arr[1:]:
        if num > max_val:
            max_val = num
            frequency = 1
        elif num == max_val:
            frequency += 1

    return frequency
