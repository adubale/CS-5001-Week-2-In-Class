def first_non_repeating_character(str1: str) -> str | None:
    """Return the first non-repeating character in the string, or None if all characters repeat.

    Args:
        str1: The input string to search.

    Returns:
        The first character that appears exactly once, or None if no such character exists.
    """
    char_order = []
    char_counts = {}

    for char in str1:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            char_order.append(char)

    for char in char_order:
        if char_counts[char] == 1:
            return char

    return None
