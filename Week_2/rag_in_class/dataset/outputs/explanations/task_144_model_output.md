# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    """Calculate the sum of pairs in the array with a specific weighting pattern.

    For each element at index i (0-based), the contribution to the sum is:
    i * arr[i] - (n - 1 - i) * arr[i]

    This simplifies to: (2*i - (n - 1)) * arr[i]

    Args:
        arr: List of numbers to process
        n: Length of the array (must match len(arr))

    Returns:
        The computed sum based on the weighting formula
    """
    total = 0
    for i in range(n - 1, -1, -1):
        # Calculate the weighted contribution for each element
        weight = 2 * i - (n - 1)
        total += weight * arr[i]
    return total
```

- Preserved the exact mathematical formula and iteration order (backwards)
- Renamed `sum` to `total` to avoid shadowing built-in
- Extracted the weight calculation for clarity while maintaining identical computation
- Added docstring explaining the formula without changing behavior
- Kept the same parameter names and return type
- Maintained the same loop bounds and iteration direction
- Preserved the exact same numerical computation for each element
- No changes to edge case handling (works with any n and array length)
- No changes to exception behavior (none in original)
