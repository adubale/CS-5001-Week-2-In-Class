# Model output for task_315

## Model
- devstral-small-2:24b-cloud

## Original Code:

def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen] 

## Refactored Code:

```python
def find_Max_Len_Even(s: str) -> str:
    """Find the longest even-length substring without spaces.

    Returns the longest substring with even length that contains no spaces.
    If no such substring exists, returns "-1".

    Args:
        s: Input string to search

    Returns:
        The longest even-length space-free substring, or "-1" if none exists
    """
    max_length = 0
    max_start = -1
    current_length = 0
    current_start = 0

    for i, char in enumerate(s):
        if char == ' ':
            if current_length > 0 and current_length % 2 == 0:
                if current_length > max_length:
                    max_length = current_length
                    max_start = current_start
            current_length = 0
            current_start = i + 1
        else:
            current_length += 1

    # Check the last segment after the loop ends
    if current_length > 0 and current_length % 2 == 0:
        if current_length > max_length:
            max_length = current_length
            max_start = current_start

    return s[max_start:max_start + max_length] if max_start != -1 else "-1"
```

- Preserved exact function signature and behavior
- Improved variable naming for clarity (maxlen→max_length, st→max_start, etc.)
- Added docstring explaining function purpose and behavior
- Used enumerate() for cleaner iteration
- Maintained same edge case handling (returns "-1" when no valid substring)
- Kept same logic for tracking current and max segments
- Preserved mutation behavior (no mutation of input string)
- Maintained same return value format and conditions
- Kept identical numerical comparisons and logic flow
