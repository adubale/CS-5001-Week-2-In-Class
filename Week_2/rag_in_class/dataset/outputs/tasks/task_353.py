def remove_column(list1, n):
    """Remove the nth column from each sublist in list1.

    Args:
        list1: List of lists where each sublist represents a row.
        n: Index of the column to remove (0-based).

    Returns:
        The modified list with the nth column removed from each sublist.
    """
    for sublist in list1:
        if n < len(sublist):
            del sublist[n]
    return list1
