import tkinter as tk
import typing
import platform

from .graphics import *
from .widgets import *


class Window(tk.Tk):

    def __init__(self, position: tuple[int | float, int | float], size: tuple[int | float, int | float],
                 title: str = "Window", bg: str | None = None, titlebar: bool = True, draggble: bool = True,
                 transparent: bool = False) -> None:
        self.x = position[0]
        self.y = position[1]

        self.width = size[0]
        self.height = size[1]

        self.wm_geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.width = self.winfo_width()
        self.height = self.winfo_height()

        self._title = title
        self.wm_title(self._title)
        self.fill = bg

        if titlebar is not True:
            self.wm_overrideredirect(titlebar)
        if draggble is not True:
            if titlebar:
                self.bind("<ButtonPress-1>", self.__restore)
                self.bind("<ButtonRelease-1>", self.__restore)
        if transparent:
            if platform.system() == 'Darwin':
                self.wm_attributes("-transparent", transparent)

    def __restore(self):
        self.wm_geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
