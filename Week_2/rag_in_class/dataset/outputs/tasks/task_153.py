def parabola_vertex(a: float, b: float, c: float) -> tuple[float, float]:
    """Calculate the vertex (x, y) of a parabola defined by ax² + bx + c.

    Args:
        a: Coefficient of x² (must not be zero)
        b: Coefficient of x
        c: Constant term

    Returns:
        A tuple (x, y) representing the vertex coordinates.

    Note:
        This implementation preserves the exact mathematical formula and behavior
        of the original implementation, including potential floating-point precision.
    """
    x = (-b) / (2 * a)
    y = ((4 * a * c) - (b * b)) / (4 * a)
    return (x, y)
