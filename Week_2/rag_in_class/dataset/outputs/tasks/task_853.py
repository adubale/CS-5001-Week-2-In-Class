import math
from typing import Union

def sum_of_odd_factors(n: int) -> Union[int, float]:
    """
    Calculate the sum of odd factors of a given integer n.

    The function works by:
    1. Removing all factors of 2 (even factors)
    2. For each odd factor i, calculate the sum of the geometric series 1 + i + i^2 + ... + i^k
       where k is the exponent of i in the prime factorization of n
    3. Multiply these sums together to get the total sum of odd factors

    Args:
        n: The integer to calculate odd factors for

    Returns:
        The sum of all odd factors of n
    """
    result = 1

    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check odd factors from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        current_sum = 1
        current_term = 1

        # Factor out all occurrences of i
        while n % i == 0:
            count += 1
            n = n // i
            current_term *= i
            current_sum += current_term

        result *= current_sum

    # If remaining n is a prime number >= 3, add it to the sum
    if n >= 2:
        result *= (1 + n)

    return result
