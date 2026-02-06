def smallest_divisor(n: int) -> int:
    """Return the smallest divisor of n greater than 1.

    For even numbers, returns 2 immediately.
    For odd numbers, checks divisibility starting from 3, incrementing by 2.
    If no divisor is found, returns n (indicating n is prime).
    """
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n
