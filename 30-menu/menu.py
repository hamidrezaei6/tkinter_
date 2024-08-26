import tkinter
from tkinter import * 

root = Tk()

def doNothing():
    pass


mu = Menu(root)   # menu parent

fileMenu = Menu(mu,tearoff=0)
editMenu = Menu(mu,tearoff=0)
helpMenu = Menu(mu,tearoff=0)

mu.add_cascade(label='File',menu=fileMenu)
mu.add_cascade(label='Edit',menu=editMenu)
mu.add_cascade(label='Help',menu=helpMenu)

root.config(menu=mu)

fileMenu.add_command(label='new',command=doNothing)
fileMenu.add_command(label='open',command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='exit',command=root.quit)


editMenu.add_command(label='copy',command=doNothing)
editMenu.add_command(label='cut',command=doNothing)
editMenu.add_command(label='paste',command=doNothing)


helpMenu.add_command(label='help',command=doNothing)
aboutMenu = Menu(helpMenu,tearoff=0)
helpMenu.add_cascade(label='about',menu=aboutMenu)
aboutMenu.add_command(label='about us',command=doNothing)











root.mainloop()