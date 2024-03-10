import tkinter as tk
from tkinter import ttk

# setup
root = tk.Tk()
root.geometry('600x400')
root.title('Canvas')

# Canvas

canvas = tk.Canvas(root, bg="white")
canvas.pack()

# canvas.create_rectangle((50, 20, 100, 200), fill = 'red', width = 10, dash = (4,2,1,1), outline = 'green')
# canvas.create_oval((200, 0, 300, 100), fill = 'green')
# canvas.create_arc(
# 	(200, 0, 300, 100),
# 	fill = 'red',
# 	start = 45,
# 	extent = 140,
# 	style = tk.CHORD,
# 	outline = 'red',
# 	width = 1)

# canvas.create_line((0, 0, 100, 150), fill = 'blue')
# canvas.create_polygon((0,0, 100,200, 300,50, 150, -50), fill = 'gray')

# canvas.create_text((100,200), text = 'this is some text', fill = 'green', width = 10)

#canvas.create_window((50, 100), window=ttk.Label(root, text=' This is a Text'))


# ----------------------------------------------------------

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill='black')


brush_size = 10
canvas.bind('<Motion>', draw_on_canvas)


# run
root.mainloop()
