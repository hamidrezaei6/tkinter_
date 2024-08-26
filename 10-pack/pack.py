from tkinter import *

win = Tk()
win.geometry('300x300')

btn1 = Button(win,text='btn1')
btn2 = Button(win,text='btn2')
btn3 = Button(win,text='btn3')
btn4 = Button(win,text='btn4')


# pack -- >> side-->> TOP , RIGHT ,LEFT , BOTTOM
# fill -->> 'y' , 'x'
btn1.pack(side=RIGHT)
btn2.pack(side=LEFT,fill='y')
btn3.pack(side=TOP)
btn4.pack(side=BOTTOM)




win.mainloop()