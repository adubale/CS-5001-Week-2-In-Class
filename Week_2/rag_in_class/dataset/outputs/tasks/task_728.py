def sum_list(lst1, lst2):
    """Return a new list where each element is the sum of corresponding elements from lst1 and lst2.

    Args:
        lst1: First list of numbers
        lst2: Second list of numbers (must be same length as lst1)

    Returns:
        List of summed elements

    Raises:
        IndexError: If lists are of different lengths (due to list indexing)
    """
    return [a + b for a, b in zip(lst1, lst2)]
