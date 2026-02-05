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
        list1: List of elements to filter.
        list2: List of elements to remove from list1.

    Returns:
        A new list containing elements from list1 that are not in list2.
        Preserves order and handles duplicates in list2 correctly.
    """
    return [x for x in list1 if x not in list2]
```

- Preserved the exact list comprehension logic for clarity and performance
- Added docstring to clarify behavior and edge case handling
- Maintained original function signature and return type
- Handles empty inputs and duplicates in list2 as specified
- No intermediate variables needed for this simple operation
- Follows Pythonic list filtering pattern
- No floating-point operations or mathematical formulas involved
- Return type is always a list, matching test expectations
