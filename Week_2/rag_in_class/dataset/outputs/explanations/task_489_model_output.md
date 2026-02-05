# Model output for task_489

## Model
- devstral-small-2:24b-cloud

## Original Code:

def frequency_Of_Largest(n,arr): 
    mn = arr[0] 
    freq = 1
    for i in range(1,n): 
        if (arr[i] >mn): 
            mn = arr[i] 
            freq = 1
        elif (arr[i] == mn): 
            freq += 1
    return freq 

## Refactored Code:

```python
def frequency_Of_Largest(n, arr):
    if n == 0:
        return 0
    max_val = arr[0]
    frequency = 1
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            frequency = 1
        elif arr[i] == max_val:
            frequency += 1
    return frequency
```

- Explicitly handle empty input case (n == 0) by returning 0
- Use more descriptive variable names (max_val instead of mn, frequency instead of freq)
- Maintain the same logic flow but with improved readability
- Preserve the exact behavior validated by the provided tests
- Keep the function signature unchanged as required
- Ensure the function works correctly for single-element inputs
- Maintain the original time complexity O(n) with single pass through the array
- Preserve the exact return value behavior for all edge cases
