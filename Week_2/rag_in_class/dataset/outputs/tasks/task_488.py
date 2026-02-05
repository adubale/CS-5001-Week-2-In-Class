import math

def area_pentagon(a):
    """Calculate the area of a regular pentagon with side length a.

    Args:
        a: Side length of the pentagon (float or int)

    Returns:
        Area of the pentagon (float) with precision to at least 15 decimal places
    """
    # Validate input
    if a <= 0:
        return 0.0

    # Calculate area using exact formula: (sqrt(5*(5+2*sqrt(5)))*a^2)/4
    # Using math.sqrt for precision and pow(a, 2) for squaring
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
