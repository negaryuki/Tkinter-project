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
help_menu.add_command(label="Help Me", command=lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=help_check_string)

# Sub menu 3
exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label="Test")
menu.add_cascade(label="Exercise", menu=exercise_menu)

exercise_sub = tk.Menu(menu, tearoff=False)
exercise_menu.add_cascade(label='Exercise Sub Menu', menu=exercise_sub)

# Menu Button

menu_button = ttk.Menubutton(root, text="Menu Button")
menu_button.pack()
button_sub = tk.Menu(menu_button, tearoff=False)
button_sub.add_command(label="Entry", command=lambda: print("Test Test"))
button_sub.add_checkbutton(label="Check")
menu_button.configure(menu=button_sub)

root.configure(menu=menu)
# Run
root.mainloop()
