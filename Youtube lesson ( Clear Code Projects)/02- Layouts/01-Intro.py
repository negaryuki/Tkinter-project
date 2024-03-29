import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.title('Layout intro')
root.geometry('600x400')

# widgets
label1 = tk.Label(root, text='Label 1',
                  background='red')  # I used tk instead of ttk , because my system did not support ttk colors
label2 = tk.Label(root, text='Label 2', background='blue')

# pack
# label1.pack(side='left', expand=True, fill='x')
# label2.pack(side='left', expand=True, fill='both')

# Grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# label1.grid(row=0,column=1, sticky= 'nsew')  # to which direction should the widget stick
# label2.grid(row=1,column=1,sticky='nsew', columnspan= 2)

# place
label1.place(x=100,y=150,width=200,height=100)  # unexpectedly, the higher y number is, the further down the axis goes
label2.place(relx=0.5, rely=0.4, relwidth=1, anchor='center')   # anchor is the point the widget is located at

# run
root.mainloop()
