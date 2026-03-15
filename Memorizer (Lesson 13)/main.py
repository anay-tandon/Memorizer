from tkinter import *
from tkinter.filedialog import *

screen = Tk()
screen.title("Memorizer")

def openFile():
    # opens file using dialog
    fin  = askopenfile(title = "Open File")
    # if filename selected
    if fin is not None:
        box.delete(0, END)
        # read lines and insert into listbox
        items = fin.readlines()
        for item in items:
            box.insert(END, item.strip())

def saveFile():
    # opens file using dialog
    fout = asksaveasfile(defaultextension=".txt")
    # if filename selected
    if fout is not None:
        # get all items from listbox
        for item in box.get(0, END):
            print(item.strip(), file = fout)
    # delete all items from listbox
    box.delete(0, END)

def addItem():
    box.insert(END, Entry1.get())
    Entry1.delete(0, END)

def deleteItem():
    index = box.curselection()
    if index:
        box.delete(index)

screen.geometry("800x500")

Open = Button(screen, text = "OPEN" , width = 15, command = openFile)
Open.pack(side = LEFT, padx = 5, pady = 5)

Delete = Button(screen, text = "DELETE" , width = 15, command = deleteItem)
Delete.pack(side = RIGHT, padx = 5, pady = 5)

Save = Button(screen, text= "SAVE" , width = 15, command = saveFile)
Save.pack(padx = 5, pady = 5)

Entry1 = Entry(screen, width = 35)
Entry1.pack(pady = 5, padx = 5)

Add = Button(screen, text= "ADD" , width = 15, command = addItem)
Add.pack(pady = 5, padx = 5)

frame = Frame(screen)
frame.pack(pady = 5, padx = 5)

ScrollBar = Scrollbar(frame, orient = VERTICAL)
ScrollBar.pack(side = RIGHT, fill = Y)

box = Listbox(frame, width = 70, bg = "red", yscrollcommand = ScrollBar.set)
box.pack(pady = 25)

ScrollBar.config(command = box.yview)

screen.mainloop()
