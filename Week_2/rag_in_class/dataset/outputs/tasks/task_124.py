import cmath
from typing import Union

def angle_complex(a: Union[int, float], b: Union[int, float]) -> float:
    """Calculate the phase angle of the complex number formed by a and b.

    Args:
        a: Real part of the complex number.
        b: Imaginary part of the complex number.

    Returns:
        The phase angle in radians of the complex number (a + b*1j).
    """
    complex_num = complex(a, b)
    angle = cmath.phase(complex_num)
    return angle
