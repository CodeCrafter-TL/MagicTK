import tkinter as tk
import time
import MagicTK.tools as tools

def interpolate_color(start_color: str, end_color: str, steps: int):
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

colors = interpolate_color("#001b5c", "#bb562d", 15)

def animate():
    for i in range(15):
        rt.after(i*10, print(colors[i]))

rt = tk.Tk()

rt.after(1000, animate)

rt.mainloop()
