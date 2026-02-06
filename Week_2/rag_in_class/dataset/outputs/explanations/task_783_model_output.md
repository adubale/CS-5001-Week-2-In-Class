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
def rgb_to_hsv(r: float, g: float, b: float) -> tuple[float, float, float]:
    """Convert RGB values in the range 0-255 to HSV values in the range [0, 360), [0, 100], [0, 100].

    Args:
        r: Red component (0-255)
        g: Green component (0-255)
        b: Blue component (0-255)

    Returns:
        Tuple of (hue, saturation, value) where:
        - hue is in degrees [0, 360)
        - saturation is a percentage [0, 100]
        - value is a percentage [0, 100]
    """
    # Normalize RGB values to [0, 1] range
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    max_val = max(r_norm, g_norm, b_norm)
    min_val = min(r_norm, g_norm, b_norm)
    delta = max_val - min_val

    # Calculate Hue
    if max_val == min_val:
        hue = 0.0
    elif max_val == r_norm:
        hue = (60 * ((g_norm - b_norm) / delta) + 360) % 360
    elif max_val == g_norm:
        hue = (60 * ((b_norm - r_norm) / delta) + 120) % 360
    else:  # max_val == b_norm
        hue = (60 * ((r_norm - g_norm) / delta) + 240) % 360

    # Calculate Saturation
    saturation = 0.0 if max_val == 0 else (delta / max_val) * 100

    # Calculate Value
    value = max_val * 100

    return hue, saturation, value
```

- Preserved exact function signature and return type
- Maintained all numerical calculations and edge case handling
- Improved variable naming for clarity (e.g., `mx` → `max_val`, `mn` → `min_val`)
- Added docstring explaining the function's purpose and return value ranges
- Added type hints without changing runtime behavior
- Kept the same algorithmic approach and mathematical operations
- Maintained the same behavior for all edge cases (grayscale, pure colors, etc.)
- Preserved the exact same return value formatting and ranges
- No changes to exception handling (none in original)
