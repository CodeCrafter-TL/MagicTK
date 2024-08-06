from PIL import Image, ImageDraw
import typing


def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color: tuple[int, int, int]):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)


def create_image(size: typing.Tuple[int, int], color: typing.Tuple[int, int, int, float]) -> Image.Image:
    img_obj = Image.new("RGBA", size, color)
    return img_obj

def interpolate_color(start_color: str, end_color: str, steps: int):
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    r_step = (end_rgb[0] - start_rgb[0]) / (steps - 1)
    g_step = (end_rgb[1] - start_rgb[1]) / (steps - 1)
    b_step = (end_rgb[2] - start_rgb[2]) / (steps - 1)

    interpolated_colors = []
    for i in range(steps):
        r = round(start_rgb[0] + i * r_step)
        g = round(start_rgb[1] + i * g_step)
        b = round(start_rgb[2] + i * b_step)

        interpolated_color = rgb_to_hex((r, g, b))
        interpolated_colors.append(interpolated_color)

    return interpolated_colors