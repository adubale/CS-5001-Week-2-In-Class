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
