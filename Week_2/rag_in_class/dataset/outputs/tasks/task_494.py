def binary_to_integer(test_tup):
    """Convert a tuple of binary digits to an integer string.

    Args:
        test_tup: Tuple of binary digits (0s and 1s)

    Returns:
        String representation of the integer value
    """
    if not test_tup:
        return "0"
    binary_str = "".join(str(ele) for ele in test_tup)
    return str(int(binary_str, 2))
