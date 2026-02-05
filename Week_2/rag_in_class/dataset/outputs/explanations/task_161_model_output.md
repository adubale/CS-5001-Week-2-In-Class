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
    """
    return [x for x in list1 if x not in list2]
```

- Preserved the exact list comprehension logic for clarity and performance
- Added docstring to clarify function purpose and parameters
- Maintained the original behavior of returning a new list without modifying inputs
- Handled edge cases implicitly (empty lists, duplicates in list2) through the list comprehension
- Ensured the function returns a list as expected by the tests
- No unnecessary changes to maintain exact test compatibility
