from tkinter import *

win = Tk()
win.geometry('600x400')

def doNothing():
    pass



parent_menu = Menu(win)
child_menu = Menu(parent_menu,tearoff=0)

parent_menu.add_cascade(label='file',menu=child_menu)
win.config(menu=parent_menu)

child_menu.add_command(label='new',command=doNothing)
child_menu.add_command(label='open',command=doNothing)
child_menu.add_command(label='save',command=doNothing)
child_menu.add_command(label='save as',command=doNothing)

child_menu.add_separator()
child_menu.add_command(label='exit',command=win.quit)








win.mainloop()