from tkinter import *

root = Tk()
root.geometry('400x250')

# Label(root,text="Hello Tkinter",width=30,height=20,fg="black",bg="#63bfb8",font="tahoma").pack()

lbl1 = Label(root,text="Hello Tkinter",width=15,height=5,fg="black",bg="#63bfb8",font="tahoma")
lbl1.pack()


lbl2 = Label(root,text="Hello Tkinter2",width=15,height=5,fg="black",bg="#63bfb8",font="tahoma")
lbl2.pack()

lbl3 = Label(root,text="Hello Tkinter3",width=15,height=5,fg="black",bg="#63bfb8",font="tahoma")
lbl3.pack()



root.mainloop()