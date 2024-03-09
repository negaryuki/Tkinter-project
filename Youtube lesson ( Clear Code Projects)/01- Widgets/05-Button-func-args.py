import tkinter as tk
from tkinter import ttk


# Function
def button_func(entry_string):
    print('Button was pressed')
    print(entry_string.get())


def outer_func(parameter):
    def inner_func():
        print("button was pressed")
        print(parameter.get())
    return inner_func()


# Window
root = tk.Tk()
root.title('Button, Functions and Arguments')

# Widgets
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(root, textvariable=entry_string)
entry.pack()

button = ttk.Button(root, text="button", command=outer_func(entry_string))
button.pack()

# Run
root.mainloop()
