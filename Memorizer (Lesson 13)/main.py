from tkinter import *

screen = Tk()
screen.title("Memorizer")

screen.geometry("800x500")

Open = Button(screen, text = "OPEN" , width = 15)
Open.pack(side = LEFT, padx = 5, pady = 5)

Delete = Button(screen, text = "DELETE" , width = 15)
Delete.pack(side = RIGHT, padx = 5, pady = 5)

Save = Button(screen, text= "SAVE" , width = 15)
Save.pack(padx = 5, pady = 5)

Entry1 = Entry(screen, width = 35)
Entry1.pack(pady = 5, padx = 5)

Add = Button(screen, text= "ADD" , width = 15)
Add.pack(pady = 5, padx = 5)

frame = Frame(screen)
frame.pack(pady = 5, padx = 5)

ScrollBar = Scrollbar(frame, orient = VERTICAL)
ScrollBar.pack(side = RIGHT, fill = Y)

box = Listbox(frame, width = 70, bg = "red", yscrollcommand = ScrollBar.set)
box.pack(pady = 25)

ScrollBar.config(command = box.yview)

screen.mainloop()