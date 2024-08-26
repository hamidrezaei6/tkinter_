from tkinter import *

win = Tk()
win.geometry('300x250+500+250')

# StringVar() , IntVar() , BoolVar()

c1 = StringVar()
c2 = StringVar()


cb1 = Checkbutton(win,text='TopLearn',variable=c1,onvalue='TopLearn',offvalue='None',height=2)
cb2 = Checkbutton(win,text='LearnBy',variable=c1,onvalue='LearnBy',offvalue='None',height=2)


cb1.pack()
cb2.pack()

# deselect() , select()
cb1.deselect()
cb2.deselect()

def check():
    print(c1.get())
    print(c2.get())

btn = Button(win,text='Check',bg='skyblue',command=check)
btn.pack()



win.mainloop()