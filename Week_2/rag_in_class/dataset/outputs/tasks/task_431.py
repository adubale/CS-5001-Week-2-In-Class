def common_element(list1, list2):
    """Check if there is at least one common element between two lists.

    Args:
        list1: First input list.
        list2: Second input list.

    Returns:
        bool: True if there is at least one common element, False otherwise.
    """
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False
