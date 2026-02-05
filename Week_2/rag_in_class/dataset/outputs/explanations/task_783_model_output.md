# Model output for task_783

## Model
- devstral-small-2:24b-cloud

## Original Code:

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

## Refactored Code:

```python
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn

    if mx == mn:
        h = 0.0
    elif mx == r:
        h = (60.0 * ((g - b) / df) + 360.0) % 360.0
    elif mx == g:
        h = (60.0 * ((b - r) / df) + 120.0) % 360.0
    elif mx == b:
        h = (60.0 * ((r - g) / df) + 240.0) % 360.0

    s = 0.0 if mx == 0 else (df / mx) * 100.0
    v = mx * 100.0

    return (h, s, v)
```

- Preserved exact floating-point precision by using 255.0 and 60.0 as floats
- Simplified saturation calculation using ternary operator
- Maintained exact mathematical formulas for hue calculation
- Ensured all intermediate calculations use float division
- Kept return type as tuple (h, s, v) with exact order
- Handled edge case where mx=0 for saturation calculation
- Used modulo operation to keep hue within 0-360 range
- Maintained original function signature and name
- All calculations performed with sufficient precision for 15 decimal places
