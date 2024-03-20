# In TKinter there are two widgets to define progress in one dimension
# 1.Slider -> can be moved by user or independently
# 2.Progress Bar -> can not be moved by user

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Window

root = tk.Tk()
root.title("Sliders")

# slider
scale_float = tk.DoubleVar(value=20)  # tk.IntVar only stores int values
scale = ttk.Scale(root,
                  command=lambda value: progress.stop(),
                  from_=0,
                  to=25,
                  length=300,
                  orient='vertical',
                  variable=scale_float)
scale.pack()

# Progress Bar
progress = ttk.Progressbar(root,
                           variable=scale_float,
                           maximum=25,
                           orient="horizontal",
                           mode='determinate',  # or "indeterminate"
                           length=300)

# progress.start(1000)  # not much useful
progress.pack()

# Scrolledtext

scroll = scrolledtext.ScrolledText(root,
                                   width=20,
                                   height=5)
scroll.pack()

# ------------------------------

exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(root, orient='vertical', variable=exercise_int)
exercise_progress.pack()
exercise_progress.start()

label = ttk.Label(root, textvariable=exercise_int)
label.pack()

exercise_scale = ttk.Scale(root, variable=exercise_int, from_=0, to=100)
exercise_scale.pack()

# run
root.mainloop()
