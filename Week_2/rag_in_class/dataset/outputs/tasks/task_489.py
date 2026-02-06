def frequency_Of_Largest(n, arr):
    """Return the frequency of the largest element in the array.

    Args:
        n: Length of the array (unused in logic but kept for API compatibility).
        arr: List of numbers to analyze.

    Returns:
        int: Count of how many times the largest value appears in the array.
    """
    if not arr:
        return 0

    max_value = arr[0]
    frequency = 1

    for value in arr[1:]:
        if value > max_value:
            max_value = value
            frequency = 1
        elif value == max_value:
            frequency += 1

    return frequency
