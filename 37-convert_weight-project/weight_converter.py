# 1 kg -- >> 1000 g
# 1 g -- >> 1000 mg
# 1 t -- >> 1000 kg , 2000 pound
# 1 pound -- >> 16 ounce

from tkinter import *

root = Tk()
root.title('weight converter')


def kiloGram():
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.2046
    ounce = float(e2_value.get()) * 35.274

    t1.delete('1.0', END)
    t1.insert(END, gram)

    t2.delete('1.0', END)
    t2.insert(END, pound)

    t3.delete('1.0', END)
    t3.insert(END, ounce)


e1 = Label(root, text='Input the weight in KG :')
e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value)
e3 = Label(root, text='gram')
e4 = Label(root, text='pound')
e5 = Label(root, text='ounce')

t1 = Text(root, height=5, width=30)
t2 = Text(root, height=5, width=30)
t3 = Text(root, height=5, width=30)

btn = Button(root, text='Convert', bg='skyblue',command=kiloGram)


e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
btn.grid(row=0, column=2)


root.mainloop()
