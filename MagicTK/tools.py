def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color: tuple[int, int, int]):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)