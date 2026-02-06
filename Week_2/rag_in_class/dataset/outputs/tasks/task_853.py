import math

def sum_of_odd_Factors(n: int) -> int:
    """
    Calculate the sum of odd factors of a given integer n.

    This function computes the sum of all odd factors of n by:
    1. Removing all factors of 2 (even factors)
    2. For each odd factor, calculating the sum of its powers in the factorization
    3. Multiplying these sums together

    Args:
        n: The integer to factorize (must be positive)

    Returns:
        The sum of all odd factors of n

    Examples:
        >>> sum_of_odd_Factors(12)  # Factors: 1, 3 → Sum: 1 + 3 = 4
        4
        >>> sum_of_odd_Factors(9)   # Factors: 1, 3, 9 → Sum: 1 + 3 + 9 = 13
        13
    """
    result = 1

    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check odd factors starting from 3 up to sqrt(n)
    for factor in range(3, int(math.sqrt(n)) + 1):
        count = 0
        current_sum = 1
        current_term = 1

        # Factor out all occurrences of the current factor
        while n % factor == 0:
            count += 1
            n = n // factor
            current_term *= factor
            current_sum += current_term

        result *= current_sum

    # Handle remaining prime factor (if n > 1)
    if n >= 2:
        result *= (1 + n)

    return result
