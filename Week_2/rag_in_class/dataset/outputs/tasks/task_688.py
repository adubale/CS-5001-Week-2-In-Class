import cmath

def len_complex(a, b):
    """Calculate the length (magnitude) of a complex number given its real and imaginary parts.

    Args:
        a (float): Real part of the complex number.
        b (float): Imaginary part of the complex number.

    Returns:
        float: The magnitude of the complex number, calculated as sqrt(a^2 + b^2).
    """
    cn = complex(a, b)
    length = abs(cn)
    return length
