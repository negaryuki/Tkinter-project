import tkinter as tk
from tkinter import ttk

# Window
root = tk.Tk()
root.geometry('600x400')
root.title('Frames and Parenting Intro')

# Frame
frame = ttk.Frame(root, width=100, height=200, borderwidth=10, relief=tk.RIDGE)
frame.propagate(True)  # the size of a frame is generally adjusted by its children. we can set in off by this function
frame.pack(side='left')

# Master setting (Parenting)
label = ttk.Label(frame, text=' A Label in the Frame')
label.pack()

button = ttk.Button(frame, text='A Button in the Frame')
button.pack()

label2 = ttk.Label(root, text='A Label outside of the Frame')
label2.pack(side='left')

# Exercise:

frame2 = ttk.Frame(root, borderwidth=10, relief=tk.RIDGE)
frame2.pack(side='left')

label3 = tk.Label(frame2, text='Test Label')
label3.pack()
button3 = tk.Button(frame2, text='Test Button')
button3.pack()
entry3 = tk.Entry(frame2)
entry3.pack()

# Run
root.mainloop()
