def find_Max_Len_Even(s: str) -> str:
    """Find the longest even-length substring without spaces.

    Returns the longest substring with even length that contains no spaces.
    If no such substring exists, returns "-1".

    Args:
        s: Input string to search

    Returns:
        The longest even-length space-free substring, or "-1" if none exists
    """
    max_length = 0
    max_start = -1
    current_length = 0
    current_start = 0

    for i, char in enumerate(s):
        if char == ' ':
            if current_length > 0 and current_length % 2 == 0:
                if current_length > max_length:
                    max_length = current_length
                    max_start = current_start
            current_length = 0
            current_start = i + 1
        else:
            current_length += 1

    # Check the last segment after the loop ends
    if current_length > 0 and current_length % 2 == 0:
        if current_length > max_length:
            max_length = current_length
            max_start = current_start

    return s[max_start:max_start + max_length] if max_start != -1 else "-1"
