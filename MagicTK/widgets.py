import tkinter as tk
import tkShadow as tks
import typing

from . import graphics as gh
from . import animations as amt


class BaseWidget:

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], text: str, bg: str, fg: str,
                 command: typing.Callable[..., typing.Any] | None = None) -> None:
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

    def config(self, **kw):
        ...

    def create_shadow(self, *args):
        ...


class Button(BaseWidget):

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], text: str, bg: str, fg: str,
                 command: typing.Callable[..., typing.Any] | None = None) -> None:
        super().__init__(master, position, size, text, bg, fg, command)

        self.displayText = gh.Text(
            self.master, [0, 0], self.text, self.color, placemode='normal')
        self.background = gh.Rectangle(self.master, position, [
                                       self.displayText.width+20, self.displayText.height+20], self.fill)
        self.master.lift(self.displayText.canvasId, self.background.canvasId)

        self.bbox = self.master.bbox(self.background.canvasId)
        self.textPos = [self.x+(self.bbox[2]-self.bbox[0])/2,
                        self.y+(self.bbox[3]-self.bbox[1])/2]
        self.displayText._position(self.textPos)

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
            self.background.canvasId, fill=self.darken_color(self.background.fill), outline=self.darken_color(self.background.fill))
        if self._command:
            self._command()

    def __end_click(self, event: tk.Event):
        self.master.itemconfigure(
            self.background.canvasId, fill=self.background.fill, outline=self.background.fill)

    @typing.override
    def config(self, **kw):
        if "position" in kw:
            self.background._position(kw["position"])

            self.textPos = [
                kw["position"][0]+(self.bbox[2]-self.bbox[0])/2, kw["position"][1]+(self.bbox[3]-self.bbox[1])/2]
            self.displayText._position(self.textPos)
            return
        if "text" in kw:
            self.displayText._text(kw["text"])
            return
        if "bg" in kw:
            self.background._bg(kw["bg"])
            return
        if "fg" in kw:
            self.displayText._fg(kw["fg"])
            return
        return

    @typing.override
    def create_shadow(self, offset: tuple[int | float, int | float], blur_radius: int | float = 4.5,
                      color: str = "#000000"):
        self.shadow = tks.Shadow(
            self.background.canvasId, self.master, offset[0], offset[1], blur_radius, color)
        self.shadow.show()
        self.master.lift(self.displayText.canvasId, self.background.canvasId)


class RoundedButton(BaseWidget):

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float],
                 size: tuple[int | float, int | float], radius: int | float, text: str, bg: str, fg: str,
                 command: typing.Callable[..., typing.Any] | None = None) -> None:
        super().__init__(master, position, size, text, bg, fg, command)

        self.radius = radius

        self.displayText = gh.Text(
            self.master, [0, 0], self.text, self.color, placemode='normal')
        self.background = gh.RoundedRectangle(self.master, position,
                                              [self.displayText.width+15, self.displayText.height+15], self.radius,
                                              self.fill)

        self.displayText._position([self.x+self.width/2, self.y+self.height/2])
        print([self.x+self.width/2, self.y+self.height/2])
        
        for Id in self.background.canvasId:
            Id: gh.PerfectCircle | gh.Rectangle
            self.master.lift(self.displayText.canvasId, Id.canvasId)


class Label(BaseWidget):

    def __init__(self, master: tk.Canvas, position: tuple[int | float, int | float], text: str, fg: str) -> None:
        super().__init__(master, position, [0, 0], text, "", fg, None)

        self.displayText = gh.Text(
            self.master, position, self.text, self.color)

    @typing.override
    def config(self, **kw):
        if "position" in kw:
            self.displayText._position(kw["position"])
            return
        if "text" in kw:
            self.displayText._text(kw["text"])
            return
        if "fg" in kw:
            self.displayText._fg(kw["text"])
            return
        return
