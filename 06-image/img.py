from tkinter import *

root = Tk()
root.geometry('400x200')

btn = Button(root)
btn.config(text='root', fg='white', bg='pink')


# bitmap -- >> question , gray75 , gray50 , gray25 , info
# compound -- >> TOP , BOTTOM , LEFT , RIGHT --> 'top'
# cursor -- >> circle , clock , heart , plus , target , watch , arrow
# font -- >> fontname , size , bold/italic , undeline/overstrike


btn1 = Button(root)
#btn1.config(text='enter', bitmap='warning', compound=BOTTOM, bd=4,
            #cursor='target', font='tahoma 14 bold underline')

font1 = 'tahoma 14 bold underline'
img = PhotoImage(file='py.png')

btn1.config(text='enter', bitmap='warning', compound=BOTTOM, bd=4,
            cursor='arrow', font=font1,image=img)


btn.pack()
btn1.pack()


root.mainloop()
