# Model output for task_161

## Model
- devstral-small-2:24b-cloud

## Original Code:

def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

## Refactored Code:

```python
def remove_elements(list1, list2):
    """Remove elements from list1 that are present in list2.

    Args:
        list1: The list from which elements will be removed.
        list2: The list of elements to remove from list1.

    Returns:
        A new list containing only elements from list1 that are not in list2.
    """
    return [x for x in list1 if x not in list2]
```

- Preserved the exact same list comprehension logic for element removal
- Added a clear docstring explaining the function's purpose and parameters
- Maintained the same function signature and return type
- Kept the same behavior for all edge cases (empty lists, duplicates, etc.)
- No changes to the algorithmic complexity (O(n*m) where n and m are list lengths)
- Preserved the immutable behavior (returns a new list without modifying inputs)
- Maintained the same order of elements in the result as in the original list1
- No changes to exception handling (none in original implementation)
- Kept the same return value type (list) for all cases
