from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x200')

userName = Label(root,text='username :')
userName.pack(side=LEFT)

userName_entry = Entry(root,show='*')
userName_entry.pack(side=LEFT)

def get_data():
    messagebox.showinfo('welcome',userName_entry.get())

btn = Button(root,text='Click me',fg='cyan',bg='black',command=get_data)
btn.pack(side=LEFT)


root.mainloop()