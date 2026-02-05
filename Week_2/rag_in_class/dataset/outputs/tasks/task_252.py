import cmath

def convert(numbers):
    """Convert a complex number to polar coordinates (magnitude, angle in radians)."""
    magnitude, angle = cmath.polar(numbers)
    return (magnitude, angle)
