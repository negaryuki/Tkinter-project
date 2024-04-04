import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.title('Layout intro')
root.geometry('600x400')

# widgets
label1 = tk.Label(root, text='First label', background='red')
label2 = tk.Label(root, text='Label 2', background='blue')
label3 = tk.Label(root, text='Last of the labels', background='green')
button = tk.Button(root, text='Button')

# Layout
label1.pack(side='top', fill='both', ipady=50, padx=10, pady=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', fill='both', expand=True)
button.pack(side='top', fill='both', expand= True)

# run
root.mainloop()
