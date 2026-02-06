# Model output for task_33

## Model
- devstral-small-2:24b-cloud

## Original Code:

def decimal_To_Binary(N): 
    B_Number = 0
    cnt = 0
    while (N != 0): 
        rem = N % 2
        c = pow(10,cnt)  
        B_Number += rem*c  
        N //= 2 
        cnt += 1
    return B_Number  

## Refactored Code:

```python
def decimal_To_Binary(N: int) -> int:
    """Convert a decimal integer to its binary representation as an integer.

    Args:
        N: The decimal integer to convert (must be non-negative).

    Returns:
        The binary representation of N as an integer (e.g., 5 -> 101).
        Returns 0 if N is 0.
    """
    binary_number = 0
    position = 0

    while N != 0:
        remainder = N % 2
        binary_number += remainder * (10 ** position)
        N = N // 2
        position += 1

    return binary_number
```

- Preserved exact function signature and behavior
- Improved variable names for clarity (B_Number -> binary_number, cnt -> position)
- Added docstring explaining purpose, args, and return value
- Maintained identical logic and control flow
- Kept same mathematical operations and order
- Preserved handling of edge cases (N=0, negative numbers if any)
- No changes to return type or exception behavior
- Code structure remains simple and straightforward
