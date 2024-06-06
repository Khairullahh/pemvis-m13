from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(56):
    mylist.insert(END, "antrian " + str(line))

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()

