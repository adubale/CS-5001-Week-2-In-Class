import math

def sumofFactors(n: int) -> int:
    """Calculate the sum of proper factors of n, with special handling for even numbers.

    For odd numbers, returns 0. For even numbers, computes the sum of all proper factors
    (excluding n itself) by factorizing n and applying the formula for sum of divisors.

    Args:
        n: The integer to factorize (must be non-negative)

    Returns:
        Sum of proper factors if n is even, 0 if n is odd
    """
    if n % 2 != 0:
        return 0

    result = 1
    remaining = n

    for i in range(2, int(math.sqrt(remaining)) + 1):
        count = 0
        current_sum = 1
        current_term = 1

        while remaining % i == 0:
            count += 1
            remaining = remaining // i

            if i == 2 and count == 1:
                current_sum = 0

            current_term *= i
            current_sum += current_term

        result *= current_sum

    if remaining >= 2:
        result *= (1 + remaining)

    return result
