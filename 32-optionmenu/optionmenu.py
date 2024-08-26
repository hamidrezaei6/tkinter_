import tkinter
from tkinter import *

root = Tk()
root.geometry('200x150')

a = StringVar()
a.set('Programming')

om = OptionMenu(root,a,'python','cSharp','js','dart','flutter')
om.pack()

def get_data():
    print(a.get())

btn = Button(root,text='Select',command=get_data)
btn.pack()




root.mainloop()