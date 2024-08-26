from tkinter import *

root = Tk()
root.geometry('200x150')

# spinbox , toplevel
spinbox = Spinbox(root,from_=2,to=25)
spinbox.pack()

tl = Toplevel(root)
btn = Button(tl,text='Exit',command=tl.destroy)
btn.pack()




root.mainloop()