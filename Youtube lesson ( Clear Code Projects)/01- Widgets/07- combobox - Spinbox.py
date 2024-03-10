import tkinter as tk
from tkinter import ttk

# setup
root = tk.Tk()
root.geometry('600x400')
root.title('Combobox and Spinbox')

# Widgets
items = ('ice cream', 'pizza', 'pasta')

food_string = tk.StringVar(value=items[0])

combo = ttk.Combobox(root, textvariable=food_string)
combo['value'] = items
# or alternatively
# combo.configure(value=items)
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text=f'selected food:{food_string.get()}'))

combo_label = ttk.Label(root, text='A Label is here ')
combo_label.pack()
# run
root.mainloop()
