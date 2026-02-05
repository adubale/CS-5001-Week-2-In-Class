import cmath

def angle_complex(a, b):
    """Calculate the phase angle of the complex number formed by a and b.

    Args:
        a: Real part of the complex number
        b: Imaginary part of the complex number

    Returns:
        The phase angle in radians as a float with precision to at least 15 decimal places
    """
    complex_num = complex(a, b)
    angle = cmath.phase(complex_num)
    return angle
