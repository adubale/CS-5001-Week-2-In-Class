def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers (int or float)

    Returns:
        List of products where each element is the product of consecutive pairs
        from the input list. Returns empty list if input has fewer than 2 elements.
    """
    result = [b * a for a, b in zip(nums[:-1], nums[1:])]
    return result
