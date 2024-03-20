# In TKinter there are two widgets to define progress in one dimension
# 1.Slider -> can be moved by user or independently
# 2.Progress Bar -> can not be moved by user

import tkinter as tk
from tkinter import ttk

# Window

root = tk.Tk()
root.title("Sliders")

# slider
scale_float = tk.DoubleVar(value=20)  # tk.IntVar only stores int values
scale = ttk.Scale(root,
                  command=lambda value: print(value),
                  from_=0,
                  to=25,
                  length=300,
                  orient='vertical',
                  variable=scale_float)
scale.pack()

# run
root.mainloop()
