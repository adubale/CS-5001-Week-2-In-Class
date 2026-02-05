# Model output for task_901

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

## Refactored Code:

```python
def smallest_multiple(n):
    if n <= 2:
        return n
    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    while True:
        divisible = True
        for a in factors:
            if i % a != 0:
                divisible = False
                i += n
                break
        if divisible:
            return i
```

- Preserved the exact logic and behavior of the original function
- Improved readability by using a boolean flag `divisible` instead of nested if conditions
- Maintained the same edge case handling (n <= 2)
- Kept the same factor calculation and loop structure
- Ensured the function returns the smallest multiple divisible by all numbers from 2 to n
- All test cases should pass exactly as before
- No changes to the mathematical logic or algorithm
- Code is more maintainable while being functionally identical
