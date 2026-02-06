def sum_list(lst1, lst2):
    """Return a new list where each element is the sum of corresponding elements from lst1 and lst2.

    Args:
        lst1: First input list of numbers
        lst2: Second input list of numbers

    Returns:
        List of summed elements at each index

    Raises:
        IndexError: If input lists have different lengths (preserves original behavior)
    """
    return [a + b for a, b in zip(lst1, lst2)]
