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
        Tuple of (x, y) coordinates of the vertex

    Raises:
        ZeroDivisionError: If a is zero (parabola is not defined)
    """
    x = -b / (2 * a)
    y = ((4 * a * c) - (b ** 2)) / (4 * a)
    return (x, y)
```

- Preserved exact mathematical formulas for vertex calculation
- Added type hints and docstring without changing runtime behavior
- Improved variable naming for clarity (x, y instead of vertex tuple)
- Maintained original exception behavior (ZeroDivisionError when a=0)
- Kept identical return structure (tuple of two floats)
- No changes to function signature or return type
- Mathematical operations remain in same order to preserve floating-point precision
- No changes to edge case handling (e.g., negative values, zeros)
