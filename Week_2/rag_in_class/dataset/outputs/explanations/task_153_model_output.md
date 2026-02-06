# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a: float, b: float, c: float) -> tuple[float, float]:
    """Calculate the vertex (x, y) of a parabola defined by ax² + bx + c.

    Args:
        a: Coefficient of x² (must not be zero)
        b: Coefficient of x
        c: Constant term

    Returns:
        A tuple (x, y) representing the vertex coordinates.

    Note:
        This implementation preserves the exact mathematical formula and behavior
        of the original implementation, including potential floating-point precision.
    """
    x = (-b) / (2 * a)
    y = ((4 * a * c) - (b * b)) / (4 * a)
    return (x, y)
```

- Preserved exact mathematical formula and floating-point behavior
- Added type hints and docstring without changing runtime behavior
- Improved variable naming for clarity (x, y instead of unpacked tuple)
- Maintained identical function signature and return structure
- Kept the same calculation order to preserve numerical semantics
- No changes to edge case handling (e.g., division by zero would still occur if a=0)
- Preserved tuple return format exactly as original
- No changes to mutation behavior (function is pure)
- Maintained identical exception behavior (would raise ZeroDivisionError if a=0)
