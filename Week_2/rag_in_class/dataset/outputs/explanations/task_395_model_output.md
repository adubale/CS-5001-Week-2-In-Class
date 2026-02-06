# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(str1: str) -> str | None:
    """Return the first non-repeating character in the string, or None if all characters repeat.

    Args:
        str1: The input string to search.

    Returns:
        The first character that appears exactly once, or None if no such character exists.
    """
    char_order = []
    char_counts = {}

    for char in str1:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            char_order.append(char)

    for char in char_order:
        if char_counts[char] == 1:
            return char

    return None
```

- Preserved exact function signature and return type behavior (None vs False)
- Improved variable names for clarity (ctr → char_counts, c → char)
- Added docstring explaining behavior without changing runtime
- Maintained original algorithm and order of operations
- Kept mutation behavior identical (no changes to input string)
- Preserved edge case handling (empty string, all repeats, etc.)
- No changes to numerical or precision behavior (none applicable)
- No changes to exception behavior (none raised)
- Maintained original order of character checking
- Added type hints without altering runtime behavior
