from tkinter import *

win = Tk()
win.geometry('300x200')

labelFrame = LabelFrame(win,text='TopLearn')
labelFrame.pack(fill=BOTH,expand=YES)

label = Label(labelFrame,text='Toplearn.com')
label.pack()


win.mainloop()