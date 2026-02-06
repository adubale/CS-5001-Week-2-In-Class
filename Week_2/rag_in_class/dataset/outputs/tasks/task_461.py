def upper_ctr(s: str) -> int:
    """Count the number of uppercase letters in the input string.

    Args:
        s: The input string to analyze.

    Returns:
        The count of uppercase letters in the string.
    """
    count = 0
    for char in s:
        if 'A' <= char <= 'Z':
            count += 1
    return count
