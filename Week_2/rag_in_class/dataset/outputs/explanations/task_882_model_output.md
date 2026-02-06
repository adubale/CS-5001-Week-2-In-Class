# Model output for task_882

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parallelogram_perimeter(b,h):
  perimeter=2*(b*h)
  return perimeter

## Refactored Code:

```python
def parallelogram_perimeter(base: float, height: float) -> float:
    """Calculate the perimeter of a parallelogram given its base and height.

    Args:
        base: The length of the base of the parallelogram.
        height: The height of the parallelogram.

    Returns:
        The perimeter of the parallelogram (2 * base * height).
    """
    return 2 * (base * height)
```

- Renamed parameters from `b` and `h` to `base` and `height` for clarity while preserving function signature
- Added type hints and docstring without changing runtime behavior
- Simplified the implementation by removing the intermediate variable `perimeter`
- Maintained exact mathematical behavior (2 * base * height)
- Preserved all edge-case handling (zeros, negatives, etc.) as the formula remains unchanged
- Kept the same return type (float) and no exceptions are raised
- No changes to mutation behavior (none in original)
- No changes to observable output order (not applicable for this function)
