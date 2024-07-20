import MagicTK.base as m
import tkinter as tk

root = tk.Tk()

c = tk.Canvas(root)
c.pack(fill='both')

m.roundedRectangle(c, [10, 10], [100, 45], 5, "#ff5f5f")
m.text(c, [10, 60], text="Hello World", fg="#000000")

m.Button(c, [100, 80], [20, 12], "Hello World", "#fafafa", "#000000", lambda: print(666))

root.mainloop()
