def remove_elements(list1, list2):
    """Remove elements from list1 that are present in list2.

    Args:
        list1: List of elements to filter.
        list2: List of elements to remove from list1.

    Returns:
        A new list containing elements from list1 that are not in list2.
    """
    return [x for x in list1 if x not in list2]
