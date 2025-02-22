color_harmony = {
    "beige": ["brown", "black", "white"],
    "brown": ["beige", "olive", "dark green"],
    "black": ["white", "gray", "navy"],
    "white": ["black", "beige", "blue"],
    "blue": ["white", "gray", "tan"],
    "red": ["black", "gray", "white"],
    "gray": ["black", "white", "blue"],
    "olive": ["brown", "black", "gray"],
    "navy": ["white", "gray", "black"],
    "tan": ["blue", "white", "black"]
}

def get_matching_colors(base_color):
    """Devuelve los colores compatibles con base_color"""
    return color_harmony.get(base_color.lower(), [])
