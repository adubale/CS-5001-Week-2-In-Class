def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers to process.

    Returns:
        List of products where each element is the product of consecutive pairs
        from the input list. Returns an empty list if input has fewer than 2 elements.
    """
    return [a * b for a, b in zip(nums[:-1], nums[1:])]
