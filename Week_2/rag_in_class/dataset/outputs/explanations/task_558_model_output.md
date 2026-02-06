# Model output for task_558

## Model
- devstral-small-2:24b-cloud

## Original Code:

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

## Refactored Code:

```python
def digit_distance_nums(n1: int, n2: int) -> int:
    """Calculate the sum of digits in the absolute difference between two numbers.

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
- Improved readability with descriptive variable names
- Added type hints and docstring without changing runtime behavior
- Maintained identical mathematical operations and digit processing
- Kept the same handling of negative numbers via abs()
- Preserved the digit-by-digit summation logic
- Used generator expression instead of map for clarity
- Maintained identical return value for all cases
- No changes to edge case handling (zeros, negatives, etc.)
