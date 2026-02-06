def number_of_substrings(s: str) -> int:
    """Return the number of possible substrings in the input string.

    The number of substrings in a string of length n is given by the formula:
    n * (n + 1) / 2, which is the sum of the first n natural numbers.

    Args:
        s: The input string.

    Returns:
        The count of all possible substrings as an integer.
    """
    str_len = len(s)
    return int(str_len * (str_len + 1) / 2)
