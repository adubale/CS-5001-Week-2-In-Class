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

- Simplified variable name from `sum` to `total` to avoid shadowing built-in `sum()`
- Maintained exact same logic and behavior as original
- Preserved backward iteration and calculation formula
- Kept function signature and return type unchanged
- No changes to edge case handling (function works for all valid n)
- Mathematical operations remain identical to original implementation
- Code is now more readable while being functionally equivalent
