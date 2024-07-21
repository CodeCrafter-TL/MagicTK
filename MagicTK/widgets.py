import tkinter as tk
import typing

from . import graphics as gh


class BaseWidget:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], text: str, bg: str, fg: str,
                 command: typing.Callable | None = None) -> None:
        self.master = master

        self.text = text
        self.fill = bg
        self.color = fg

        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]
        self._command = command
    
    def darken_color(self, hex_color: str, factor: float | int = 0.7):
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        dark_rgb = tuple(int(max(0, c * factor)) for c in rgb)
        dark_hex = '#{:02x}{:02x}{:02x}'.format(*dark_rgb)

        return dark_hex


class Button(BaseWidget):

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], text: str, bg: str, fg: str,
                 command: typing.Callable | None = None) -> None:
        super().__init__(master, position, size, text, bg, fg, command)

        self.displayText = gh.Text(
            self.master, [0, 0], self.text, self.color, placemode='normal')
        self.background = gh.Rectangle(self.master, position, [
                                       self.displayText.width+20, self.displayText.height+20], self.fill)
        self.master.lift(self.displayText.canvasId, self.background.canvasId)

        self.bbox = self.master.bbox(self.background.canvasId)
        self.textPos = [self.x+(self.bbox[2]-self.bbox[0])/2,
                        self.y+(self.bbox[3]-self.bbox[1])/2]
        self.displayText.position(self.textPos)

        self.master.tag_bind(self.background.canvasId,
                             "<Button-1>", self.__start_click)
        self.master.tag_bind(self.displayText.canvasId,
                             "<Button-1>", self.__start_click)
        self.master.tag_bind(self.background.canvasId,
                             "<ButtonRelease-1>", self.__end_click)
        self.master.tag_bind(self.displayText.canvasId,
                             "<ButtonRelease-1>", self.__end_click)

    def __start_click(self, event: tk.Event):
        self.master.itemconfigure(
            self.background.canvasId, fill=self.darken_color(self.background.fill))
        if self._command:
            self._command()

    def __end_click(self, event: tk.Event):
        self.master.itemconfigure(
            self.background.canvasId, fill=self.background.fill)


class Label(BaseWidget):

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float], text: str, fg: str) -> None:
        super().__init__(master, position, [0, 0], text, "", fg, None)

        self.displayText = gh.Text(self.master, position, self.text, self.color)
