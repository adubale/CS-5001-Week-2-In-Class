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
def median_numbers(a, b, c):
    """Return the median of three numbers a, b, and c."""
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
```

- Preserved exact behavior for all input combinations
- Improved readability with clear conditional logic
- Maintained same return type (int/float)
- Handled all edge cases (equal values, negative numbers, etc.)
- Reduced nesting levels for better maintainability
- Used direct comparisons instead of nested if-else
- Kept function signature unchanged
- Ensured same precision for floating-point inputs
- Validated against all test cases in pytest file
