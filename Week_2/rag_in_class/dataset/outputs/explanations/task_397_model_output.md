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
    """Return the median of three numbers a, b, c."""
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
```

- Simplified the logic by using direct comparisons to determine the median
- Maintained the exact same behavior as the original implementation
- Improved readability by reducing nested conditionals
- Preserved all edge cases (e.g., equal values)
- Kept the same return type (int or float depending on input)
- No changes to function signature or name
- All test cases should pass exactly as before
