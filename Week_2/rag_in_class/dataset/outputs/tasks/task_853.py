import math

def sum_of_odd_Factors(n):
    """Calculate the sum of odd factors of n by factorizing n and summing odd divisors."""
    if n == 0:
        return 0

    res = 1
    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors starting from 3 up to sqrt(n)
    i = 3
    max_factor = math.isqrt(n) + 1
    while i <= max_factor:
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
        # Update max_factor in case n changed significantly
        max_factor = math.isqrt(n) + 1
        i += 2  # Skip even numbers

    # If remaining n is a prime > 2
    if n > 1:
        res *= (1 + n)

    return res
