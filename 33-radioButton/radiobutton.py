from tkinter import *

root = Tk()

a = IntVar()

def code():
    y = f'value is {str(a.get())}'
    lb.config(text=y)



r1 = Radiobutton(root,text='python',variable=a,value=1,command=code)
r1.pack(anchor=W)

r2 = Radiobutton(root,text='cSharp',variable=a,value=2,command=code)
r2.pack(anchor=W)

r3 = Radiobutton(root,text='javascript',variable=a,value=3,command=code)
r3.pack(anchor=W)

lb = Label(root)
lb.pack()


root.mainloop()