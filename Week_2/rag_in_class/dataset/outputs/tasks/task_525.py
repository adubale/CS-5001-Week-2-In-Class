def parallel_lines(line1, line2):
    """Check if two lines are parallel by comparing their slopes.

    Args:
        line1: Tuple (a, b) representing the line equation ax + by = 0
        line2: Tuple (c, d) representing the line equation cx + dy = 0

    Returns:
        bool: True if lines are parallel, False otherwise
    """
    # Handle edge cases where lines are vertical (b=0 or d=0)
    if line1[1] == 0 and line2[1] == 0:
        return True  # Both vertical lines are parallel
    if line1[1] == 0 or line2[1] == 0:
        return False  # One vertical, one not

    # Compare slopes using cross-multiplication to avoid floating-point precision issues
    return line1[0] * line2[1] == line2[0] * line1[1]
