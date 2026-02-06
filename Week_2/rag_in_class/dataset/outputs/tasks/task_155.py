def even_bit_toggle_number(n: int) -> int:
    """Toggle the bits at even positions (0-indexed from the right) in the integer n.

    Args:
        n: The integer whose bits are to be toggled.

    Returns:
        The integer with even-positioned bits toggled.
    """
    result = 0
    bit_position = 0
    temp = n

    while temp > 0:
        if bit_position % 2 == 1:  # Even position (0-indexed)
            result |= 1 << bit_position
        bit_position += 1
        temp >>= 1

    return n ^ result
