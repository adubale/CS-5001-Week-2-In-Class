def mul_consecutive_nums(nums):
    """Multiply each pair of consecutive numbers in the input list.

    Args:
        nums: List of numbers (int or float)

    Returns:
        List of products of consecutive pairs. Returns empty list if input has 0 or 1 elements.
    """
    if len(nums) < 2:
        return []
    return [a * b for a, b in zip(nums[:-1], nums[1:])]
