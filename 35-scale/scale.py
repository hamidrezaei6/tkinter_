from tkinter import *

root = Tk()
root.title('scale')
root.geometry('400x400')


def check():
    scale_value = scale.get()
    if scale_value > 10:
        print('bigger than 10')
    else:
        print('lower than 10')


scale = Scale(root, from_=0, to=25, orient=HORIZONTAL, resolution=0.1)
scale.pack()


# scale1 = Scale(root,from_=0,to=25,orient=VERTICAL,resolution=0.1)
# scale1.pack()

btn = Button(root, text='get value', command=check)
btn.pack()


root.mainloop()
