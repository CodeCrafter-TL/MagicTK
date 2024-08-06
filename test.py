import MagicTK.base as m
import MagicTK.animations as a
import tkinter as tk

width, height = 800, 800
radius = 10

root = tk.Tk()
root.configure(bg='SystemTransparent')
root.wm_attributes("-transparent", 1)
root.wm_overrideredirect(1)
root.wm_geometry(f"{width}x{height}")

c = tk.Canvas(root, width=width+8, height=height+8,
              bg='SystemTransparent', bd=0, border=0, borderwidth=0)
c.place_configure(x=-4, y=-4)
m.RoundedRectangle(c, [4, 4], [width, height], radius, "#ffffff")
m.TopRoundedRectangle(c, [4, 4], [width, radius*2], radius, "#eaeaea")
c.create_oval(10, 8, 22, 20, fill='#FF5F57', outline="#FF5F57")
c.create_oval(30, 8, 42, 20, fill='#FEBC2E', outline="#FEBC2E")
c.create_oval(50, 8, 62, 20, fill='#28C840', outline="#28C840")
c.create_text(width/2, radius*1.5, fill='#000000', text='tk')

"""m.RoundedRectangle(c, [25, 10], [100, 45], 5, "#ff5f5f")
m.Rectangle(c, [25, 90], [100, 40], "#1c8df3")
m.Rectangle(c, [5, 5], [100, 40], "#1c8df3", 0.4)
m.Text(c, [25, 60], text="Hello World", fg="#000000")

b = m.Button(c, [100, 80], [20, 12], "Hello World", "#bb1c2f", None)
b.create_shadow([0.75, 2.5])
# an = a.ColorTransition(750, c, b, "#bb1c2f", "#ffffff", 500, 60)
# a.ColorTransition(1000, c, b, "#bb1c2f", "#000000", 5000, 60, None).run()
# an.run()
l = m.Label(c, [100, 120], "Hello World", "#000000")
l.config(text="Hello MagicTK")"""

aa = tk.Toplevel(root)
aa.wm_geometry("800x800")
aa.configure(bg="#ffffff")
aa.mainloop()

root.mainloop()
