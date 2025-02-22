color_harmony = {
    # Neutrales
    "beige": ["brown", "black", "white", "tan", "olive"],
    "brown": ["beige", "olive", "dark green", "tan", "burgundy"],
    "black": ["white", "gray", "navy", "red", "charcoal"],
    "white": ["black", "beige", "blue", "gray", "tan"],
    "gray": ["black", "white", "blue", "charcoal", "olive"],
    "charcoal": ["gray", "black", "navy", "olive"],
    "tan": ["blue", "white", "black", "brown", "beige"],
    "sand": ["white", "olive", "brown", "tan"],

    # Azules
    "navy": ["white", "gray", "black", "beige", "burgundy"],
    "blue": ["white", "gray", "tan", "black", "brown"],
    "sky blue": ["white", "beige", "gray", "navy"],
    "denim": ["white", "gray", "black", "tan"],
    "cobalt": ["black", "gray", "white"],
    "turquoise": ["white", "tan", "brown"],

    # Verdes
    "olive": ["brown", "black", "gray", "beige", "tan"],
    "khaki": ["white", "brown", "beige", "black"],
    "emerald": ["black", "gold", "white"],
    "dark green": ["brown", "black", "gray", "gold"],
    "mint": ["white", "gray", "navy"],

    # Rojos y Rosados
    "red": ["black", "gray", "white", "navy"],
    "burgundy": ["black", "navy", "white", "gray", "beige"],
    "maroon": ["black", "white", "gray", "tan"],
    "crimson": ["black", "gray", "white"],
    "coral": ["white", "gray", "beige", "tan"],
    "pink": ["white", "gray", "tan", "navy"],

    # Amarillos y Dorados
    "yellow": ["navy", "gray", "black", "brown"],
    "gold": ["black", "brown", "white", "burgundy"],
    "mustard": ["black", "gray", "brown", "white"],

    # Naranjas
    "orange": ["white", "gray", "black", "brown"],
    "rust": ["white", "tan", "black", "olive"],

    # Púrpuras
    "purple": ["gray", "black", "white"],
    "lilac": ["white", "gray", "tan", "navy"],
    "violet": ["black", "white", "gray"]
}

def get_matching_colors(color):
    """Devuelve los colores compatibles con la armonía definida."""
    return color_harmony.get(color.lower(), [])
