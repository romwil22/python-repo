"""

A program that stores this book information:
Title, Author
Year, ISBN

user can:

view all records
search an entry
add entry
update entry
delete entry
close

"""

from tkinter import *
from backend import Database

database = Database("books.db")

class Window(object):
    
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Books Database")
        
        titleLabel = Label(window, text="Title:")
        titleLabel.grid(row=0,column=0)

        self.titleEntry = StringVar()
        self.tEntry = Entry(window,textvariable=self.titleEntry)
        self.tEntry.grid(row=0,column=1)

        authorLabel = Label(window, text="Author:")
        authorLabel.grid(row=0,column=2)

        self.authorEntry = StringVar()
        self.aEntry = Entry(window,textvariable=self.authorEntry)
        self.aEntry.grid(row=0,column=3)

        yearLabel = Label(window, text="Year:")
        yearLabel.grid(row=1,column=0)

        self.yearEntry = StringVar()
        self.yEntry = Entry(window,textvariable=self.yearEntry)
        self.yEntry.grid(row=1,column=1)

        isbnLabel = Label(window, text="ISBN:")
        isbnLabel.grid(row=1,column=2)

        self.isbnEntry = StringVar()
        self.iEntry = Entry(window,textvariable=self.isbnEntry)
        self.iEntry.grid(row=1,column=3)

        self.listEntries = Listbox(window,height=6,width=35)
        self.listEntries.grid(row=2,rowspan=6, column=0,columnspan=2)

        listScrollBar = Scrollbar(window)
        listScrollBar.grid(row=2,rowspan=6,column=2)

        self.listEntries.configure(yscrollcommand=listScrollBar.set)
        listScrollBar.configure(command=self.listEntries.yview)

        self.listEntries.bind("<<ListboxSelect>>",self.get_selected_row)

        viewButton = Button(window,text="View books",width=12,command=self.view_command)
        viewButton.grid(row=2,column=3)

        searchButton = Button(window,text="Search book",width=12,command=self.search_command)
        searchButton.grid(row=3,column=3)

        addButton = Button(window,text="Add book",width=12,command=self.add_command)
        addButton.grid(row=4,column=3)

        updateButton = Button(window,text="Update book",width=12,command=self.update_command)
        updateButton.grid(row=5,column=3)

        deleteButton = Button(window,text="Delete book",width=12,command=self.delete_command)
        deleteButton.grid(row=6,column=3)

        closeButton = Button(window,text="Close",width=12,command=window.destroy)
        closeButton.grid(row=7,column=3)
    
    def view_command(self):
        self.listEntries.delete(0,END)
        for row in database.view():
            self.listEntries.insert(END, row)
        
    def search_command(self):
        self.listEntries.delete(0,END)
        for row in database.search(self.titleEntry.get(),self.authorEntry.get(),self.yearEntry.get(),self.isbnEntry.get()):
            self.listEntries.insert(END,row)
            
    def add_command(self):
        database.insert(self.titleEntry.get(),self.authorEntry.get(),self.yearEntry.get(),self.isbnEntry.get())
        self.listEntries.delete(0,END)
        self.listEntries.insert(END,(self.titleEntry.get(),self.authorEntry.get(),self.yearEntry.get(),self.isbnEntry.get()))
            
    def get_selected_row(self,event):
        try:
            global selectedTuple
            index = self.listEntries.curselection()[0]
            self.selectedTuple = self.listEntries.get(index)
            self.tEntry.delete(0,END)
            self.tEntry.insert(END,self.selectedTuple[1])
            self.aEntry.delete(0,END)
            self.aEntry.insert(END,self.selectedTuple[2])
            self.yEntry.delete(0,END)
            self.yEntry.insert(END,self.selectedTuple[3])
            self.iEntry.delete(0,END)
            self.iEntry.insert(END,self.selectedTuple[4])
        except IndexError:
            pass

        
    def delete_command(self):
        database.delete(self.selectedTuple[0])
        
    def update_command(self):
        database.update(self.selectedTuple[0],self.titleEntry.get(),self.authorEntry.get(),self.yearEntry.get(),self.isbnEntry.get())
        


    
    
window = Tk()

Window(window)

window.mainloop()