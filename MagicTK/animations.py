import tkinter as tk
import typing
import time
import asyncio

from . import tools


class ColorTransition:
    def __init__(self, master: tk.Canvas, widget: object, start: str, end: str, ms: float, aps: int,
                 callback: typing.Callable[..., typing.Any] | None = None) -> None:
        self.master = master
        self.widget = widget
        self.colors = [start, end]
        self.time = ms
        self.aps = aps
        self.speed = 1000 / self.aps
        self.callback = callback

    def submit_colors(self, index: int):
        self.transitions = self.interpolate_color(
            self.colors[0], self.colors[1], 16)
        self.master.itemconfigure()

    def start(self):
        self.i = 0
        self.__animate()

    def __animate(self):
        if self.i <= 16:
            self.submit_colors(self.i)
            self.master.after(self.speed, self.__animate)
            self.i += 1
        else:
            if self.callback:
                self.callback()

    def interpolate_color(self, start_color: str, end_color: str, steps: int):
        start_rgb = tools.hex_to_rgb(start_color)
        end_rgb = tools.hex_to_rgb(end_color)

        r_step = (end_rgb[0] - start_rgb[0]) / (steps - 1)
        g_step = (end_rgb[1] - start_rgb[1]) / (steps - 1)
        b_step = (end_rgb[2] - start_rgb[2]) / (steps - 1)

        interpolated_colors = []
        for i in range(steps):
            r = round(start_rgb[0] + i * r_step)
            g = round(start_rgb[1] + i * g_step)
            b = round(start_rgb[2] + i * b_step)

            interpolated_color = tools.rgb_to_hex((r, g, b))
            interpolated_colors.append(interpolated_color)

        return interpolated_colors

class ColorTransition:

    def __init__(self, delay: int, master: tk.Canvas, widget: object, start: str, end: str, ms: float, fps: int,
                 callback: typing.Callable[..., typing.Any] | None = None) -> None:
        self.delay = delay
        self.master = master
        self.widget = widget
        self.colors = [start, end]
        self.time = ms
        self.fps = fps
        # self.speed = 1000 / self.fps
        self.callback = callback
    
    def interpolate_color(self, start_color: str, end_color: str, steps: int):
        start_rgb = tools.hex_to_rgb(start_color)
        end_rgb = tools.hex_to_rgb(end_color)

        r_step = (end_rgb[0] - start_rgb[0]) / (steps - 1)
        g_step = (end_rgb[1] - start_rgb[1]) / (steps - 1)
        b_step = (end_rgb[2] - start_rgb[2]) / (steps - 1)

        interpolated_colors = []
        for i in range(steps):
            r = round(start_rgb[0] + i * r_step)
            g = round(start_rgb[1] + i * g_step)
            b = round(start_rgb[2] + i * b_step)

            interpolated_color = tools.rgb_to_hex((r, g, b))
            interpolated_colors.append(interpolated_color)

        return interpolated_colors

    def run(self):
        self.transitions = self.interpolate_color(self.colors[0], self.colors[1], 15)
        for i in range(15):
            self.master.after(self.delay, self.__submit(i))
    
    def __submit(self, index: int):
        self.widget.config(bg=self.transitions[index])
        print(index, self.transitions[index])
