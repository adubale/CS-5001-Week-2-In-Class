import cmath
from typing import Union

def len_complex(a: Union[int, float], b: Union[int, float]) -> float:
    """Calculate the magnitude (length) of a complex number given its real and imaginary parts.

    Args:
        a: The real part of the complex number.
        b: The imaginary part of the complex number.

    Returns:
        The magnitude (length) of the complex number as a float.
    """
    complex_number = complex(a, b)
    return abs(complex_number)
