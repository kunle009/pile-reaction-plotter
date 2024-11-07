def hex_to_rgb(hex_code):
    """Convert hex color code to RGB tuple."""
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i : i + 2], 16) for i in (0, 2, 4))


def hex_to_aci(hex_code):
    """Map hex code to ACI color index. ACI accepts values 1-255."""
    rgb = hex_to_rgb(hex_code)

    # This is a simple direct mapping example, in practice you could use
    # a more sophisticated algorithm or a predefined lookup table.
    # For now, let's map based on intensity.
    intensity = sum(rgb) // 3  # Average out the RGB values

    if intensity < 30:
        return 1  # Black
    elif intensity < 128:
        return 7  # Dark Gray
    elif intensity < 200:
        return 8  # Light Gray
    else:
        return 255  # White
