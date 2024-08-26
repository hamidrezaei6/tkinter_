from tkinter import *

root = Tk()
root.title('Toplearn singup')
root.iconbitmap(r'E:\TopLearn\Tkinter_Course\25-signup_form\signup_form\images\logo.ico')
root.geometry('270x200+500+200')

lblUserName = Label(root,text='username :').grid(row=0,column=0,sticky=W)
entry_UserName = Entry(root)
entry_UserName.grid(row=0,column=1)

lblPassword = Label(root,text='password :').grid(row=1,column=0)
entry_password = Entry(root,show='*')
entry_password.grid(row=1,column=1)


def submit():
    resultUser = 'your username is : ' + entry_UserName.get()
    resultPass = 'your password is : ' + entry_password.get()
    lblShowUser.config(text=resultUser,bg='lime')
    lblShowPass.config(text=resultPass,bg='pink')



btn = Button(root,text='Register!',bg='skyblue',command=submit)
btn.grid(row=0,column=2,columnspan=3,rowspan=2,sticky=W+E+N+S,padx=5)


lblShowUser = Label(root)
lblShowUser.grid(row=3,column=0,rowspan=3,columnspan=5,pady=5,sticky=W+E+N+S) 

lblShowPass = Label(root)
lblShowPass.grid(row=6,column=0,rowspan=3,columnspan=5,pady=5,sticky=W+E+N+S) 

root.mainloop()