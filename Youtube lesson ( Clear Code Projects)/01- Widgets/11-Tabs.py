import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.geometry('600x400')
root.title('Tab Widgets')

# Notebook widget

notebook = ttk.Notebook(root)
tab1= ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="some random text")
label1.pack()

tab2= ttk.Frame(notebook)

notebook.add(tab1, text="TAB 1")
notebook.add(tab2, text="TAB 2")

notebook.pack()


# Run
root.mainloop()
