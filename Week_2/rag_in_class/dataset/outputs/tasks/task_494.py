def binary_to_integer(test_tup):
    """Convert a tuple of binary digits (0s and 1s) to a decimal integer string.

    Args:
        test_tup: A tuple of integers representing binary digits (0 or 1).

    Returns:
        A string representation of the decimal integer formed by the binary digits.
    """
    binary_str = "".join(str(digit) for digit in test_tup)
    decimal_value = int(binary_str, 2)
    return str(decimal_value)
