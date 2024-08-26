from tkinter import *

root = Tk()
root.geometry('450x200+250+150')


def button():
    btn.quit()

btn = Button(root,text='close',fg='red',bg='black',activeforeground='white',activebackground='cyan',command=button)
btn.pack()


root.mainloop()