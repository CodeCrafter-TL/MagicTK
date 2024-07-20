import MagicTK.graphics as g

root = g.tk.Tk()

c = g.tk.Canvas(root)
c.pack(fill='both')

g.roundedRectangle(c, [10, 10], [100, 45], 5, "#ff5f5f")

root.mainloop()