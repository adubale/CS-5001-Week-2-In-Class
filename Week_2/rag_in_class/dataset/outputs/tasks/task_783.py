def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn

    if mx == mn:
        h = 0.0
    elif mx == r:
        h = (60.0 * ((g - b) / df) + 360.0) % 360.0
    elif mx == g:
        h = (60.0 * ((b - r) / df) + 120.0) % 360.0
    elif mx == b:
        h = (60.0 * ((r - g) / df) + 240.0) % 360.0

    s = 0.0 if mx == 0 else (df / mx) * 100.0
    v = mx * 100.0

    return (h, s, v)
