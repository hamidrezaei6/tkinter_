import tkinter
from tkinter import *

root = Tk()
root.geometry('200x350')

mb = Menubutton(root,text='Toplearn',relief=RAISED)
mb.pack()

mu = Menu(mb,tearoff=0)
mb.config(menu=mu)

a = StringVar()
b = StringVar()

def topLearn():
    print(a.get())
    print(b.get())

mu.add_checkbutton(label='python',variable=a,command=topLearn,onvalue='python',offvalue='None')
mu.add_checkbutton(label='Csharp',variable=b,command=topLearn,onvalue='Csharp',offvalue='Empty')




root.mainloop()