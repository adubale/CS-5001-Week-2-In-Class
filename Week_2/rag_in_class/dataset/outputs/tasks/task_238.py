def number_of_substrings(s: str) -> int:
    """Calculate the number of possible substrings in a string.

    Args:
        s: Input string

    Returns:
        int: Number of substrings (n*(n+1)/2 where n is string length)
    """
    str_len = len(s)
    return int(str_len * (str_len + 1) / 2)
