def sum_list(lst1, lst2):
    """Return a new list where each element is the sum of corresponding elements from lst1 and lst2.

    Args:
        lst1: List of numbers
        lst2: List of numbers (must be same length as lst1)

    Returns:
        List of sums with same length as input lists

    Raises:
        ValueError: If input lists have different lengths
    """
    if len(lst1) != len(lst2):
        raise ValueError("Input lists must have the same length")

    return [a + b for a, b in zip(lst1, lst2)]
