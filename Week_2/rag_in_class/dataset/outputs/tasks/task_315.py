def find_Max_Len_Even(s: str) -> str:
    """Find the longest even-length substring without spaces.

    Returns the longest substring with even length and no spaces.
    If no such substring exists, returns "-1".
    """
    max_len = 0
    start_index = -1
    current_len = 0

    for i, char in enumerate(s):
        if char == ' ':
            if current_len % 2 == 0 and current_len > max_len:
                max_len = current_len
                start_index = i - current_len
            current_len = 0
        else:
            current_len += 1

    # Check the last segment after the final space (or the entire string if no spaces)
    if current_len % 2 == 0 and current_len > max_len:
        max_len = current_len
        start_index = len(s) - current_len

    return s[start_index:start_index + max_len] if start_index != -1 else "-1"
