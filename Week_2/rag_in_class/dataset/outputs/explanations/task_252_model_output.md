# Model output for task_252

## Model
- devstral-small-2:24b-cloud

## Original Code:

import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num) 

## Refactored Code:

```python
import cmath
from typing import Union, Tuple

def convert(numbers: Union[complex, float, int]) -> Tuple[float, float]:
    """
    Convert a complex number or real number to its polar form (magnitude, phase in radians).

    Args:
        numbers: A complex number or real number to convert.

    Returns:
        A tuple (magnitude, phase) representing the polar form of the input number.
    """
    magnitude, phase = cmath.polar(numbers)
    return (magnitude, phase)
```

- Preserved the exact function signature and return type
- Added type hints for better readability without changing behavior
- Added a clear docstring explaining the function's purpose and parameters
- Extracted the tuple unpacking into named variables for clarity
- Maintained the exact same return structure (tuple of two floats)
- Kept the use of cmath.polar() which is the core behavior
- No changes to numerical precision or edge case handling
- The refactored version is functionally identical to the original
