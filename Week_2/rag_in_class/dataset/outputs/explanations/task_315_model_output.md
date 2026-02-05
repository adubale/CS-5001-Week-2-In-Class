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
def find_Max_Len_Even(str):
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while i < n:
        if str[i] == ' ':
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1
    if currlen % 2 == 0:
        if maxlen < currlen:
            maxlen = currlen
            st = i - currlen
    if st == -1:
        return "-1"
    return str[st:st + maxlen]
```

- Maintained the exact logic and structure of the original function
- Improved readability with consistent indentation and spacing
- Preserved all edge case handling (empty strings, no even-length words)
- Kept the same return behavior ("-1" for no even-length words)
- Ensured the function still processes strings character by character
- Maintained the same variable naming for clarity
- Kept the same algorithm for tracking current and maximum lengths
- Preserved the exact same return value format
- Ensured the function handles spaces and word boundaries identically
- Maintained the same performance characteristics (O(n) time complexity)
