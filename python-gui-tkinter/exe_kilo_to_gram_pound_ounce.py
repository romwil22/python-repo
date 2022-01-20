# CONVERTER APP GUI
from tkinter import *

window =Tk()

def kgConverter():
    # conversion equation
    gram = float(valueEntry.get()) * 1000
    pound = float(valueEntry.get()) * 2.20462
    ounce = float(valueEntry.get()) * 35.274
    
    # insert result to text gram, pound, ounce
    gramText.insert(END,str(gram))
    poundText.insert(END,str(pound))
    ounceText.insert(END,str(ounce))
    

# converter buttton
convertButton = Button(window, text="convert", command=kgConverter)
convertButton.grid(row=0,column=2)

# kilo/s entry field
kgValue = StringVar()
valueEntry = Entry(window,textvariable=kgValue)
valueEntry.grid(row=0,column=1)

# kilo/s label
textLabel = Label(window, text="kg")
textLabel.grid(row=0,column=0)

# text result gram, pound, and ounce
gramText = Text(window,width=10,height=1)
gramText.grid(row=1,column=0)
poundText = Text(window,width=10,height=1)
poundText.grid(row=1,column=1)
ounceText = Text(window,width=10,height=1)
ounceText.grid(row=1,column=2)

window.mainloop()