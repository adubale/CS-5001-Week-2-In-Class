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
    """Calculate a weighted sum of array elements based on their positions.

    For each element at index i (0-based), the weight is:
    - Positive contribution: i * arr[i]
    - Negative contribution: (n-1-i) * arr[i]
    The total sum is the sum of all these weighted contributions.

    Args:
        arr: List of numbers to be processed
        n: Number of elements to consider (must be <= len(arr))

    Returns:
        The computed weighted sum
    """
    total = 0
    for i in range(n - 1, -1, -1):
        weight = i - (n - 1 - i)
        total += weight * arr[i]
    return total
```

- Preserved the exact mathematical formula: `i*arr[i] - (n-1-i)*arr[i]`
- Renamed `sum` to `total` to avoid shadowing built-in `sum()`
- Extracted the weight calculation into a separate variable for clarity
- Added a descriptive docstring explaining the algorithm
- Maintained the same loop direction (backwards) and range
- Kept the same parameter names and function signature
- Preserved all numerical behavior exactly
- No changes to edge case handling (empty arrays, negative indices, etc.)
