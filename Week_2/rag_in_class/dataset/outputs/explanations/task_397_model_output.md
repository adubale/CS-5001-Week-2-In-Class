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
    """Return the median of three numbers a, b, and c.

    The median is the number that would be in the middle if the three numbers
    were sorted in ascending order.
    """
    if (a <= b <= c) or (c <= b <= a):
        return b
    if (b <= a <= c) or (c <= a <= b):
        return a
    return c
```

- Preserved exact behavior for all input combinations
- Improved readability with clear conditional logic
- Added type hints and docstring without changing runtime behavior
- Maintained original function signature and return type
- Reduced nested conditionals to flat comparisons
- Kept algorithmic complexity at O(1)
- Preserved all edge cases (duplicates, equal values, etc.)
- No changes to numerical precision or comparison semantics
- All test cases should pass without modification
