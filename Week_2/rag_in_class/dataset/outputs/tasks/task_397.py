def median_numbers(a: float, b: float, c: float) -> float:
    """Return the median value of three numbers a, b, and c.

    The median is the number that would be in the middle if the three numbers
    were sorted in ascending order.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The median value of the three input numbers
    """
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
