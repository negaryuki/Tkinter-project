import tkinter as tk
from tkinter import ttk

# Setup
root = tk.Tk()
root.title('Button')
root.geometry('600x400')


# Button
def button_func():
    print("simple button")


button_string = tk.StringVar()

button = ttk.Button(root, text='simple button', command=button_func, textvariable=button_string)
button.pack()

# checkbutton

check_var = tk.StringVar()   # we could use IntVar only the type of the result will change

check_button = ttk.Checkbutton(
    root,
    text="check box",
    command=lambda: print(check_var.get()),
    variable=check_var) # checkbuttons use "variables" instead of "text variables" since they don't return a txt
check_button.pack()

# run
root.mainloop()
