import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update the label
    # label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'


# print(label.configure())

# window
root = tk.Tk()
root.title('Getting and setting widgets')

# widgets
label = ttk.Label(master=root, text='Some text')
label.pack()

entry = ttk.Entry(master=root)
entry.pack()

button = ttk.Button(master=root, text='The button', command=button_func)
button.pack()


# change text back
def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'


reset_button = ttk.Button(master=root, text='reset button', command=reset_func)
reset_button.pack()

# run
root.mainloop()
