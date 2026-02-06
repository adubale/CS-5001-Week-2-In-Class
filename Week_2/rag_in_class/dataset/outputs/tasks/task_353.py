def remove_column(list1: list, n: int) -> list:
    """Remove the nth column from each row in the 2D list.

    Args:
        list1: A 2D list where each element is a list representing a row.
        n: The index of the column to remove from each row.

    Returns:
        The modified 2D list with the nth column removed from each row.

    Note:
        This function mutates the input list and its sublists in-place.
    """
    for row in list1:
        del row[n]
    return list1
