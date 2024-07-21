import MagicTK.base as m
import tkinter as tk

root = m.Window([10, 10], [200, 200], "MagicTK")

c = tk.Canvas(root)
c.pack(fill='both')

m.RoundedRectangle(c, [10, 10], [100, 45], 5, "#ff5f5f")
m.Text(c, [10, 60], text="Hello World", fg="#000000")

m.Button(c, [100, 80], [20, 12], "Hello World", "#fafafa", "#000000", lambda: print(666))
m.Label(c, [100, 120], "Hello World", "#000000")

root.mainloop()
