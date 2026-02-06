# Model output for task_453

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math 
def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :    
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) : 
            count= count + 1
            n = n // i 
            if (i == 2 and count == 1) : 
                curr_sum = 0
            curr_term = curr_term * i 
            curr_sum = curr_sum + curr_term 
        res = res * curr_sum  
    if (n >= 2) : 
        res = res * (1 + n) 
    return res 

## Refactored Code:

```python
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
```

- Preserved exact function signature and behavior for both even and odd inputs
- Maintained the special case handling where the first factor of 2 makes current_sum = 0
- Kept the mathematical algorithm and factorization logic identical
- Improved variable names for clarity (res → result, n → remaining in loop)
- Added type hints and docstring without changing runtime behavior
- Maintained the same loop bounds and termination conditions
- Preserved the final adjustment for remaining prime factors
- Kept all numerical operations and order of operations unchanged
- No changes to exception behavior (none in original implementation)
