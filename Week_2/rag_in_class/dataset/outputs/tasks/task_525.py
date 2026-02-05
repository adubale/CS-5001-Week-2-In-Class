def parallel_lines(line1, line2):
    """Check if two lines are parallel by comparing their slopes.

    Args:
        line1: Tuple of (m1, b1) representing line equation y = m1*x + b1
        line2: Tuple of (m2, b2) representing line equation y = m2*x + b2

    Returns:
        bool: True if lines are parallel (slopes are equal), False otherwise
    """
    m1, b1 = line1
    m2, b2 = line2
    return m1 == m2
