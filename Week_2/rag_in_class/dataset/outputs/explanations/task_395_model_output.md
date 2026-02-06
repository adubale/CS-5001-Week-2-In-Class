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

- Preserved exact function signature and return type behavior (returns `str` or `None`)
- Improved variable names (`ctr` → `char_counts`, `c` → `char`) for clarity
- Added type hints and docstring without changing runtime behavior
- Maintained original algorithm and logic flow exactly
- Kept the same order of operations and return values
- No changes to edge case handling (empty string, all repeats, etc.)
- Preserved the use of `None` as the return value for no matches
- No changes to mutation behavior (none in this function)
- No changes to exception behavior (none raised in this function)
