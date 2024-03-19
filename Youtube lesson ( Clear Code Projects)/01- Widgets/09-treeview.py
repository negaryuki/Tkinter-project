# Treeview creates tables

import tkinter as tk
from tkinter import ttk
from random import choice

# window
root = tk.Tk()
root.geometry('600x400')
root.title('Treeview')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(root, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)

# insert values

# table.insert(parent='', index= 0,values=('Jane','Doe','JaneDoe2024@email.com'))

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first[0]}{last}@email.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)

table.insert(parent='', index=tk.END, values=('XXXXX', 'YYYYY', 'ZZZZZ'))
# run
root.mainloop()
