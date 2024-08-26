from tkinter import *
from tkinter import messagebox



win = Tk()
win.title('messageBox')
win.geometry('300x300+500+200')


# showwarning() , showerror()
# askquestion() , askokcancel() , askyesno() , askretrycancel
def site():
    if messagebox.askokcancel('Enter','Are you sure')== YES:
        messagebox.showinfo('Toplearn','www.toplearn.com')
    else:
        messagebox.showerror('Not found','None!')

    


# askquestion() , askokcancel() , askyesno() , askretrycancel



btn = Button(win)
btn.config(text='TopLearn',bg='red',fg='cyan',command=site)
btn.pack()



win.mainloop()