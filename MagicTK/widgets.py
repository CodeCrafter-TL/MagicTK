import tkinter as tk
import typing


class Button:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float]) -> None:
        self.master = master
        
        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]


    def darkenColor(self, hex_color: str, factor=0.7):
        hex_color = hex_color.lstrip('#')

        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        dark_rgb = tuple(int(max(0, c * factor)) for c in rgb)

        dark_hex = '#{:02x}{:02x}{:02x}'.format(*dark_rgb)

        return dark_hex
