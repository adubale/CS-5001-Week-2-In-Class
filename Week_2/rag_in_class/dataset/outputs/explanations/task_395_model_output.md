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
def first_non_repeating_character(str1):
    """Return the first non-repeating character in the string, or None if all characters repeat."""
    char_order = []
    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_order.append(char)

    for char in char_order:
        if char_count[char] == 1:
            return char

    return None
```

- Maintained the exact function signature and behavior as required
- Improved variable naming for clarity (e.g., `ctr` → `char_count`)
- Preserved the original logic flow while making the code more readable
- Handled edge cases implicitly (empty string returns None, all repeating characters returns None)
- Maintained the same return type (char or None) as specified
- Kept the same time complexity (O(n)) and space complexity (O(n))
- Added a docstring to clarify the function's purpose
- Preserved the exact behavior validated by the provided tests
