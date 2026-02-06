def common_element(list1, list2):
    """Check if there is at least one common element between two lists.

    Returns:
        bool: True if any element exists in both lists, False otherwise.
    """
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False
