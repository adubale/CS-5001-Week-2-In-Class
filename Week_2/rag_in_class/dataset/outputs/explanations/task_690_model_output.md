# Model output for task_690

## Model
- devstral-small-2:24b-cloud

## Original Code:

def mul_consecutive_nums(nums):
    result = [b*a for a, b in zip(nums[:-1], nums[1:])]
    return result

## Refactored Code:

```python
def mul_consecutive_nums(nums):
    """Multiply each element with the next consecutive element in the list.

    Args:
        nums: List of numbers (int or float)

    Returns:
        List of products where each element is the product of consecutive pairs
        from the input list. Returns empty list if input has 0 or 1 elements.

    Examples:
        >>> mul_consecutive_nums([1, 2, 3, 4])
        [2, 6, 12]
        >>> mul_consecutive_nums([5])
        []
        >>> mul_consecutive_nums([])
        []
    """
    if len(nums) < 2:
        return []
    return [b * a for a, b in zip(nums[:-1], nums[1:])]
```

- Preserved exact behavior with list comprehension for consecutive multiplication
- Added explicit edge case handling for empty and single-element inputs
- Maintained original function signature and name
- Added docstring with clear examples and behavior description
- Used precise multiplication operation without rounding
- Kept the same return type (list) and structure
- No changes to core logic to ensure test compatibility
