def decimal_To_Binary(N: int) -> int:
    """Convert a decimal integer to its binary representation as an integer.

    Args:
        N: The decimal integer to convert (must be non-negative).

    Returns:
        The binary representation of N as an integer (e.g., 5 -> 101).
        Returns 0 if N is 0.
    """
    binary_number = 0
    position = 0

    while N != 0:
        remainder = N % 2
        binary_number += remainder * (10 ** position)
        N = N // 2
        position += 1

    return binary_number
