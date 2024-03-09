# Events: can be many things such as:
# Keyboard input
# widget change
# widdet select/deselect
# Mouse click/motion/reel

# widget.bind(event,function)
# event format: modifier-type-detail
# exp. Alt-Keypress-a

import tkinter as tk
from tkinter import ttk


# list of events
# pythontutorial.net/tkinter/tkinter-event-binding

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')


# window
root = tk.Tk()
root.geometry('600x500')
root.title('Event Binding')

# widgets
text = tk.Text(root)
text.pack()

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text='A button')
button.pack()

# events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

# window.bind('<Motion>', get_pos)

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# exercise :
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

# run
root.mainloop()
