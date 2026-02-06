import math

def sumofFactors(n: int) -> int:
    """Calculate the sum of all factors of n, excluding n itself.

    Args:
        n: An integer to compute the sum of factors for.

    Returns:
        The sum of all factors of n (excluding n), or 0 if n is odd.
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
