import tkinter as tk
from tkinter import ttk


def button_func():
    print('a button was pressed')


def exercise_button_func():
    print('hello')


# create a window
root = tk.Tk()
root.title('Window and Widgets')
root.geometry('800x500')

# ttk label
label = ttk.Label(master=root, text='This is a test')
label.pack()

# tk.text
text = tk.Text(master=root)
text.pack()

# ttk entry
entry = ttk.Entry(master=root)
entry.pack()

# exercise label
exercise_label = ttk.Label(master=root, text="my label")
exercise_label.pack()

# ttk button
button = ttk.Button(master=root, text='A button', command=button_func)
button.pack()

# exercise_button = ttk.Button(master = window, text = 'exercise button', command = exercise_button_func)
exercise_button = ttk.Button(master=root, text='exercise button', command=lambda: print('hello'))
exercise_button.pack()

# run
root.mainloop()
