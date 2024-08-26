from tkinter import *

win = Tk()

listBox = Listbox(win)
listBox.insert(0,'python')
listBox.insert(1,'cSharp')
listBox.insert(2,'java')
listBox.insert(3,'js')
listBox.insert(4,'dart')
listBox.insert(5,'flutter')
listBox.pack()

listBox.select_set(3)


def clicked():
    # print(listBox.curselection())
    print(listBox.get(listBox.curselection()))

btn = Button(win,text='Select',command=clicked)
btn.pack()



win.mainloop()