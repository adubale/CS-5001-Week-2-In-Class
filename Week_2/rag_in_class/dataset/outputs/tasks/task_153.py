def parabola_vertex(a: float, b: float, c: float) -> tuple[float, float]:
    """Calculate the vertex (x, y) of a parabola defined by ax² + bx + c.

    Args:
        a: Coefficient of x² (must not be zero)
        b: Coefficient of x
        c: Constant term

    Returns:
        Tuple of (x, y) coordinates of the vertex

    Raises:
        ZeroDivisionError: If a is zero (parabola is not defined)
    """
    x = -b / (2 * a)
    y = ((4 * a * c) - (b ** 2)) / (4 * a)
    return (x, y)
