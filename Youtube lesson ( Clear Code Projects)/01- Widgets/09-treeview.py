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

# table.insert(parent = '', index = 0, values = ('John', 'Doe', 'JohnDoe@email.com'))
for i in range(100):
	first = choice(first_names)
	last = choice(last_names)
	email = f'{first[0]}{last}@email.com'
	data = (first, last, email)
	table.insert(parent = '', index = 0, values = data)

table.insert(parent = '', index = tk.END, values = ('XXXXX', 'YYYYY', 'ZZZZZ'))

# events
def item_select(_):
	print(table.selection())
	for i in table.selection():
		print(table.item(i)['values'])
	# table.item(table.selection())

def delete_items(_):
	print('delete')
	for i in table.selection():
		table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)
# run
root.mainloop()
