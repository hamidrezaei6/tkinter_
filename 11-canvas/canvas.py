from tkinter import * 

window = Tk()
window.title('Canvas')

cv = Canvas(window,bg='lime',width=400,height=300)
cv.pack(side=LEFT)

cv1 = Canvas(window,bg='cyan',width=400,height=300)
cv1.pack(side=RIGHT)





window.mainloop()