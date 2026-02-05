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
    total = 0
    for i in range(n - 1, -1, -1):
        total += i * arr[i] - (n - 1 - i) * arr[i]
    return total
```

- Simplified variable naming from `sum` to `total` to avoid shadowing built-in `sum()`
- Maintained exact same logic and behavior as original implementation
- Preserved the backward iteration and calculation formula precisely
- Kept the same function signature and return type
- Ensured no changes to mathematical operations or edge case handling
- Code is now more readable while being functionally identical
