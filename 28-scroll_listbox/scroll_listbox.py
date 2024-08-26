from tkinter import *

win = Tk()

scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT,fill=Y)


listBox = Listbox(win,yscrollcommand=scrollbar.set)
listBox.pack(side=LEFT,fill=BOTH)

scrollbar.config(command=listBox.yview)

for i in range(50):
    listBox.insert(END,'TOPLEARN'+str(i))

print(listBox.size())



win.mainloop()