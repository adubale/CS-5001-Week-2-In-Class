def remove_column(list1: list, n: int) -> list:
    """Remove the element at index n from each sublist in list1.

    Args:
        list1: A list of lists where each sublist has at least n+1 elements.
        n: The index of the element to remove from each sublist.

    Returns:
        The modified list1 with elements at index n removed from each sublist.
    """
    for sublist in list1:
        del sublist[n]
    return list1
