import cmath
import math

def angle_complex(a, b):
    """Calculate the phase angle of the complex number formed by a and b.

    Args:
        a: Real part of the complex number
        b: Imaginary part of the complex number

    Returns:
        The phase angle in radians, precise to at least 15 decimal places
    """
    # Create the complex number from a and b
    cn = complex(a, b)

    # Calculate the phase angle using cmath.phase
    # Note: cmath.phase handles all edge cases including zero magnitude
    angle = cmath.phase(cn)

    # Return the angle with full precision
    return angle
