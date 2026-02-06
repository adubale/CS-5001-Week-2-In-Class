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

    Returns the longest substring with even length and no spaces.
    If no such substring exists, returns "-1".
    """
    max_len = 0
    start_index = -1
    current_len = 0

    for i, char in enumerate(s):
        if char == ' ':
            if current_len % 2 == 0 and current_len > max_len:
                max_len = current_len
                start_index = i - current_len
            current_len = 0
        else:
            current_len += 1

    # Check the last segment after the final space (or the entire string if no spaces)
    if current_len % 2 == 0 and current_len > max_len:
        max_len = current_len
        start_index = len(s) - current_len

    return s[start_index:start_index + max_len] if start_index != -1 else "-1"
```

- Preserved exact function signature and behavior
- Improved variable names for clarity (e.g., `s` instead of `str`, `start_index` instead of `st`)
- Added docstring explaining the function's purpose
- Used `enumerate` for cleaner iteration
- Simplified the final segment check by using `len(s)` instead of `i`
- Maintained all edge case handling (no even-length substrings returns "-1")
- Kept the same logic for tracking max length and start position
- Preserved the exact return format (substring or "-1")
- No changes to numerical or string operations that could affect behavior
