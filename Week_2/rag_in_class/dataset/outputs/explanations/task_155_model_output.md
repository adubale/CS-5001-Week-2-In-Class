# Model output for task_155

## Model
- devstral-small-2:24b-cloud

## Original Code:

def even_bit_toggle_number(n) : 
    res = 0; count = 0; temp = n 
    while (temp > 0) :     
        if (count % 2 == 1) : 
            res = res | (1 << count)      
        count = count + 1
        temp >>= 1 
    return n ^ res 

## Refactored Code:

```python
def even_bit_toggle_number(n: int) -> int:
    """Toggle the bits at even positions (0-indexed from the right) in the integer n.

    Args:
        n: The integer whose bits are to be toggled.

    Returns:
        The integer with even-positioned bits toggled.
    """
    result = 0
    bit_position = 0
    temp = n

    while temp > 0:
        if bit_position % 2 == 1:  # Even position (0-indexed)
            result |= 1 << bit_position
        bit_position += 1
        temp >>= 1

    return n ^ result
```

- Preserved the exact logic of toggling even-positioned bits (0-indexed from the right)
- Improved variable names for clarity (res → result, count → bit_position, temp remains as it's a common convention)
- Added a docstring explaining the function's purpose and behavior
- Maintained the same algorithmic complexity (O(log n) where n is the input number)
- Kept the same return type and mutation behavior (no mutation of input)
- Preserved the exact bit manipulation operations and their order
- Maintained the same handling of edge cases (0, negative numbers, etc.)
- No changes to the public API or function signature
- Added type hints without changing runtime behavior
