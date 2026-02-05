def common_element(list1, list2):
    """Check if there is any common element between two lists."""
    return any(x in list2 for x in list1)
