import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.geometry('600x400')
root.title('Menu')

# Menu
menu = tk.Menu(root)

# Sub menu 1
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="new", command=lambda: print("New file"))
file_menu.add_command(label="open", command=lambda: print("Open"))
file_menu.add_separator()
menu.add_cascade(label="File", menu=file_menu)

# Sub Menu 2
help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help Me", command=lambda: print("Help"))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='check',onvalue='on', offvalue= 'off', variable=help_check_string)

root.configure(menu=menu)
# Run
root.mainloop()
