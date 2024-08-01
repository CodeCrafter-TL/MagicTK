import MagicTK.base as m
import MagicTK.animations as a
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

c = tk.Canvas(root, width=402, height=402)
c.place_configure(x=-1, y=-1)

m.RoundedRectangle(c, [25, 10], [100, 45], 5, "#ff5f5f")
m.Text(c, [25, 60], text="Hello World", fg="#000000")

b = m.Button(c, [100, 80], [20, 12], "Hello World", "#bb1c2f", None)
b.create_shadow([0.75, 2.5])
an = a.ColorTransition(750, c, b, "#bb1c2f", "#ffffff", 500, 60)
# a.ColorTransition(1000, c, b, "#bb1c2f", "#000000", 5000, 60, None).run()
an.run()
l = m.Label(c, [100, 120], "Hello World", "#000000")
l.config(text="Hello MagicTK")

root.mainloop()
