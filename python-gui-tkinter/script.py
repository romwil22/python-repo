# CREATING GUI WINDOWS AND ADDING WIDGETS
from tkinter import *

window = Tk()

def km_to_miles():
    miles = round(float(entryValue.get()) * 1.6, 2)
    text.insert(END, str(miles) + "m")

# button
bt1 = Button(window, text="Submit", command=km_to_miles)
bt1.grid(row=0, column=0)

# entry
entryValue = StringVar()
entry = Entry(window,textvariable=entryValue)
entry.grid(row=0, column=1)

# text
text = Text(window, width=15, height=1)
text.grid(row=0, column=2)

window.mainloop()
