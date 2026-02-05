def mul_consecutive_nums(nums):
    """Multiply each element with the next consecutive element in the list.

    Args:
        nums: List of numbers (int or float)

    Returns:
        List of products where each element is the product of consecutive pairs
        from the input list. Returns empty list if input has 0 or 1 elements.

    Examples:
        >>> mul_consecutive_nums([1, 2, 3, 4])
        [2, 6, 12]
        >>> mul_consecutive_nums([5])
        []
        >>> mul_consecutive_nums([])
        []
    """
    if len(nums) < 2:
        return []
    return [b * a for a, b in zip(nums[:-1], nums[1:])]
