import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.title('TKinter Variables')


def button_func():
    print(string_var.get())
    string_var.set("button pressed")


# tkinter variable -. to connect label and entry to each other
string_var = tk.StringVar()

# widget
label = ttk.Label(master=root, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=root, textvariable=string_var)
entry.pack()

button = ttk.Button(master=root, text="button", command=button_func)
button.pack()

root.mainloop()
