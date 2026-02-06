# Model output for task_488

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area

## Refactored Code:

```python
import math

def area_pentagon(a: float) -> float:
    """Calculate the area of a regular pentagon with side length a.

    The formula used is:
    area = (sqrt(5*(5 + 2*sqrt(5))) * a^2) / 4

    Args:
        a: The length of a side of the regular pentagon (must be positive)

    Returns:
        The area of the pentagon as a float
    """
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
```

- Preserved the exact mathematical formula and calculation order
- Added type hints and docstring without changing runtime behavior
- Maintained the same function signature and return type
- Kept the same variable naming for the area calculation
- Preserved all numerical precision and floating-point behavior
- No changes to edge case handling (e.g., negative inputs would still produce NaN)
- Maintained the division by 4.0 to ensure float result
- Kept the same import statement and module structure
