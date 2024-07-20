import MagicTK.graphics as g

root = g.tk.Tk()

c = g.tk.Canvas(root)
c.pack(fill='both')

g.roundedRectangle(c, [10, 10], [100, 45], 5, "#ff5f5f")
g.text(c, [10, 60], text="Hello World", fg="#000000")

root.mainloop()