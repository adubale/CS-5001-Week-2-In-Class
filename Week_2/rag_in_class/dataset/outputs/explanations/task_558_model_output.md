# Model output for task_558

## Model
- devstral-small-2:24b-cloud

## Original Code:

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

## Refactored Code:

```python
def digit_distance_nums(n1: int, n2: int) -> int:
    """Calculate the sum of the digits in the absolute difference between two numbers.

    Args:
        n1: First integer
        n2: Second integer

    Returns:
        Sum of digits in the absolute difference between n1 and n2
    """
    difference = abs(n1 - n2)
    return sum(int(digit) for digit in str(difference))
```

- Preserved exact function signature and behavior
- Improved readability with type hints and docstring
- Simplified the implementation by breaking down the operations
- Maintained the same mathematical computation (absolute difference then digit sum)
- Kept the same handling of all edge cases (negative numbers, zeros, etc.)
- Used a generator expression instead of map for clarity
- No changes to numerical precision or behavior
- All test cases should pass without modification
