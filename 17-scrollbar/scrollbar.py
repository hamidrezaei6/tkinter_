from tkinter import *

root = Tk()
root.geometry('660x250')

txt = Text(root,bg='skyblue')
txt.pack(side=LEFT,fill=Y)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)

txt.config(yscrollcommand=scroll.set)

scroll.config(command=txt.yview)




root.mainloop()