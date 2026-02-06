def median_numbers(a: float, b: float, c: float) -> float:
    """Return the median of three numbers a, b, and c.

    The median is the number that would be in the middle if the three numbers
    were sorted in ascending order.
    """
    if (a <= b <= c) or (c <= b <= a):
        return b
    if (b <= a <= c) or (c <= a <= b):
        return a
    return c
