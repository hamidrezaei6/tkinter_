from tkinter import *

win = Tk()

menu_parent = Menu(win)

fileMenu = Menu(menu_parent,tearoff=0)

menu_parent.add_cascade(label='file',menu=fileMenu)

win.config(menu=menu_parent)

win.mainloop()