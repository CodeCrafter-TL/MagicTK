import tkinter as tk
import typing


class perfectCircle:

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


class ellipse:

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


class rectangle:

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


class roundedRectangle:

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

        perfectCircle(self.master, [self.x, self.y], self.radius, self.fill)
        perfectCircle(self.master, [self.x, self.y +
                      self.roundedHeight], self.radius, self.fill)
        perfectCircle(self.master, [
                      self.x+self.roundedWidth, self.y+self.roundedHeight], self.radius, self.fill)
        perfectCircle(
            self.master, [self.x+self.roundedWidth, self.y], self.radius, self.fill)
        rectangle(self.master, [self.x, self.y+self.radius],
                  [self.diameter, self.roundedHeight], self.fill)
        rectangle(self.master, [self.x+self.radius, self.y+self.roundedHeight],
                  [self.roundedWidth, self.diameter], self.fill)
        rectangle(self.master, [self.x+self.roundedWidth, self.y +
                  self.radius], [self.diameter, self.roundedHeight], self.fill)
        rectangle(self.master, [self.x+self.radius, self.y],
                  [self.roundedWidth, self.diameter], self.fill)

        rectangle(self.master, [self.x+self.diameter, self.y+self.diameter],
                  [self.roundedWidth - self.diameter, self.roundedHeight - self.diameter], self.fill)


class text:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 text: str, fg: str) -> None:
        self.master = master

        self.fill = fg

        self.x = position[0]
        self.y = position[1]
        self.text = text

        self.canvasId = self.master.create_text(
            self.x, self.y, text=self.text, fill=self.fill)
        
        self.bbox = self.master.bbox(self.canvasId)
        self.width = self.bbox[2] - self.bbox[0]
        self.height = self.bbox[3] - self.bbox[1]
        self.master.coords(self.canvasId, self.x+self.width/2, self.y+self.height/2)
