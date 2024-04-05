import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title,size):
        super().__init__()  # ensures that tk works well

        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])

        self.mainloop()


App("Hi",(600,600))