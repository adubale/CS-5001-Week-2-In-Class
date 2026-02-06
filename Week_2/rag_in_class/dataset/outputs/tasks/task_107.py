def count_Hexadecimal(L: int, R: int) -> int:
    """Count numbers in range [L, R] that contain hexadecimal digits (A-F) in their representation.

    Args:
        L: Start of range (inclusive)
        R: End of range (inclusive)

    Returns:
        Count of numbers containing hexadecimal digits (10-15) in their decimal representation
    """
    count = 0
    for num in range(L, R + 1):
        if 10 <= num <= 15:
            count += 1
        elif num > 15:
            current = num
            while current != 0:
                if current % 16 >= 10:
                    count += 1
                    break  # Only need to find one hex digit to count the number
                current = current // 16
    return count
