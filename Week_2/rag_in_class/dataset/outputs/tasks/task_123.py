def amicable_numbers_sum(limit: int) -> int:
    """Calculate the sum of all amicable numbers up to the given limit.

    An amicable number is a number that is the sum of its proper divisors,
    excluding itself, and whose sum of proper divisors is the original number.

    Args:
        limit: The upper bound (inclusive) for finding amicable numbers.

    Returns:
        The sum of all amicable numbers up to the limit.

    Raises:
        Returns error messages for invalid inputs (non-integer or <= 0).
    """
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit < 1:
        return "Input must be bigger than 0!"

    amicables = set()

    for num in range(2, limit + 1):
        if num in amicables:
            continue

        # Calculate sum of proper divisors for num
        sum_fact = sum(fact for fact in range(1, num) if num % fact == 0)

        # Calculate sum of proper divisors for sum_fact
        sum_fact2 = sum(fact for fact in range(1, sum_fact) if sum_fact % fact == 0)

        # Check if they form an amicable pair
        if num == sum_fact2 and num != sum_fact:
            amicables.update({num, sum_fact2})

    return sum(amicables)
