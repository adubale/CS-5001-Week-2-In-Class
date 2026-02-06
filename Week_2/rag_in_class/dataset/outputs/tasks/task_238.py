def number_of_substrings(s: str) -> int:
    """Return the number of possible substrings in the input string.

    The number of substrings of a string of length n is given by the formula n*(n+1)/2.
    This includes all possible contiguous sequences of characters.

    Args:
        s: The input string to count substrings for.

    Returns:
        The count of substrings as an integer.
    """
    str_len = len(s)
    return int(str_len * (str_len + 1) / 2)
