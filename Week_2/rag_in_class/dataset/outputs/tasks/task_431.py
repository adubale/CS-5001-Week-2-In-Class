def common_element(list1, list2):
    """Check if there is any common element between two lists."""
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False
