from tkinter import *

root = Tk()

cv = Canvas(root,bg='pink',width=400,height=300)
cv.pack()

img = PhotoImage(file='toplearn.png')
cv.create_image(200,150,image=img,anchor=CENTER)


root.mainloop()