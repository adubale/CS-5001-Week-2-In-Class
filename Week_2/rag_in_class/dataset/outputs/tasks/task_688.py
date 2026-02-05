import cmath

def len_complex(a, b):
    """Calculate the length of a complex number given its real and imaginary parts.

    Args:
        a (float): Real part of the complex number.
        b (float): Imaginary part of the complex number.

    Returns:
        float: The length (magnitude) of the complex number.
    """
    cn = complex(a, b)
    length = abs(cn)
    return length
