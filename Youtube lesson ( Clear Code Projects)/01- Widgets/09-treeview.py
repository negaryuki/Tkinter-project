# Treeview creates tables

import tkinter as tk
from tkinter import ttk
from random import choice

# window
root = tk.Tk()
root.geometry('600x400')
root.title('Treeview')

# treeview
table = ttk.Treeview(root, columns=('first', 'last', 'email'), show= 'headings')
table.heading('first', text='First name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack()

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# run
root.mainloop()
