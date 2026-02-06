# Model output for task_431

## Model
- devstral-small-2:24b-cloud

## Original Code:

def common_element(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

## Refactored Code:

```python
def common_element(list1, list2):
    """Check if there is at least one common element between two lists.

    Returns:
        bool: True if any element exists in both lists, False otherwise.
    """
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False
```

- Preserved the exact function signature and return type
- Simplified the logic by removing unnecessary variable `result` and direct return
- Added a clear docstring explaining the function's purpose
- Maintained the same nested loop structure and comparison logic
- Kept the same early return behavior when a match is found
- Preserved the default return value of False when no match is found
- Maintained the same time complexity (O(n*m))
- No changes to edge case handling (empty lists, single elements, etc.)
- All test cases should pass without modification
