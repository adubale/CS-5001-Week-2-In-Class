def count_Hexadecimal(L: int, R: int) -> int:
    """Count numbers in range [L, R] that contain at least one hexadecimal digit (A-F).

    Args:
        L: Start of range (inclusive)
        R: End of range (inclusive)

    Returns:
        Count of numbers in [L, R] with at least one hexadecimal digit
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
                    break
                current = current // 16
    return count
