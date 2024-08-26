from tkinter import *

root = Tk()

frame_1 = Frame(root,width=300,height=150,bg='skyblue')
frame_1.grid(row=0,column=0)


frame_2 = Frame(root,width=300,height=150,bg='lime')
frame_2.grid(row=1,column=0)

# btn1 , btn2 inside to frame1
btn1 = Button(frame_1,text='btn1',command=root.destroy)
btn1.grid(row=0,column=0)

btn2 = Button(frame_1,text='btn2',command=root.destroy)
btn2.grid(row=1,column=1)


# btn3 , btn4 inside to frame2
btn3 = Button(frame_2,text='btn3',command=root.destroy)
btn3.grid(row=0,column=0)

btn4 = Button(frame_2,text='btn4',command=root.destroy)
btn4.grid(row=1,column=1)

root.mainloop()