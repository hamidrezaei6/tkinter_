from tkinter import *

root = Tk()
root.geometry('500x400')
root.title('config method')


# anchor --> n,nw,ne,s,sw,se,e,w
btn = Button(root, text='hello')
btn.config(text='hi Tkinter', bg='#abcabc', fg='white',
           activebackground='green', activeforeground='black', width=10, height=10,anchor=SW)

btn.pack()


root.mainloop()
