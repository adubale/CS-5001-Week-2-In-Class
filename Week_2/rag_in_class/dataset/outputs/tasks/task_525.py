def parallel_lines(line1, line2):
    """Check if two lines are parallel by comparing their slopes.

    Args:
        line1: A tuple or list representing a line in the form (y_intercept, slope).
        line2: A tuple or list representing a line in the form (y_intercept, slope).

    Returns:
        bool: True if the lines are parallel (slopes are equal), False otherwise.
    """
    return line1[0] / line1[1] == line2[0] / line2[1]
