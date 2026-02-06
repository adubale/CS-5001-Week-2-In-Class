import cmath
from typing import Union, List, Tuple

def convert(numbers: Union[complex, List[complex]]) -> Union[Tuple[float, float], List[Tuple[float, float]]]:
    """
    Convert complex number(s) to polar form using cmath.polar.

    Args:
        numbers: A single complex number or a list of complex numbers.

    Returns:
        For a single complex number: tuple of (magnitude, phase) in radians.
        For a list of complex numbers: list of (magnitude, phase) tuples.
    """
    return cmath.polar(numbers)
