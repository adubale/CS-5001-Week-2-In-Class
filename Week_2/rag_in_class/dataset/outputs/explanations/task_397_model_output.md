# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a: float, b: float, c: float) -> float:
    """Return the median value of three numbers a, b, and c.

    The median is the number that would be in the middle if the three numbers
    were sorted in ascending order.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The median value of the three input numbers
    """
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c
```

- Preserved exact function signature and return type
- Added type hints and docstring without changing runtime behavior
- Maintained all conditional logic exactly as in original
- Kept all return statements in the same positions
- Preserved all comparison operations and their order
- No changes to the algorithm or decision flow
- Improved readability through consistent formatting and documentation
- Maintained all edge case handling (equal values, negative numbers, etc.)
- No changes to variable names that could affect behavior
- All test cases should pass without modification
