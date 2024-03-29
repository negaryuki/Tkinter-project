import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.geometry('600x400')
root.title('Menu')

# Menu
menu = tk.Menu(root)

# Sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="new", command=lambda: print("New file"))
menu.add_cascade(label="File", menu=file_menu)

root.configure(menu=menu)
# Run
root.mainloop()
