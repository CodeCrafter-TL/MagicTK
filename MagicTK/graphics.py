import tkinter as tk
import typing


class PerfectCircle:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 radius: int | float, bg: str) -> None:
        self.master = master

        self.fill = bg

        self.x = position[0]
        self.y = position[1]
        self.radius = radius
        self.diameter = self.radius * 2

        self.canvasId = self.master.create_oval(
            self.x, self.y, self.x+self.diameter, self.y+self.diameter, fill=self.fill, outline=self.fill)


class Ellipse:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], bg: str) -> None:
        self.master = master

        self.fill = bg

        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]

        self.canvasId = self.master.create_oval(
            self.x, self.y, self.x+self.width, self.y+self.height, fill=self.fill, outline=self.fill)


class Rectangle:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], bg: str) -> None:
        self.master = master

        self.fill = bg

        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]

        self.canvasId = self.master.create_rectangle(
            self.x, self.y, self.x+self.width, self.y+self.height, fill=self.fill, outline=self.fill)

    def _position(self, newPosition: tuple[int | float, int | float]):
        self.master.coords(
            self.canvasId, newPosition[0], newPosition[1], newPosition[0]+self.width, newPosition[1]+self.height)
        self.x = newPosition[0]
        self.y = newPosition[1]

    def _bg(self, newBg: str):
        self.master.itemconfigure(self.canvasId, fill=newBg, outline=newBg)
        self.fill = newBg

    def _size(self, newSize: tuple[int | float, int | float]):
        self.width = newSize[0]
        self.height = newSize[1]
        print(self.x, self.y, self.width, self.height)
        self.master.coords(self.canvasId, self.x, self.y, self.x+self.width, self.y+self.height)


class RoundedRectangle:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], radius: int | float, bg: str) -> None:
        self.master = master

        self.fill = bg
        self.radius = radius
        self.diameter = self.radius * 2

        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]
        self.roundedWidth = self.width - self.radius * 2
        self.roundedHeight = self.height - self.radius * 2

        PerfectCircle(self.master, [self.x, self.y], self.radius, self.fill)
        PerfectCircle(self.master, [self.x, self.y +
                      self.roundedHeight], self.radius, self.fill)
        PerfectCircle(self.master, [
                      self.x+self.roundedWidth, self.y+self.roundedHeight], self.radius, self.fill)
        PerfectCircle(
            self.master, [self.x+self.roundedWidth, self.y], self.radius, self.fill)
        Rectangle(self.master, [self.x, self.y+self.radius],
                  [self.diameter, self.roundedHeight], self.fill)
        Rectangle(self.master, [self.x+self.radius, self.y+self.roundedHeight],
                  [self.roundedWidth, self.diameter], self.fill)
        Rectangle(self.master, [self.x+self.roundedWidth, self.y +
                  self.radius], [self.diameter, self.roundedHeight], self.fill)
        Rectangle(self.master, [self.x+self.radius, self.y],
                  [self.roundedWidth, self.diameter], self.fill)

        Rectangle(self.master, [self.x+self.diameter, self.y+self.diameter],
                  [self.roundedWidth - self.diameter, self.roundedHeight - self.diameter], self.fill)


class Text:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 text: str, fg: str, *, placemode: typing.Literal['normal', 'usable'] = 'usable') -> None:
        self.master = master

        self.fill = fg
        self.placemode = placemode

        self.x = position[0]
        self.y = position[1]
        self.text = text

        self.canvasId = self.master.create_text(
            self.x, self.y, text=self.text, fill=self.fill)

        self.bbox = self.master.bbox(self.canvasId)
        self.width = self.bbox[2] - self.bbox[0]
        self.height = self.bbox[3] - self.bbox[1]

        if self.placemode == 'usable':
            self._usable()

    def _position(self, newPosition: tuple[int | float, int | float]):
        if self.placemode == 'normal':
            self.master.coords(self.canvasId, newPosition[0], newPosition[1])
            self.x = newPosition[0]
            self.y = newPosition[1]

    def _text(self, newText: str):
        self.master.itemconfigure(self.canvasId, text=newText)
        self.text = newText
        if self.placemode == 'usable':
            self._usable()

    def _fg(self, newFg: str):
        self.master.itemconfigure(self.canvasId, fill=newFg)
        self.fill = newFg

    def _usable(self):
        self.bbox = self.master.bbox(self.canvasId)
        self.width = self.bbox[2] - self.bbox[0]
        self.height = self.bbox[3] - self.bbox[1]

        self.master.coords(self.canvasId, self.x +
                           self.width/2, self.y+self.height/2)
