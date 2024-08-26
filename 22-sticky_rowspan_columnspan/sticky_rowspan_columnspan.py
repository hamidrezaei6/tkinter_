from tkinter import *

root = Tk()
root.geometry('300x200+500+200')

# sticky -->> W , E , S ,N
# rowspan , columnspan

lblName = Label(root,text='Name:').grid(row=0,column=0,sticky=W)
entryName = Entry(root).grid(row=0,column=1)

lblUserName = Label(root,text='username:').grid(row=1,column=0)
entryUserName = Entry(root).grid(row=1,column=1)


cb = Checkbutton(root,text='TopLearn').grid(row=2,columnspan=2,sticky=W)

btn = Button(root,text='Click',bg='cyan').grid(row=0,column=2,columnspan=3,rowspan=3,sticky=W+E+S+N,padx=5)


root.mainloop()