import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.geometry('400x300')

# widgets
label1 = ttk.Label(root, text='Label 1', background='green')
label2 = ttk.Label(root, text='Label 2', background='red', width=50)

# grid
root.columnconfigure((0, 1), weight=1, uniform='a')
root.rowconfigure((0, 1), weight=1, uniform='a')

label1.grid(row=0, column=0)
label2.grid(row=1, column=0, sticky='nsew')

# run
root.mainloop()
