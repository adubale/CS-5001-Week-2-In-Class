def filter_oddnumbers(nums):
    """Return a list of odd numbers from the input list.

    Args:
        nums: List of integers to filter.

    Returns:
        List of odd integers from the input.
    """
    return [x for x in nums if x % 2 != 0]
