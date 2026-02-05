# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    x = -b / (2 * a)
    y = (4 * a * c - b * b) / (4 * a)
    return (x, y)
```

- Preserved exact mathematical formula for vertex calculation
- Separated x and y calculations for clarity
- Maintained tuple return type with (x, y) order
- No rounding or precision loss in calculations
- Handled edge cases implicitly (division by zero would raise exception as in original)
- Preserved original function signature and name
- Improved readability with clear variable names
- Maintained exact floating-point precision requirements
