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

# spinbox
spin_int= tk.IntVar(value=12)
spin = ttk.Spinbox(root, from_=3, to=21, increment=3, command=lambda: print(spin_int.get()))
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()

# exercise----------------------------------------------------
# create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased

exercise_letters = ('A', 'B', 'C', 'D', 'E')
exercise_string = tk.StringVar(value=exercise_letters[0])
exercise_spin = ttk.Spinbox(root, textvariable=exercise_string, values=exercise_letters)
exercise_spin.pack()

exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_string.get()))

# run
root.mainloop()
