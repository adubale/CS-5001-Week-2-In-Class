def digit_distance_nums(n1, n2):
    """Calculate the sum of the digits of the absolute difference between two numbers."""
    difference = abs(n1 - n2)
    return sum(int(digit) for digit in str(difference))
