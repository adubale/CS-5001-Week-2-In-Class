def smallest_multiple(n: int) -> int:
    """Return the smallest positive multiple of n that is divisible by all integers from 1 to n.

    Args:
        n: A positive integer (n >= 1).

    Returns:
        The smallest multiple of n divisible by all integers from 1 to n.

    Examples:
        >>> smallest_multiple(5)
        60
        >>> smallest_multiple(10)
        2520
    """
    if n <= 2:
        return n

    i = n * 2
    # Generate factors from n down to 3 (since 1 and 2 are already handled by n>=3)
    factors = [number for number in range(n, 2, -1) if number * 2 > n]

    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if a == factors[-1] and i % a == 0:
                return i
