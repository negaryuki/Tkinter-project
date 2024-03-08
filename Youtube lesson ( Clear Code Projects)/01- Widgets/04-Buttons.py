import tkinter as tk
from tkinter import ttk

# Setup
root = tk.Tk()
root.title('Button')
root.geometry('600x400')


# Button
def button_func():
    print("simple button")
    print(radio_var.get())


button_string = tk.StringVar()

button = ttk.Button(root, text='simple button', command=button_func, textvariable=button_string)
button.pack()

# checkbutton

check_var = tk.IntVar()   # we could use IntVar  or BooleanVar only the type of the result will change

check_button = ttk.Checkbutton(
    root,
    text="check box",
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5)      # checkbuttons use "variables" instead of "text variables" since they don't return a txt
check_button.pack()

# Radio Button

radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(root,
                         text="radio button",
                         value= 'radio 1',
                         variable= radio_var,
                         command= lambda: print(radio_var.get()))
radio1.pack()              # It is important to set a value for each radio button otherwise all radio buttons will be
                            # connected and act toghether

radio2 = ttk.Radiobutton(root,
                         text="radio button",
                         value = 2,
                         variable= radio_var,
                         command= lambda:print(radio_var.get()))
radio2.pack()


# run
root.mainloop()
