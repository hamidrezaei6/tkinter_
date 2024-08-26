from tkinter import *

win = Tk()

# StringVar() , IntVar() , BoolVar()

c1 = StringVar()
c2 = StringVar()


cb1 = Checkbutton(win,text='TopLearn',variable=c1,onvalue='TopLearn',offvalue='None',height=2)
cb2 = Checkbutton(win,text='LearnBy',variable=c1,onvalue='LearnBy',offvalue='None',height=2)


cb1.pack()
cb2.pack()


win.mainloop()