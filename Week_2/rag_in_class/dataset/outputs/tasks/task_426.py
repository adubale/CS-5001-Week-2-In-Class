def filter_oddnumbers(nums):
    """Return a list containing only the odd numbers from the input iterable.

    Args:
        nums: An iterable of numbers to filter.

    Returns:
        A list of odd numbers from the input, preserving order.
    """
    return [num for num in nums if num % 2 != 0]
